Date: 2014-03-16
Title: Java中Annotation注解机制实现分析
Category: 编程语言
Tags: Java分析
Slug: annotation
Img:pics/java.jpg
summary:Java中的`Annotation`很常见，只是时常被人忽略而已，因为如果不和Java反射机制混合使用时，代码的第一行说明了该注解是用来修饰方法的，代码的第二行是用来说明注解只出现在源代码中，即注解在代码编译后的字节码文件以及运行时是不会出现的，所以呢，你去掉该注解是不会影响程序的运行，但不是所有的注解都可以去掉...

----------
Java中的Annotation很常见，只是时常被人忽略而已，因为如果不和Java反射机制混合使用时，`Annotation`注解估计也只能被用来起着注解说明的用途了，以下就是Java中一个典型的`Annotation`注解

<a href="http://www.yanyulin.info/pages/2014/03/annotation.html">
<img src="http://www.yanyulin.info/pics/java/annotation_1.jpg" alt="烟雨林博客"/>
</a>

红色方框中的@Override，是不是见过:),只是经常被忽略而已，去掉也没大影响，是的，真的没什么影响，如果你跟踪@Override注解，你会发现如下代码：

<a href="http://www.yanyulin.info/pages/2014/03/annotation.html">
<img src="http://www.yanyulin.info/pics/java/annotation_2.jpg" alt="烟雨林博客"/>
</a>

代码的第一行说明了该注解是用来修饰方法的，代码的第二行是用来说明注解只出现在源代码中，即注解在代码编译后的字节码文件以及运行时是不会出现的，所以呢，你去掉该注解是不会影响程序的运行，但不是所有的注解都可以去掉，有些注解去掉了，就要影响程序的运行了，因为注解已经被编译进字节码文件中，代码在运行的过程中会通过反射机制从注解中获取一 些相关的信息，最典型的莫过于淘宝的WebX框架，随处可见这样的使用，如下代码：

<a href="http://www.yanyulin.info/pages/2014/03/annotation.html">
<img src="http://www.yanyulin.info/pics/java/annotation_3.jpg" alt="烟雨林博客"/>
</a>

这里的`@FormGroup`就不能去掉，如果跟踪可以发现注解的是这样说明的

<a href="http://www.yanyulin.info/pages/2014/03/annotation.html">
<img src="http://www.yanyulin.info/pics/java/annotation_4.jpg" alt="烟雨林博客"/>
</a>

代码的第一行说明了注解会出现在运行时，第二行则说明了该注解是用来修饰方法参数的,所以注解去掉后，程序将无法运行，因为WebX框架将会通过Java反射机制获取注解参数初始化simple。

`Annotation详解`：

`Annotation `提供了一条与程序元素关联任何信息或者任何元数据的途径，从某些方面看，`Annotation`就像修饰符一样被使用，并应用于包/类型/构造方法/方法/成员变量/参数/本地变量的声明中,这些信息被存储在
Annotation的“name=value”结构对中。

样例解释(此代码来源于`WebX框架`中的`FormGroup.java`)：

<a href="http://www.yanyulin.info/pages/2014/03/annotation.html">
<img src="http://www.yanyulin.info/pics/java/annotation_5.jpg" alt="烟雨林博客"/>
</a>

上面的代码就是图一中的@FromGroup的实现，代码中的第一行表示注解将会出现在运行时，这里可以说明一下，注解出现的三个时期，CLASS/SOURCE/RUNTIME,其中CLASS说明注解将会出现在字节码文件中，SOURCE表示注解将会出现在源代码文件中，RUNTIME表示注解将会出现在运行期，备注：出现在字节码文件中的注解，在加载进JVM时不一定会出现，取决于注解的设置，在没有设定RetentionPolicy时，系统默认的是CLASS。

