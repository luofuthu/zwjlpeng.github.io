Date: 2014-03-27
Title: Velocity中对宏的初始化过程分析
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_12
Img:pics/company/taobao.jpg
summary:本篇博文是对<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html" target="_blank">Velocity入门例子创建普通的`web`工程</a>中代码的一个详细解说，分析整个`Web`应用程序的流程，在阅读本篇博文之前可以参考该篇博文，容器会把`class`给生成实例 就是把他给`new`出来,然后根据`class`内容 生成一个静态的文本文件，响应给用户,响应结束以后，这个new出来的对象 就会被容器收回...

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

8、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_8.html" target="_blank">Velocity初始化资源加载器以及预指令</a>

9、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_9.html" target="_blank">Velocity语法简明教程</a>

10、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_10.html" target="_blank">Velocity中的事件初始化以及解析池初始化</a>


11、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_11.html" target="_blank">Velocity中对宏的初始化过程分析</a>

本篇博文是对<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html" target="_blank">Velocity入门例子创建普通的web工程</a>中代码的一个详细解说，分析整个Web应用程序的流程，在阅读本篇博文之前可以参考该篇博文

**普通的JSP页面的执行流程如下所示**

在网站发布的时候`jsp`文件会被编译成`class`文件,(这里的`class`文件其实就是`servlet`)用户请求时,容器会把class给生成实例 就是把他给new出来,然后根据class内容 生成一个静态的文本文件，响应给用户,响应结束以后，这个new出来的对象 就会被容器收回 这叫http的无状态特性,当然如果启用缓存的话,这个new出来的对象会驻留在服务器，并且把他响应给下一个请求这个页面的用户，节省服务器资源和响应时间，这里我们的页面不是一个JSP页面， 而是一个VM页面，当然也就不需要JSP引擎


1：将JSP页面翻译成一个Servlet，这个Servlet是一个java文件，同时也是一个完整的java程序

2：JSP引擎调用java编译器对这个Servlet进行编译，得到可执行文件class

3：JSP引擎调用java虚拟机来解释执行class文件，生成向客户端发送的应答，然后发送给客户端

作为一个Web程序，服务器将Web程序装载进来时，最先读取的是web.xml配置文件，web.xml文件里面最关键的部分部份就是：

    1.	<servlet>  
    2.	<servlet-name>velocity</servlet-name>  
    3.	<servlet-class>com.pp.PrtInfo</servlet-class>  
    4.	 </servlet>  
    5.	 <servlet-mapping>  
    6.	<servlet-name>velocity</servlet-name>  
    7.	<url-pattern>*.vm</url-pattern>  
    8.	 </servlet-mapping>


从这个配置文件中，可以看到的是，对于所有的*.vm，都将转交给com.pp.PrtInfo,当然，我这里仅是为了简便，在Java Web程序中所有类最终结果都是一个Servlet类，可是如果你观察例子六中的代码，你可能惊奇的发现是例子六中的代码并没有doGet/doPost这样的Servlet标志性代码,可是如果你查看一下他的父类的代码，你就会发现，父类是继承自HttpServlet，显然了吧，这真是一个Servlet类，看看他的doGet与doPost方法吧，如下源代码：

    1.	public void doGet(HttpServletRequest request, HttpServletResponse response) 
    2.	throws ServletException, IOException  
    3.	{  
    4.	doRequest(request, response);  
    5.	}  
    6.	public void doPost(HttpServletRequest request, HttpServletResponse response)
    7.	throws ServletException, IOException  
    8.	{  
    9.	doRequest(request, response);  
    10.	}  
    
看到了吧，两个方法中均调用的是doRequest方法，看看doRequest方法
    
    1.	protected void doRequest(HttpServletRequest request, HttpServletResponse response)  
    2.	throws IOException  
    3.	   {  
    4.	   Context context = null;  
    5.	   try  
    6.	   {  
    7.	   // then get a context  
    8.	   context = createContext(request, response);  
    9.	  
    10.	   // call standard extension point  
    11.	   fillContext(context, request);  
    12.	  
    13.	   setContentType(request, response);  
    14.	  
    15.	   // get the template  
    16.	   Template template = handleRequest(request, response, context);  
    17.	  
    18.	   // merge the template and context into the response  
    19.	   mergeTemplate(template, context, response);  
    20.	   } catch (IOException e) {  
    21.	   error(request, response, e);  
    22.	   throw e;  
    23.	   }  
    24.	   catch (ResourceNotFoundException e)  
    25.	   {  
    26.	   manageResourceNotFound(request, response, e);  
    27.	   }  
    28.	   catch (RuntimeException e)  
    29.	   {  
    30.	   error(request, response, e);  
    31.	   throw e;  
    32.	   }  
    33.	   finally  
    34.	   {  
    35.	   requestCleanup(request, response, context);  
    36.	   }  
    37.	   }  

看到了吧，两个方法中均调用的是doRequest方法，看看doRequest方法


看到上面的代码，你在看看例子六中的`fillContext`以及`setContentType()`就大概明白了，在`fillContext`中我们将一些变量放进了context容器中，在setContentType我们设置了输出时的编码方式。`mergeTemplate`会使用Velocity引擎将context中的内容与模板进行结合，并将结果输出。
