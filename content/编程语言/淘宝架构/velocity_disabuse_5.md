Date: 2014-03-19
Title: Velocity中的单例模式以及多实例模式
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_5
Img:pics/company/taobao.jpg
summary:`Velocity`作为MVC框架的V存在，与普通的JSP页面不同，它是一种模板引擎，利用先编辑完的格式作为大纲，把一些需要变化的地方作为参数传入，显示时将模板与参数合并，达到最终的输出样子，从上面的解说中，可以看出`Velocity`最根本的就是由三个部分组成，其中engine就是负责将context与template连接起来...

----------

**本系列教程，为个人在淘宝实习所写，博文中所提及的WebX为淘宝的架构，大家可以忽略，当然有兴趣的，也可以自已去搜搜，淘宝的WebX目前处于开源状态**

Velocity作为MVC框架的V存在，与普通的JSP页面不同，它是一种模板引擎，利用先编辑完的格式作为大纲，把一些需要变化的地方作为参数传入，显示时将模板与参数合并，达到最终的输出样子，从上面的解说中，可以看出Velocity最根本的就是由context,engine,template三个部分组成，其中engine就是负责将context与template连接起来。
　　


一般的**Velocity**程序编写的步骤如下：
　　
1:首先创建一个模板,如*.vm,将需要参数化或者实例化的地方用context中有关的符号标记出来，标记时采用的是VTL语言，至于VTL语言可以参考本文后面的附录。
　　
2:给context设定一些初值，这些值用来替换template中被标记的地方
　　
3:利用engine将template中需要替换的地方用context中的值替换掉，也就是所谓的合并，从而得到该模板的实例。
　　
我们在例子中的一直使用的是如下代码：

	//初始化Velocity模板  
	Velocity.init();  
	//创建一个VeloctiyContext对象  
	VelocityContext context=new VelocityContext();  
	//向VelocityContext对象中放入一个键值对  
	context.put("list", getNames());  
	Template template=null;  
	//通过静态方法获取一个模板  
	template=Velocity.getTemplate("test.vm");  
	//创建一个输出流  
	BufferedWriter writer=new BufferedWriter(new OutputStreamWriter(System.out));

将上述的代码换成如下形式，代码同样能运行，为什么？

	//初始化Velocity模板  
	VelocityEngine engine=new VelocityEngine();  
	//创建一个VeloctiyContext对象  
	VelocityContext context=new VelocityContext();  
	//向VelocityContext对象中放入一个键值对  
	context.put("list", getNames());  
	Template template=null;  
	//通过静态方法获取一个模板  
	template=engine.getTemplate("test.vm");  
	//创建一个输出流  
	BufferedWriter writer=new BufferedWriter(new OutputStreamWriter(System.out));

这大概就是Velocity里的设计模式吧，Velocity里的单实例模式与多实例模式

**Velocity引擎的单实例模式**

上述代码中1与3其实是相同的情况，都是运行与单实例模式，作为一个开发工程师，我始终相信的是没有什么比源码更具有说服力
	
Velocity.init()方法的源码如下(init方法为什么能调用是因为其是Velocity类里的静态方法，这个不用多说吧

	public static void init()  
	{  
	    RuntimeSingleton.init();  
	}  

看到这行代码，你也就会明白其实例子三与上述代码1与3中的引擎是相同回事

继续跟踪上术代码：

	public synchronized static void init()  
	{  
	    ri.init();  
	} 

从上面这行代码中，至少可以看到这是一个线程安全级的方法，这个方法里又调用了ri.init()方法，ri是什么呢，看看其定义就知道了

	private static RuntimeInstance ri = new RuntimeInstance(); 

看到了吗ri是一个静态类，静态类不属于任何对象，在类第一次加载时就会分配内存，永久驻留于内存中,哦，C++中肯定是这样的，Java中估计也是吧,因此试想一下吧，一个程序中无论有多少个线程，使用这种方式来获取引擎的话，使用的都是同一个引擎。

再看看上述代码中的

	Velocity engine=new Velocity();

看到这行，也许有人会说这应该不是一个单实例模式吧，可事实上如果你跟踪上述代码运行的过程中，你会发现上面代码生成engine的过程中调用的是默认构造函数，而Velocity中默认的构造函数是什么都不做的，那个ri.init()初始化会发生在什么时候呢，如果你跟踪可以发现会被延迟到getTemplate函数调用的时候，如下代码所示：

	public synchronized void init()  
	 {  
	     if (!initialized && !initializing)  
	     {  
	         log.debug("Initializing Velocity, Calling init()...");  
	         initializing = true;  
	  
	         log.trace("*******************************************************************");  
	         log.debug("Starting Apache Velocity v@build.version@ (compiled: @build.time@)");  
	         log.trace("RuntimeInstance initializing.");  
	  
	         initializeProperties();  
	         initializeLog();  
	         initializeResourceManager();  
	         initializeDirectives();  
	         initializeEventHandlers();  
	         initializeParserPool();  
	  
	         initializeIntrospection();  
	         initializeEvaluateScopeSettings();  
	         /* 
	          *  initialize the VM Factory.  It will use the properties 
	          * accessable from Runtime, so keep this here at the end. 
	          */  
	         vmFactory.initVelocimacro();  
	  
	         log.trace("RuntimeInstance successfully initialized.");  
	  
	         initialized = true;  
	         initializing = false;  
	     }  
	 } 

看看上面的代码，可以发现的是如果未初始化，则在调用getTempate时由于未初始化，而会调用该函数，进行初始化。

**Velocity的多实例模式**

有了单实例模式，多实例模式也是显而易见的，代码如下：

	//初始化Velocity模板  
	VelocityEngine engine=new VelocityEngine();  

跟踪代码的执行过程，可以发现如下代码：

	public VelocityEngine()  
	{  
	    // do nothing  
	} 


构造函数中没有做任何事情，但是别忘了的是，Java中构造函数没有任何代码并不一定表示不会做任何东西，这和C++类似，由于Java中属性被初始化了，因此编译器在编译字节码文件中，会将属性的初始化放在构造函数中进行，如不信，可以定个简单的程序，如下就是一个：

	public class test {  
	private String str="pp";  
	public test(){    
	}  
	}  

将生成的字节码文件，反编译生成JVM汇编指令如下：



<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_5.html">
<img src="http://www.yanyulin.info/pics/taobao/velocity5_1.jpg"   alt="烟雨林博客"/>
</a>

看到了吧str=”pp”被放在了构造函数中吧,说这个的目的，就是想让我们再看看VelocityEngine这个类里面的属性，看看吧，你会发现这个东西


	private RuntimeInstance ri = new RuntimeInstance();  


是吧，对于每次运行new VelocityEngine()，都会生成RuntimeInstance这样的一个实例，而不再是所对的对象都共享一个Velocity引擎，而是每个一个。