其次ElementType是用来指定`Annotation`类型可以用在哪一些元素上的，包括TYPE（类型），METHOD（方法），`FIELD（字段）`，`PARAMETER（参数）`等。其中TYPE是指可以用在Class,Interface等类型上。
最后就是注解里的属性说明了，看起来有点像函数,个人觉的看着不爽，这里有四个属性，每个属性均有一个默认的值，其中应该注意的就是第一个参数value,例如注解写成这种形式时@FormGroup(“simple”)就表示对注解中的 value赋值为simple,其他的取默认值。

仿照WebX里的`@FormGromp`自已设计一个参数注解，可以节省代码。

本例子是基于Java工程，而不是淘宝的WebX工程,实现参数注解

注解FormGroup.java文件

	package com.pp;
	import java.lang.annotation.ElementType;
	import java.lang.annotation.Retention;
	import java.lang.annotation.RetentionPolicy;
	import java.lang.annotation.Target;
	@Retention(RetentionPolicy.RUNTIME)
	@Target({ ElementType.PARAMETER })
	public @interface FormGroup {
		//value是默认值，适用于这种形式@FormGroup("simple")
	    String value() default "";
	    String name() default "";
	    String instanceKey() default "";
	    boolean skipIfInvalid() default true;
	}


一个简单的JavaBean文件SimpleObject.java

	package com.pp;
	
	public class SimpleObject {
	private String name;
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	}

使用注解的类Action.java,主要是模拟WebX框架的Action机制

	package com.pp;
	public class Action {
	//使用参数注解的方法
	public void printfUser(@FormGroup("pp") SimpleObject so){
		System.out.println(so.getName());
	}
	}

最后一个InvokeMain.java通过Java反射机制调用printfUser函数
	
	package com.pp;
	import java.lang.annotation.Annotation;
	import java.lang.reflect.Method;
	public class InvokeMain {
	public void refInvoke()
	{
		try {
			//利用Java反射机制获取Action里的方法说明
			Method mtd=Action.class.getDeclaredMethod("printfUser", SimpleObject.class);
			//利用反射获取相关的参数注解
			Annotation [][]ant=mtd.getParameterAnnotations();
			//将参数注解转换成特定的注解类型
			FormGroup tmp=(FormGroup)ant[0][0];
			//构造一个JavaBean对象
			SimpleObject so=new SimpleObject();
			//对对象设置值 
			so.setName(tmp.value());
			//调用对象里的方法
			mtd.invoke(new Action(), so);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public static void main(String[] args) {
		new InvokeMain().refInvoke();
	}
	}

好了，终于完了，不是吗,这里的过程其实与`WebX`框架的流程是一样的，哦，其实是我认为是一样的，WebX框架在接受到一个请求后，在页面显示之前，如图一所示，@FormGroup中的simple代表的是表单，在提交到相应的Action处理之前，中间会有一个反射机制的调用，反射机制中会从参数注解获取表单的名称，根据表单的名称进而从表单中获得用户提交的参数，即各种request.getParameter的调用，然后创建一个对象`SimpleObject simple`,并用获取的参数对simple进行赋值，然后通过反射机制调用`SimpleAction`里的`doGreeting`,看看我们上面的代码`Method.invoke()`

看了好久，也没找到WebX实现从注解中获取表单参数的代码，只找到了下面这几行关键代码，有找到的可以告诉我一下


	public Object invoke(Object obj, Object[] args) throws InvocationTargetException {
	        return fc.invoke(index, obj, args);
	}

从这里我们可以看到无论例子中还是WebX中注解的确是个好东西，可以节省代码的编写，将代码中共同的部分抽取出来，使得程序可以更加关注业务处理方面的内容，这也符合Spring中面向切面编程的要求。


如果你是一个`C/C++`爱好者，像我一样，很抱谦，C++里真的没有注解Anotaton这一说，也没有反射这一说，如果说C++实现了反射(用typeid)我想作用也是很局限的，仅能判写出运行时类的类型，而且还是建立在虚基类或者虚函数的基础上，只要在这两个情况下，C++里的内存对象布局里虚函数表中才会有一项指明类的类别，这样运行时才能判断出来，如果没有虚函数虚基类这个词，那么你使用typeid获取的类的类型信息，均是在编译时期都已经确定好的，而不是运行期!
