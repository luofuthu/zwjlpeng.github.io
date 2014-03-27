Date: 2014-03-20
Title: velocity初始化过程分析读取配置文件
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_6
Img:pics/company/taobao.jpg
summary:有了上面的单实例模式与多实例模式，下要要分析的就是Velocity引擎的初始化过程，上面代码中我们一直没有细讲的就是`ri.init()`,这个`init()`方法里的内容，现在就看看这个里面到底是什么，代码如下，现在就看看这个里面到底是什么，代码如下，这行代码是读取配置文件，由于我们执行的是,这个init方法里面没有指定配置文件，...

----------

**本系列教程，为个人在淘宝实习所写，博文中所提及的WebX为淘宝的架构，大家可以忽略，当然有兴趣的，也可以自已去搜搜，淘宝的WebX目前处于开源状态**

**Velocity引擎解惑**

1、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">Velocity入门教程HelloWord程序</a>

2、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_2.html" target="_blank">Velocity入门例子自定义呈现容器</a>

3、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>


4、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html" target="_blank">Velocity入门例子创建普通的web工程</a>

5、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_5.html" target="_blank">Velocity中的单例模式以及多实例模式</a>

有了上面的单实例模式与多实例模式，下要要分析的就是Velocity引擎的初始化过程，上面代码中我们一直没有细讲的就是ri.init(),这个init()方法里的内容：
　　

	public synchronized void init()  //这是一个同步方法，增加了线程安全性
	 {    //如果未进行初始化，就会执行以下的初始化过程
	     if (!initialized && !initializing)  
	     {   //打印出调试信息
	         log.debug("Initializing Velocity, Calling init()...");
				//将初始化标志置为真  
	         initializing = true;  
	  		//无用的打钱信息
	         log.trace("*******************************************************************");  
				//又是无用的打印信息
	         log.debug("Starting Apache Velocity v@build.version@ (compiled: @build.time@)");  
	         log.trace("RuntimeInstance initializing.");  
	  	    //读取属性配置文件
	         initializeProperties();
			    //读取初始化日志文件  
	         initializeLog();  
	          //初始化资源加载器
	         initializeResourceManager();
			    //初始化VTL预指令 
	         initializeDirectives();
	          //初始化事件处理句柄
	         initializeEventHandlers(); 
			    //初始化解析池 
	         initializeParserPool();  
	          //应该是static content include system
	         initializeIntrospection();  
	         initializeEvaluateScopeSettings();  
	         /* 
	          *  initialize the VM Factory.  It will use the properties 
	          * accessable from Runtime, so keep this here at the end. 
	          */  
	          //初始化宏
	         vmFactory.initVelocimacro();  
	         log.trace("RuntimeInstance successfully initialized.");  
	         initialized = true;  
	         initializing = false;  
	     }  
	 }  


上面我已经写了注释，下面就深入代码内部进行分析一下：

**initializeProperties(读取配置文件)**

 	//读取属性配置文件
	initializeProperties();

这行代码是读取配置文件，由于我们执行的是Velocity.init()->ri.init(),这个init方法里面没有指定配置文件


	private void initializeProperties()  
	 {  
	     /* 
	      * Always lay down the default properties first as 
	      * to provide a solid base. 
	      */  
	     if (configuration.isInitialized() == false)  
	     {  
	         setDefaultProperties();  
	     }  
	  
	     if( overridingProperties != null)  
	     {  
	         configuration.combine(overridingProperties);  
	     }  
	 }


因此上面的代码中的overridingProperties会是默认值null,对比ri.init(p)代码，可以发现有参数p时会首先对overridingProperties进行初始化，如下所示

	public void init(Properties p)  
	{  
	    setProperties(ExtendedProperties.convertProperties(p));  
	    init();  
	}  

因此initializeProperties()代码的执行实际过程中只会持执行setDefaultProperties(),这个函数，看看这个函数的实现吧

	private void setDefaultProperties()  
	   {  
	       InputStream inputStream = null;  
	       try  
	       {  
	           //重要这里获取到了属性的配置文件DEFAULT_RUNTIME_PROPERTIES是默认的配
				//置文件org/apache/velocity/runtime/defaults/velocity.properties
	           inputStream = getClass()  
	               .getResourceAsStream('/' + DEFAULT_RUNTIME_PROPERTIES);  
	  		//将配置文件加载进来
	           configuration.load( inputStream );  
	           if (log.isDebugEnabled())  
	           {  
	               log.debug("Default Properties File: " +  
	                   new File(DEFAULT_RUNTIME_PROPERTIES).getPath());  
	           }  
	       }  
	       catch (IOException ioe)  
	       {  
	           String msg = "Cannot get Velocity Runtime default properties!";  
	           log.error(msg, ioe);  
	           throw new RuntimeException(msg, ioe);  
	       }  
	       finally  
	       {  
	           try  
	           {  //各种关闭呀，一看就知道
	               if (inputStream != null)  
	               {  
	                   inputStream.close();  
	               }  
	           }  
	           catch (IOException ioe)  
	           {  
	               String msg = "Cannot close Velocity Runtime default properties!";  
	               log.error(msg, ioe);  
	               throw new RuntimeException(msg, ioe);  
	           }  
	       }  
	   }  


上面的代码就是读取默认的配置文件，并将其加载进来，默认的配置文件是真的有呢，截图看看：

<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_6.html">
<img src="http://www.yanyulin.info/pics/taobao/velocity6_1.jpg" alt="烟雨林博客"/>
</a>

在默认配置文件中主要涉及的是各种配置，如下是一部份，这一部份主要涉及的是宏指令

	velocimacro.permissions.allow.inline = true  
	velocimacro.permissions.allow.inline.to.replace.global = false  
	velocimacro.permissions.allow.inline.local.scope = false  	  
	velocimacro.context.localscope = false  
	velocimacro.max.depth = 20 

这里面设置允许宏的内联，即递归，不允许全局替换，最大嵌套深度为20等等

