Date: 2014-03-18
Title: Velocity入门例子创建普通的web工程
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_4
Img:pics/company/taobao.jpg
summary:**本系列教程，为个人在淘宝实习所写，博文中所提及的WebX为淘宝的架构，大家可以忽略，当然有兴趣的，也可以自已去搜搜，淘宝的WebX目前处于开源状态**，例子是一个`Velocity`在Web上应用的例子，例子中的Web程序没有采用任何的框架，是一个纯粹的Java Web工程，首先看看效果吧，然后再是关键代码，等到后面再分...

----------

**本系列教程，为个人在淘宝实习所写，博文中所提及的WebX为淘宝的架构，大家可以忽略，当然有兴趣的，也可以自已去搜搜，淘宝的WebX目前处于开源状态**

本篇博文仅随前三篇博文而来

<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">
Velocity入门教程HelloWord程序
</a>


<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_2.html" target="_blank">
Velocity入门例子自定义呈现容器
</a>

<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">
Velocity入门例子事件监听机制
</a>


本篇博文主要介绍velocity中的事件处理机制

例子是一个Velocity在Web上应用的例子，例子中的Web程序没有采用任何的框架，是一个纯粹的Java Web工程。

在开始这项工作之前，还需要从官网上下载velocity-tools-2.0

官网地址是<a href="http://velocity.apache.org/download.cgi" target="_blank" >http://velocity.apache.org/download.cgi</a>

首先看看效果吧，然后再是关键代码，等到后面再分析其中涉及的原理部分

<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html">
<img src="http://www.yanyulin.info/pics/taobao/velocity4_1.jpg"  width="100%" alt="烟雨林博客"/>
</a>

呈现的结果很显然，模拟了后台数据库的行为，用于存储数据，同时实现了分页机制，正如标题所说的，此工程非WebX工程，因此在使用Velocity建立Web工程时需要导入相应的Jar包，需要导入的详细Jar包列表如下:

<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html">
<img src="http://www.yanyulin.info/pics/taobao/velocity4_2.jpg" alt="烟雨林博客"/>
</a>

然后创建Web工程，其中几个得要的源文件如下源码所示

第一个比较重要的源码文件就是web.xml.因为这是服务器加载Web程序时首先读取的，是Web应用程序最基本的配置文件

Web.xml

    <?xml version="1.0" encoding="UTF-8"?>  
    <web-app version="2.5"   
        xmlns="http://java.sun.com/xml/ns/javaee"   
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee   
        http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">  
      <servlet>  
        <servlet-name>velocity</servlet-name>  
        <servlet-class>com.pp.PrtInfo</servlet-class>  
      </servlet>  
      <servlet-mapping>  
        <servlet-name>velocity</servlet-name>  
        <url-pattern>*.vm</url-pattern>  
      </servlet-mapping>  
      <display-name></display-name>   
      <welcome-file-list>  
            <welcome-file>index.vm</welcome-file>  
      </welcome-file-list>  
    </web-app>  

从这个xml文件中很容易看出来的是对于所有的`*.vm`的请求都将由`com.pp.PrtInfo`这个类进行处理，PrtInfo类是一个`Servlet`类，下面是其源代码

PrtInfo.java

	package com.pp;  
	import java.util.ArrayList;  
	import javax.servlet.http.HttpServletRequest;  
	import javax.servlet.http.HttpServletResponse;  
	  
	import org.apache.velocity.Template;  
	import org.apache.velocity.context.Context;  
	import org.apache.velocity.tools.view.VelocityViewServlet;  
	  
	public class PrtInfo extends VelocityViewServlet {  
	    private static final long serialVersionUID = 1L;  
	  
	    @Override  
	    protected void fillContext(Context context, HttpServletRequest request) {  
	        super.fillContext(context, request);  
	        ArrayList<MallDb> db=new ArrayList<MallDb>();  
	        for(int i=0;i<100;i++)  
	        {  
	            MallDb tmp=new MallDb("追日"+(i+1),"研发工程师","TEL:12581");  
	            db.add(tmp);  
	        }  
	        String page=request.getParameter("page");  
	        int num=1;  
	        if(page!=null)  
	            num=Integer.parseInt(page);  
	        context.put("initialValue", (num-1)*10);  
	        context.put("page", Math.round(db.size()/10));  
	        context.put("db", db.subList((num-1)*10, 10*(num)));  
	    }  
	  
	    @Override  
	    protected Template handleRequest(HttpServletRequest request,  
	            HttpServletResponse response, Context ctx) {  
	        // TODO Auto-generated method stub  
	        response.setCharacterEncoding("GBK");  
	        response.setContentType("text/html");  
	        return super.handleRequest(request, response, ctx);  
	    }  
	}

这个类里面，你并没有发现`doGet`与`doPost`请求，难道没有吗？其实不是，后面再进行分析，注意的是为了防止页面中的中文乱码，我们对请求返回的数据进行了编码的设置，这样就可以解决乱码的问题，从这个代码中可以发现是的代码中使用了MallDb这个类，下面是这个类的详细代码，其实就是一个简单的`JavaBean`

MallDb.java

	package com.pp;  
	  
	public class MallDb {  
	    private String name;  
	    private String job;  
	    private String Tel;  
	    public String getName() {  
	        return name;  
	    }  
	    public void setName(String name) {  
	        this.name = name;  
	    }  
	    public String getJob() {  
	        return job;  
	    }  
	    public MallDb(String name, String job, String tel) {  
	        super();  
	        this.name = name;  
	        this.job = job;  
	        Tel = tel;  
	    }  
	    public void setJob(String job) {  
	        this.job = job;  
	    }  
	    public String getTel() {  
	        return Tel;  
	    }  
	    public void setTel(String tel) {  
	        Tel = tel;  
	    }  
	}  

上这的这个`MallDb.java`没有什么好讲的，一看就懂