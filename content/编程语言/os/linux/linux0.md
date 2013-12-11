Date: 2013-11-19
Title: Linux中0号进程的创建分析
Category: 编程语言
Tags: Linux
Slug: linux0
Img:pics/linux.jpg
summary:Linux中1号进程是由0号进程来创建的，因此必须要知道的是如何创建0号进程，由于在创建进程时，程序一直运行在内核态，而进程运行在用户态，因此创建0号进程涉及到特权级的变化，即从特权级0变到特权级3，Linux是通过模拟中断返回来实现特权级的变化以及创建0号进程，通过将0号进程的代码段选择子以及程序计数器EIP直接压入内核态堆栈，然后利用iret汇编指令中断返回跳转到0号进程运行。

----------
`Linux`中1号进程是由0号进程来创建的，因此必须要知道的是如何创建0号进程，由于在创建进程时，程序一直运行在内核态，而进程运行在用户态，因此创建0号进程涉及到特权级的变化，即从特权级0变到特权级3，`Linux`是通过模拟中断返回来实现特权级的变化以及创建0号进程，通过将0号进程的代码段选择子以及程序计数器`EIP`直接压入内核态堆栈，然后利用iret汇编指令中断返回跳转到0号进程运行。

代码如下

	move_to_user_mode();//创建0号进程，开始进入0号进程，切换到特权级3运行
	if (!fork()) {init();｝//创建1号进程
跟踪代码：

    #define move_to_user_mode() \
    __asm__ ("movl %%esp,%%eax\n\t" \//将esp寄存器的内容存入eax中
    	"pushl $0x17\n\t" \//压入0号任务的数据段选择符
    	"pushl %%eax\n\t" \//压入堆栈指针
    	"pushfl\n\t" \//压入标志寄存器
    	"pushl $0x0f\n\t" \//压入0号任务的代码段选择符
    	"pushl $1f\n\t" \//压入EIP，即切换到0号任务后CPU运行的位置
    	"iret\n" \//中断返回指令
    	"1:\tmovl $0x17,%%eax\n\t" \//由于发生了切换，需要更改各段寄存器
    	"movw %%ax,%%ds\n\t" \//更改段寄存器ds
    	"movw %%ax,%%es\n\t" \//更改段寄存器es
    	"movw %%ax,%%fs\n\t" \//更改段寄存器fs
    	"movw %%ax,%%gs" \//更改段寄存器gs
    	:::"ax")
    
分析如下,注释已经很清楚：

代码为嵌入汇编语句的C程序，`::”ax”`表示的是输出为空，输入为空，在这个宏定义的执行过程中可以发生改变的是`ax`寄存器，这属于GNU的gas语法，不作解释

`0x17`与`0x0f`的真实意义，跟踪查看前先写成二进制形式`0x17=0000 0000 0001 0111`,`0x0f=0000 0000 0000 1111`;`0x17`与`0x0f`的后三们均是111，段选择子的后三位分别表示RPL以及TI,因此后三位即表示请示特权级为3，描述符在LDT中，故0x17与0x0f分别表示LDT中的第二项与第一项，即然是LDT表，在使用之前肯定要进行初始化，帮初始化代码肯定在move_to_user_mode之前，跟踪分析可以发现在`sched_init`中，源码如下：

    void sched_init(void)
    {
    	int i;
    //desc_struct表示是描述符表类型typedef struct desc_struct{a,b}desc_table[256];
    	struct desc_struct * p;
    	if (sizeof(struct sigaction) != 16)
    		panic("Struct sigaction MUST be 16 bytes");
    //这里开始是关键部分，gdt是全局描述符表的基地址
    //FIRST_TSS_ENTRY与FIRST_LDT_ENTRY分别是4，5即全局描述符表中的第4项
    //与第五项代表的是第一个任务，对其进行设置
    //查看static union task_union init_task = {INIT_TASK,};可以看到INIT_TASK可以看到//INIT_TASK是个宏定义，即下面的注释
    	set_tss_desc(gdt+FIRST_TSS_ENTRY,&(init_task.task.tss));
    	set_ldt_desc(gdt+FIRST_LDT_ENTRY,&(init_task.task.ldt));
    //p指向GDT表中0号任务的下一个位置，即GDT表中第6项
    	p = gdt+2+FIRST_TSS_ENTRY;
    //NR_TASKS是Linux 0.11中最多支持的进程数64个
    	for(i=1;i<NR_TASKS;i++) {
    		task[i] = NULL;
    //重复两次是因为每个进程对应一个LDT与一个TSS
    		p->a=p->b=0;
    		p++;
    		p->a=p->b=0;
    		p++;
    	}
    //将标志寄存器的NT位禁止
    	__asm__("pushfl ; andl $0xffffbfff,(%esp) ; popfl");
    //#define ltr(n) __asm__("ltr %%ax"::"a" (_TSS(n)))这是宏定义，很显然吧
    //加载当前的任务寄存器与ldtr寄存器
    	ltr(0);
    //#define lldt(n) __asm__("lldt %%ax"::"a" (_LDT(n)))
    	lldt(0);
    //定时器8253的初始化
    	outb_p(0x36,0x43);		/* binary, mode 3, LSB/MSB, ch 0 */
    //#define LATCH (1193180/HZ)，用此设置后时钟中断为每10ms一次
    	outb_p(LATCH & 0xff , 0x40);	/* LSB */
    	outb(LATCH >> 8 , 0x40);	/* MSB */
    //后面是设置定时器的中断以及打开定时器
    	set_intr_gate(0x20,&timer_interrupt);
    	outb(inb_p(0x21)&~0x01,0x21);
    	set_system_gate(0x80,&system_call);
    //备注：
    //定时器有三个锁存器，他们各有其则，锁存器0用于维护系统时钟，地址为0x40
    //锁存器1用于周期性的向DMA发送数据信号，供存储器刷新用，地址为0x41
    //锁存器2用于扬声器发出声音，地址为0x42,因此这里向0x40设定值
    }
    
`INIT_TASK`宏定义，其实就是0号任务，看起来比较混乱，其实就是初始化task_struct结构体
    
    #define INIT_TASK \
    //0表示可运行的，15表示运行时间片，15表示运行优化级
    /* state etc */	{ 0,15,15, \
    //0表示没有信号，{{}}信号处理句柄设为0，0表示不屏蔽信号
    /* signals */	0,{{},},0, \//初始化信号设置
    //将exit_code以及start_code,end_code,end_data,brk,start_stack均设为0
    /* ec,brk... */	0,0,0,0,0,0, \
    //0表示进程号，-1表示父进程，后面三个0表示,pgrp,session,leader
    /* pid etc.. */	0,-1,0,0,0, \
    //设置进程的这6个成员unsigned short uid,euid,suid; unsigned short gid,egid,sgid;
    /* uid etc */	0,0,0,0,0,0, \
    //设置进程的报警定时器以及5个时间函数
    /* alarm */	0,0,0,0,0,0, \
    //表明该进程未使用协处理器
    /* math */	0, \
    /* fs info */	-1,0022,NULL,NULL,NULL,0, \
    /* filp */	{NULL,}, \
    //这里就是很关键的一部份，表始初始化一个局部LDT表，即第一个任务的
    	{ \
    		{0,0}, \
    /* ldt */	{0x9f,0xc0fa00}, \
    		{0x9f,0xc0f200}, \
    	}, \
    //第一个任务的任务状态表，跟踪struct tss_struct可以知道其详细意义
    /*tss*/	{0,PAGE_SIZE+(long)&init_task,0x10,0,0,0,0,(long)&pg_dir,\
    	 0,0,0,0,0,0,0,0, \
    	 0,0,0x17,0x17,0x17,0x17,0x17,0x17, \
    	 _LDT(0),0x80000000, \
    		{} \
    	}, \
    }

到这了，也差不多了，额外的部份再看看第一个任务的LDT表与TSS表，由上面可知0号任务的LDT的代码段与数据段分别为{0x9f,0xc0fa00}与{0x9f,0xc0f200},根据保护模式下的定义，可以代码段的段基址为0，段限长为640KB,段属性为存在于内存中、特权级为3，代码段，同理分析得数据段的段基址为0，段限长为640KB,段属性为存在于内存中，特权级为3，数据段

第一个任务的状态表，提一下吧
    
    struct tss_struct {
    	long	back_link;	/* 16 high bits zero */
    	long	esp0;
    	long	ss0;		/* 16 high bits zero */
    	long	esp1;
    	long	ss1;		/* 16 high bits zero */
    	long	esp2;
    	long	ss2;		/* 16 high bits zero */
    	long	cr3;
    	long	eip;
    	long	eflags;
    	long	eax,ecx,edx,ebx;
    	long	esp;
    	long	ebp;
    	long	esi;
    	long	edi;
    	long	es;		/* 16 high bits zero */
    	long	cs;		/* 16 high bits zero */
    	long	ss;		/* 16 high bits zero */
    	long	ds;		/* 16 high bits zero */
    	long	fs;		/* 16 high bits zero */
    	long	gs;		/* 16 high bits zero */
    	long	ldt;		/* 16 high bits zero */
    	long	trace_bitmap;	/* bits: trace 0, bitmap 16-31 */
    	struct i387_struct i387;
    };
    
根据这个表可以看到的是任务0的内核态堆栈指针esp0=PAGE_SIZE+(long)&init_task,即第一个PCB块(task_struct)的顶部空间，PAGE_SIZE=4k,ss0=0x10,0x10查一下head.s你就会发现是gdt的第一个描述符，即内核代码段，后面还有几个是对数据段寄存器的定义以及ldt的定义