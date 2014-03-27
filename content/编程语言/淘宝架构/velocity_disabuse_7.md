Date: 2014-03-21
Title: velocity初始化日志系统的过程分析
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_7
Img:pics/company/taobao.jpg
summary:这个函数的作用从其名字就可以看得出来，是用来初始化日志系统的，`Velocity`会使用来默认创建一个`LogChute`的实例，第一个被创建的日志系统是其实也就是`LogChute`的子类，内部的实现是通过一个来保存信息，用来作为初始化日志系统的过程中产生的日志信息，在创建完第一个系统内置的日...

----------

**本系列教程，为个人在淘宝实习所写，博文中所提及的WebX为淘宝的架构，大家可以忽略，当然有兴趣的，也可以自已去搜搜，淘宝的WebX目前处于开源状态**

**Velocity引擎解惑**

1、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">Velocity入门教程HelloWord程序</a>

2、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_2.html" target="_blank">Velocity入门例子自定义呈现容器</a>

3、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>


4、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html" target="_blank">Velocity入门例子创建普通的web工程</a>

5、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_5.html" target="_blank">Velocity中的单例模式以及多实例模式</a>

6、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_6.html" target="_blank">velocity初始化过程分析读取配置文件</a>

这个函数的作用从其名字就可以看得出来，是用来初始化日志系统的，`Velocity`会使用`LogManger`来默认创建一个`LogChute`的实例，第一个被创建的日志系统是`HoldingLogChute`,`HoldingLogChute`其实也就是`LogChute`的子类，内部的实现是通过一个`vector`来保存信息，用来作为初始化日志系统的过程中产生的日志信息，在创建完第一个系统内置的日志实例后，才会开始真正的创建日志系统，如下是其源代码：

	private void initializeLog()  
	{  
	    // since the Log we started with was just placeholding,  
	    // let's update it with the real LogChute settings.  
	    try  
	    {  
	        LogManager.updateLog(this.log, this);  
	    }   
	    catch (Exception e)  
	    {  
	        throw new VelocityException("Error initializing log: " + e.getMessage(), e);  
	    }  
	} 


代码的关键就是调用了LogManger类的updateLog这个方法，在跟踪进入这个方法之前，让我们看看log这个属性值：


	private Log log = new Log();  

看到了这个属性值并不是我的本意，我的本意还是继续跟踪上述代码进入 

	public Log()  
	{  
	    setLogChute(new HoldingLogChute());  
	} 

再跟踪setLogChute看看

	protected void setLogChute(final LogChute chute)  
	{  
	    if (chute == null)  
	    {  
	        throw new NullPointerException("The LogChute cannot be set to null!");  
	    }  
	    this.chute = chute;  
	} 

看到这里的时候，其实我们的第一个日志系统已经创建成功，是一个默认的日志系统，叫LogChute,可以看看里面的参数为什么要加上final,这和C++里面的const是一个道理，再看看这个默认的日志系统内部实现，我们必须要看看的就是上面的setLogChute(new HoldingLogChute())，进入HoldingLogChute类，可以看到如下代码：

	private Vector pendingMessages = new Vector();  
	    private volatile boolean transferring = false;  

再回头看看我们刚开始说的，是不是明白了

好了，叉开了这么久，再看看我们的update函数，不然都忘了,其函数的实现源码如下所示：
	
	public static void updateLog(Log log, RuntimeServices rsvc) throws Exception
	{  
	    // create a new LogChute using the RuntimeServices  
	    LogChute newLogChute = createLogChute(rsvc);  
	    LogChute oldLogChute = log.getLogChute();  
	    // pass the new LogChute to the log first,  
	    // (if the old was a HoldingLogChute, we don't want it  
	    //  to accrue new messages during the transfer below)  
	    log.setLogChute(newLogChute);   
	    // If the old LogChute was the pre-Init logger,  
	    // dump its messages into the new system.  
	    if (oldLogChute instanceof HoldingLogChute)  
	    {  
	        HoldingLogChute hlc = (HoldingLogChute)oldLogChute;  
	        hlc.transferTo(newLogChute);  
	    }  
	}

上面代码的英文注释已经详细了，不需要我翻译了吧,我想说的只有一个函数就是createLogChute(rsvc)这个函数，看看其源代码，哦，源代码真是太长了，两页也显示不下，捡重要的贴吧，首先看看下面这一行代码

	Object o = rsvc.getProperty(RuntimeConstants.RUNTIME_LOG_LOGSYSTEM);  

这一行代码，其实也是读取配置文件,其中RUNTIME_LOG_LOGSYSTEM是一个常量，这个常量就是runtime.log.logsystem，这个就是前面读取的配置文件里面定义的，不一定会有哈，如果没有话，程序还会走其他途径的,不过还真没有哈，不信你打开默认的配置文件看看，真心的没有，所以o=null,程序会跳过好大的一段,执行到以下代码


	List classes = new ArrayList(); 
	    Object obj = rsvc.getProperty( RuntimeConstants.RUNTIME_LOG_LOGSYSTEM_CLASS );   

上面的代码和上面的上面的类似，RUNTIME_LOG_LOGSYSTEM_CLASS同样是一个常量，这个常量真实值是runtime.log.logsystem.class，看看配置文件里，是有这个值的，这里我列出来了，如下

	runtime.log.logsystem.class = org.apache.velocity.runtime.log.AvalonLogChute,
	org.apache.velocity.runtime.log.Log4JLogChute,org.apache.velocity.runtime.log.
	CommonsLogLogChute,org.apache.velocity.runtime.log.ServletLogChute,org.apache
	.velocity.runtime.log.JdkLogChute  


这次obj不再为NULL了，最后就是关键的代码了，太长了，不列了，说一下大概的意思，根据上面List类型变量classes存储的类全名，看看能不能生成相应日志类的实例，如果能的话就使用该日志系统，如果不能就接着遍历，直到找到一个行的，如果均不行，就抛出异常，终于到最后了


	LogChute slc = new SystemLogChute();  
	        slc.init(rsvc);  
	        log.debug("Using SystemLogChute.");


如果没有一个日志系统能够利用，就使用默认的SystemLogChute输出日志，这个日志系统实际上就是使用System.err进行日志的打印输出。

再回头看看updateLog这个函数，估计也很好理解了，就是产生一个新的日志系统，然后将旧日志系统里的数据输出到新日志系统，并将新日志系统设置为默认的。
　　

总结一下，就是当velocity没有配置runtime.log.logsystem这个属性时，就会继续寻找runtime.log.logsystem.class这个属性，默认的velocity.properties配置文件中，这个属性的值依次是:


	1:AvalonLogChute
	2:Log4JLogChute
	3:CommonsLogLogChute
	4:ServletLogChute
	5JdkLogChute


当然Velocity不会使用这么多的日志系统，只会使用第一个能实例化的日志系统。



