Date: 2014-03-07
Title: Linux系统中并发与竞争机制分析
Category: 编程语言
Tags: Linux汇总
Slug: concurrent
Img:pics/linux.jpg
summary:现代`Linux`系统中有相非常多的并发源，导致的问题就是并发与竞争，多个并发源竞争同一个共享数据竞争的情况来自对资源的共享存取结果，当多个线程操作同一数据结构时，混乱就可能存在，在驱动编程中尽量避免共享资源，采用的方法通常是加锁机制,`PV`操作：PV操作实际上是对一个整形值进行操作，一个想进入临界区...

----------
现代`Linux`系统中有相非常多的并发源，导致的问题就是并发与竞争，多个并发源竞争同一个共享数据
竞争的情况来自对资源的共享存取结果，当多个线程操作同一数据结构时，混乱就可能存在，在驱动编程中尽量避免共享资源，采用的方法通常是加锁机制。

共享资源的互斥

`PV`操作：PV操作实际上是对一个整形值进行操作，一个想进入临界区获取共享资源的进程调用P操作，如果整形值大于0,将整形值减1，获取共享资源，否则等待，使用完后调用V操作，将整形值增1，唤醒等待的进程

`Linux`下PV实现：

要使用PV操作，必须包含`<linux/semaphore.h>,`相关的数据类型是`struct semaphore`,PV操作要进行创建然后初始化

	static inline void sema_init(struct semaphore *sem, int val)//val是pv操作的初始整形值

PV操作一般用于互斥，因此内核提供了如下的宏定义进行申明

	#define DECLARE_MUTEX(name)

如果PV操作必须在运行时初始化，内核提供了如下操作

	#define init_MUTEX(sem)		sema_init(sem, 1)
	#define init_MUTEX_LOCKED(sem)	sema_init(sem, 0)

Linux中P操作对应如下三个函数

	extern void down(struct semaphore *sem);//P操作递减整形值，如果没有，等待
	extern int __must_check down_interruptible(struct semaphore *sem);//P操作递减整形值，允许

用户可中断

	extern int __must_check down_trylock(struct semaphore *sem);//P操作不成功，立刻返回，不等待

V操作：

	extern void up(struct semaphore *sem);//信号使用完毕之后必须要返还给系统

读者写者的PV操作

Linux内核为这种情况提供了一个特殊的类型rwsem(在linux/rwsem.h中)，rwsem必须在运行时显示的初始化

	Void init_rwsem(struct rw_semaphore *sem)

Completion机制

Completion是任务使用的一个轻量级机制，允许一个线程告诉另一个线程工作已完成，为使用completion你的代码必须包括`<linux/completion.h>`

DECLARE_COMPLETION(name)创建completion

自旋锁简介<linux/spinlock.h>类型为spinlock_t,同任何其他类型一样，自旋锁必须要初始化，注意所有的自旋锁都是不可中断的，一旦你调用 spin_lock你将自旋直到锁变为可用。

对自旋锁进行操作的相关函数


	#define spin_lock_irq(lock)		_spin_lock_irq(lock)
	#define spin_lock_bh(lock)		_spin_lock_bh(lock)//获得锁之前禁止软件中断
	#define spin_lock_irqsave(lock, flags)	//获得锁之间禁止中断，之前的中断保存在flag里	
	#define spin_trylock(lock)	
	#define spin_lock(lock)	

有四个方法来释放自旋锁

	# define spin_unlock(lock)		_spin_unlock(lock)
	# define read_unlock(lock)		_read_unlock(lock)
	# define write_unlock(lock)		_write_unlock(lock)
	# define spin_unlock_irq(lock)		_spin_unlock_irq(lock)
	# define read_unlock_irq(lock)		_read_unlock_irq(lock)
	# define write_unlock_irq(lock)		_write_unlock_irq(lock)

非阻塞的自旋锁操作

	Int spin_trylock(spinlock_t *lock)
	Int spin_trylock_bh(spinlock_t *lock)

这些函数成功时返回非零，否则0，没有try版本来禁止中断

一个完整的加锁体制对于一个简单的整数值有点过分，对于这样的情况，内核提供了一个原子整数类型称为atomic_t定义在,`<asm/atomic.h>`中
