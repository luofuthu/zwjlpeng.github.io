Date: 2014-03-15
Title: Velocity入门教程HelloWord程序
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_1
Img:pics/company/taobao.jpg
summary:`Velocity`是`Apache`公司的开源产品，是一套基于`Java`语言的模板引擎，可以很灵活的将后台数据对象与模板文件结合在一起，说的直白一点，就是允许任何人使用模板语言引用后台java代码定义的对象，界面设计人员可以和java程序开发人员同步开发一个遵循MVC架构的web站点，也就是说，页面设计人员可以...

----------

**简介**

`Velocity`是`Apache`公司的开源产品，是一套基于`Java`语言的模板引擎，可以很灵活的将后台数据对象与模板文件结合在一起，说的直白一点，就是允许任何人使用模板语言引用后台java代码定义的对象

`Velocity`应用于Web开发时，界面设计人员可以和java程序开发人员同步开发一个遵循MVC架构的web站点，也就是说，页面设计人员可以只关注页面的显示效果，而由Java程序开发人员关注业务逻辑编码

`Velocity`将 java代码从web页面中分离出来，这样为web站点的长期维护提供了便利,之所以写这篇文章，是因为在淘宝实习，淘宝的WebX框架也使用了`Velocity`

**入门例子**

`Velocity`应用于`java`工程时，创建完一个普通的java工程后，需要引入相应的jar包，才能让工程支持`Velocity`模板引擎(velocity-1.7.jar/ commons-*.jar)

如下是例子一

	VelJava工程的后台java代码`VelJava.java`
	
	//构造函数  
	public VelJava() throws IOException{  
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
	    //将模板与context中的对象结合，然后输出  
	    if(template!=null)  
	        template.merge(context, writer);  
	    //刷新缓存  
	    writer.flush();  
	    //关闭writer  
	    writer.close();  
	}  
	//VelocityContext键值对中的值  
	public ArrayList<String> getNames(){  
	    ArrayList<String> list=new ArrayList<String>();  
	    list.add("element 1");  
	    list.add("element 2");  
	    list.add("element 3");  
	    list.add("element 4");  
	    return list;  
	}

**备注**

在这个例子中，以健值对的形式将getNames()函数的返回值存放在Velocity容器中，并给其一个键值为`list`

模板文件的代码如下`test.vm`：

	##声明了一个变量  
	#set( $this = "ppTest")  
	##将变量打印出来  
	$this is great!  
	##对后台的list进行扫描，将集合中的元素一个一个的打印出来  
	#foreach( $name in $list )  
	$name is showed!  
	#end  
	##设置一个判断条件，将将判断条件赋值为真  
	#set( $condition = true)  
	##判断条件为真，执行  
	#if ($condition)  
	The condition is true!  
	##判断条件为假时，执行  
	#else  
	The condition is false!  
	#end 

**备注**

其中的##表示的是注释

`#`set类表示的是预处理指令

$变量名表示声明的是一个变量


上面的代码注释的已经很清楚了，如果只是应用，不需要了解更多细节的话，上面的代码已经够了，从上面的代码中可以看出`Velocity`的一个好处就是模板文件与后台文件可以同步开发，只要约定好一些共有的变量定义即可，在模板输出时，由模板引擎进行变量的替换,替换之后再进行相应的输出


第二个例子：`Velocity`动态创建模板并渲染(Java工程)

例子二，演示了在Java工程将模板渲染后以指定的编码方式`GBK`输出，同时也演示了动态创建模板，然后进行渲染

	public static void main(String[] args) {  
	    //初始化Velocity引擎  
	    Velocity.init();  
	    //获取一个VelocityContext对象  
	    VelocityContext context=new VelocityContext();  
	    //向此对象容器中加入相应的键值对  
	    context.put("name", "Velocity");  
	    context.put("project", "Jakarta");  
	    //StringWriter底层其实就是一个StringBuffer  
	    StringWriter w=new StringWriter();  
	    //将test2.vm与context进行合并，生成的最终代码写入StringWriter的buf中  
	    Velocity.mergeTemplate("test2.vm", "GBK",context,w);  
	    //将其在控制台上打印出来  
	    System.out.println("模板:"+w);  
	    //动态创建模板  
	    String s="正在使用 $project $name 渲染模板";  
	    w=new StringWriter();  
	    /* 
	     *context：对输入的字符串进行渲染 
	     *w:渲染后的结果输出的地方 
	     *mystring:发生错误时，被用来作为错误文件的名字 
	     *s:包括VTL语言的输入字符串 
	    */   
	    Velocity.evaluate(context, w, "mystring", s);  
	    //将结果进行输出来  
	    System.out.println(w);  
	}  

例子二的模板文件`test2.vm`如下：

	Hello 来自于 $name 在 $project 工程里. 


例子二与例子一极为相似，例子二的模板只不过是在代码中创建的，例子一中的模板是直接引用外部的test.vm文件，从上面的代码中可以揣测一下Velocity是如何工作的，大概是这样的

1、将外部的vm文件读入内存

2、Velocity模板引擎对vm文件进行解析


3、解析之后对模板文件中的变量进行替换，并执行vm中的相应判断逻辑

4、执行完后，整个页面的渲染结果就知道了，再直接输出即可


从这里可以看出只要前后台代码的开发人员能够约定相同的变量，则前后台的开发完全可以并行执行