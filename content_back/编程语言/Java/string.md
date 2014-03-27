Date: 2013-07-31
Title: String StringBuffer StringBuilder的区别分析
Category: 编程语言
Tags: Java
Slug: string
Img:pics/java.jpg
summary:这是一道很常见的面试题目，String是不可变的对象(final)类型，每一次对String对象的更改均是生成一个新的String对象，原有的对象不会改变，相比之下StringBuffer与StringBuilder均是可更改的对象，效率要大于String,两者之间的区别在于StringBuffer适用于多线程，是线程安全的，而StringBuiler是JDK5.0后出来的，专门针对单线程，效率上要高于StringBuffer。

----------
这是一道很常见的面试题目，至少我遇到过String/StringBuffer/StringBuilder的区别：String是不可变的对象(final)类型，每一次对String对象的更改均是生成一个新的String对象，原有的对象不会改变，相比之下StringBuffer与StringBuilder均是可更改的对象，效率要大于String,两者之间的区别在于StringBuffer适用于多线程，是线程安全的，而StringBuiler是JDK5.0后出来的，专门针对单线程，效率上要高于StringBuffer。

String测试的源代码：

	//生成一个字符串对象
	String str="abc";
	//让两个tmp指向同一个字符串
	String tmp=str;
	//对字符串进行重新赋值，如果str是可以更改的，那么最终的结果就是tmp与str的值还是一样的
	str="abc"+str;
	//将结果打印出来
	System.out.println(str);//test
	System.out.println(tmp);//abc
	//时间测试，待会与后面结果对比
	long start=System.currentTimeMillis();
	for(int i=0;i<1000000;i++)
		str="a"+str;
	//平均时间会运行好久好久的，真的，你可以试试，有几分钟
	System.out.println(System.currentTimeMillis()-start);
上面的代码很显然了吧，如果String是可变对象的话，那么str与tmp的结果应该是一样的，因为指向了同一片空间，但最后结果不一样，是因为String指向的空间是一个final类型，不可更改的，执行str=”test”,实际上是又重新申请了空间存放test，然后str指向了”test”这片空间，而tmp不变，最后的时间测试中，由于每次都是由str+”a”构造出一个新的对象，然后将str指向这个新的对象，期间str原来指向的空间会由GC回收，因此会很费时的。

看看String类实现的部份源码

    public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence
    {
    /** 存放字符串的空间，看看前面的final,应该就明白了吧，修饰的内容是不可更改的*/
    private final char value[];
    
    /**偏移位置，第一个字符*/
    private final int offset;
    
    /**字符个数*/
    private final int count;
你也会发现，里面用来存储字符串的是一个char型的数组value,看看char的前面的那个final,应该明白了吧：）

StringBuffer的测试源代码：

	//生成一个StringBuffer对象,并在里面存放abc
	StringBuffer str=new StringBuffer("abc");
	//tmp也指向这个StringBuffer对象
	StringBuffer tmp=str;
	//对字符串进行重新赋值，如果str是可以更改的，那么最终的结果就是tmp与str的值还是一样的
	str=str.append("abc");
	//将结果打印出来
	System.out.println(str);//abcabc
	System.out.println(tmp);//abcabc
	//时间测试，待会与后面结果对比
	long start=System.currentTimeMillis();
	for(int i=0;i<1000000;i++)
		str=str.append("a");
	//平均时间在63ms左右
	System.out.println(System.currentTimeMillis()-start);

上面的代码也是很显然的吗，由于操作的始终是同一个对象，同一片内存空间，因此tmp与str的值是一样的，在测试时间时，由于避免了内存的释放与回收(不是绝对的避免，当内存不足以存放数据时，又重新分配一片大点的空间，总的来说就是减少的内存的释放与回收)，因此时间大大减少，效率提高了。

     public final class StringBuffer extends AbstractStringBuilder
     implements java.io.Serializable, CharSequence
     {
    static final long serialVersionUID = 3388685877147921107L;
    
    /**
     * 可以看出会有16B的默认空间 
     */
      public StringBuffer() {
    	super(16);
    }
从这里可以看出，如果什么都不存放的话，StringBuffer会有16字节的默认空间

看看StringBuffer的父类，更清楚:)

    abstract class AbstractStringBuilder implements Appendable, CharSequence {
    /**
     *这个value就是用来存放字符串的，默认情况下就是16B的空间，没有final吧:)
     */
    char value[];

看了这些，你也应该知道String与StringBuffer的区别，还有一点就是StringBuffer是线程安全的，体现在哪呢，看看源代码吧:)

    public synchronized int length() {
	return count;
    }

    public synchronized int capacity() {
	return value.length;
    }


    public synchronized void ensureCapacity(int minimumCapacity) {
	if (minimumCapacity > value.length) {
	    expandCapacity(minimumCapacity);
	}
    }

上面只是部份方法，你可以看到的是大部份的方法都含有一个synchronized关键字，这个关键字的作用就是用来进行线程同步的，因此是多线程安全的。
StringBuilder的测试源代码：

	//生成一个StringBuilder对象,并在里面存放abc
	StringBuilder str=new StringBuilder("abc");
	//tmp也指向这个StringBuffer对象
	StringBuilder tmp=str;
	//对字符串进行重新赋值，如果str是可以更改的，那么最终的结果就是tmp与str的值还是一样的
	str=str.append("abc");
	//将结果打印出来
	System.out.println(str);//abcabc
	System.out.println(tmp);//abcabc
	//时间测试，待会与后面结果对比
	long start=System.currentTimeMillis();
	for(int i=0;i<1000000;i++)
		str=str.append("a");
	//平均时间在36左右
	System.out.println(System.currentTimeMillis()-start);

上面的代码也是类似的，说明了StringBuilder与StringBuffer类似，但比StringBuffer的效率更改，这是为什么呢，看看源代码就知道了:)
源代码中StringBuffer与StringBuilder继承自同一个父类，代码极奇相似，只是StringBuilder各个函数少了synchonized关键字，这也就说明了StringBuilder不是线程安全的，即然有了synchronized关键字，那么代码每次运行的时候均需要锁住该对象，以避免其他对象调用该方法，不管是单线程还是多线程，因此这需要一定的开销，因此StringBuiler的效率要高于StringBuffer:)