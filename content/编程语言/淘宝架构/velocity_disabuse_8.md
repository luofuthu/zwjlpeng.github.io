Date: 2014-03-22
Title: Velocity初始化资源加载器以及预指令
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_8
Img:pics/company/taobao.jpg
summary:跟踪看看其源码码，源代码虽然看上去经较多，可是真正值得我们分析的却不是很多，在上面的代码就是资源管理器的初始化了，其中最重要的函数是`resourceManger`了，这个函数会针对每种特定的资源加载器进行初始化，为了缩减篇幅，在此就不列了，在这个初始化的过程中，还会读取配置文件中的这两个属性，对缓存进行初始配置...

----------

**本系列教程，为个人在淘宝实习所写，博文中所提及的WebX为淘宝的架构，大家可以忽略，当然有兴趣的，也可以自已去搜搜，淘宝的WebX目前处于开源状态**

**Velocity引擎解惑**

1、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">Velocity入门教程HelloWord程序</a>

2、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_2.html" target="_blank">Velocity入门例子自定义呈现容器</a>

3、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>


4、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html" target="_blank">Velocity入门例子创建普通的web工程</a>

5、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_5.html" target="_blank">Velocity中的单例模式以及多实例模式</a>

6、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_6.html" target="_blank">velocity初始化过程分析读取配置文件</a>

7、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_7.html" target="_blank">velocity初始化日志系统的过程分析</a>

跟踪看看其源码码，源代码虽然看上去经较多，可是真正值得我们分析的却不是很多，

下面是关键的代码

	String rm = getString(RuntimeConstants.RESOURCE_MANAGER_CLASS);  

这行代码的目的就是获取资源管理器的类名，其实也是从配置文件读取的，运行后的结果是

	rm=org.apache.velocity.runtime.resource.ResourceManagerImpl

	Object o = null;  
	try  
	{  
	   o = ClassUtils.getNewInstance( rm );  
	}

上面的代码是实例化资源管理器

	resourceManager = (ResourceManager) o;    
	resourceManager.initialize(this); 

再上面的代码就是资源管理器的初始化了。其中最重要的一个函数就是resourceManger.initialize(this)了，这个函数会针对每种特定的资源加载器进行初始化，为了缩减篇幅，在此就不列了，在这个初始化的过程中，还会读取配置文件中的resouce.manger.logwhenfound以及resource.manger.cache.class这两个属性，对缓存进行初始配置。

**initializeDirectives(初始化预指令)**

直接上源文件吧

	private void initializeDirectives()  
	 {  
		    //创建一个属性文件，用于记录
	     Properties directiveProperties = new Properties();  
	     InputStream inputStream = null;   
	     try  
	     {  
				//读取/org/apache/velocity/runtime/defaults/directive.properties这
	          //文件
	         inputStream = getClass().getResourceAsStream('/' + DEFAULT_RUNTIME_DIRECTIVES);  
				//为空时的处理
	         if (inputStream == null)  
	         {  
	             throw new VelocityException("Error loading directive.properties! " +  
	                                 "Something is very wrong if these properties " +  
	                                 "aren't being located. Either your Velocity " +  
	                                 "distribution is incomplete or your Velocity " +  
	                                 "jar file is corrupted!");  
	         }  
	  	   //加载这个配置文件，即读取到Properties对象中
	         directiveProperties.load(inputStream);  
	  
	     }  
	     catch (IOException ioe)  
	     {  
	         String msg = "Error while loading directive properties!";  
	         log.error(msg, ioe);  
	         throw new RuntimeException(msg, ioe);  
	     }  
	     finally  
	     {  
	         try  
	         {  //各种关闭操作，咱不关心
	             if (inputStream != null)  
	             {  
	                 inputStream.close();  
	             }  
	         }  
	         catch (IOException ioe)  
	         {  
	             String msg = "Cannot close directive properties!";  
	             log.error(msg, ioe);  
	             throw new RuntimeException(msg, ioe);  
	         }  
	     }  
	     /* 
	      * Grab all the values of the properties. These 
	      * are all class names for example: 
	      * 
	      * org.apache.velocity.runtime.directive.Foreach 
	      */  
			//对directiveProperties里面的元素生成其枚举集合
	     Enumeration directiveClasses = directiveProperties.elements();  
	 		//循环遍历
	     while (directiveClasses.hasMoreElements())  
	     {  
	         String directiveClass = (String) directiveClasses.nextElement();  
	         //对每一条指令均实例化一个可以处理该指令的类，并填加到指令集合中
			    loadDirective(directiveClass);  
	         log.debug("Loaded System Directive: " + directiveClass);  
	     }  
	  
	     /* 
	      *  now the user's directives 
	      */  
	  	//从配置文件velocity.properties里查看有没有用户自定义的属性文件 
	     String[] userdirective = configuration.getStringArray("userdirective");

        //如果有的话将将填加到用户自定义的属性集合中去
	     for( int i = 0; i < userdirective.length; i++)  
	     {  
	         loadDirective(userdirective[i]);  
	         if (log.isDebugEnabled())  
	         {  
	             log.debug("Loaded User Directive: " + userdirective[i]);  
	         }  
	     }  
	  
	 }  

上面的代码还是很容易理解的，就是根据配置文件中定义的指令，将相应的指令实现类加载进系统指令集合或者用户指令集合中去。

