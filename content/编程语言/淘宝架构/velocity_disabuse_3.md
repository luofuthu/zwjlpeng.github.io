Date: 2014-03-17
Title: Velocity入门例子事件监听机制
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_3
Img:pics/company/taobao.jpg
summary:本篇博文仅随前两篇博文而来<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">Velocity入门教程HelloWord程序</a>,<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_2.html" target="_blank">Velocity入门例子自定义呈现容器</a>，本篇博文主要介绍`Velocity`中的事件处理机制，例子中是一个事件处理样例，在模板中对后台Java对象的引用被渲染之前，先要经过注册的事件处理器的处理，程序中采用的是动态创建模板...

----------

本篇博文仅随前两篇博文而来

<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">
Velocity入门教程HelloWord程序
</a>


<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_2.html" target="_blank">
Velocity入门例子自定义呈现容器
</a>

本篇博文主要介绍velocity中的事件处理机制

例子中是一个事件处理样例，在模板中对后台Java对象的引用被渲染之前，先要经过注册的事件处理器的处理

	public class EventExample implements ReferenceInsertionEventHandler         {  
	    public static void main( String args[] )  
	    {  
	        new EventExample();  
	    }  
	    public EventExample()  
	    {  
	        Velocity.init();  
	        VelocityContext context = new VelocityContext();  
	        context.put("name", "Velocity");  
	        EventCartridge ec = new EventCartridge();  
	        //注册事件处理器  
	        ec.addEventHandler(this);  
	        //将注册的事件处理器与context容器进行绑定  
	        ec.attachToContext( context );  
	        try  
	        {  
	            System.out.println("");  
	            System.out.println("Velocity事件处理样例");  
	            System.out.println("============================");  
	            System.out.println("");  
	            String s = "打印name:$name.";  
	            StringWriter w = new StringWriter();  
	            Velocity.evaluate( context, w, "mystring", s );  
	            System.out.println("渲染结果 : ");  
	            System.out.println("   " +  w.toString());  
	            System.out.println("");  
	            s = "模板文件 中引用后台未定义的对象$floobie , $nullvalue";  
	            w = new StringWriter();  
	            Velocity.evaluate( context, w, "mystring", s );  
	            System.out.println("空引用测试: ");  
	            System.out.println("   " + w.toString());  
	        }  
	        catch( Exception e )  
	        {  
	            System.out.println("Exception : " + e );  
	        }  
	    }  
	    //模板渲染时在将后台对象插入模板引用之前调用  
	    public Object referenceInsert( String reference, Object value  ){  
	        String s = null;  
	        if( value != null ){  
	            s = "渲染之前 " + value.toString() + "渲染完成";  
	        }  
	        else{  
	            if ( reference.equals("floobie") ){  
	                s = "<no floobie value>";  
	            }  
	        }  
	    //将value提交给模板中引用value的地方使用  
	        return s;  
	    }  
	}   

**备注**

1、程序中采用的是动态创建模板，动态创建模板可以参考Velocity入门教程之HelloWorld,动态创建的模板为"打印name:$name."，其中$name就是需要使用Velocity来渲染的对象

2、在创建动态模板`"打印name:$name."`之前已经向容器中放入了键值为name的键值对，因此模板中的`$name`即可以从后台中取出键为name的值进行渲染


3、同样的道理，`"模板文件 中引用后台未定义的对象$floobie , $nullvalue"`也是一个动态创建的模板，但此模板中的参数floobie在context不存存以floobie为键的键值对，因此在渲染时$floobie被渲染为空

4、Velocity中为用户提供了各种事件，其中`referenceInsert`就表示在对模板中的引用对象进行渲染之前可以由程序员自定义想要的操作

