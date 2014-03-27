Date: 2014-03-18
Title: Java字节码文件解读示例
Category: 编程语言
Tags: Java分析
Slug: bytecode
Img:pics/java.jpg
summary:`Java`为什么能够支持跨平台，其实关键就是在于其*.class字节码文件，因为*.class字节码文件有一个统一标准的规范，里面是JVM运行的时需要的相关指令,各家的JVM必须能够解释编译执行标准字节码文件，因此Java是一种跨平台语言，再想想C++/C等语言为什么不是跨平台的，就是因为其源文件经过编译后生成...

----------

`Java`为什么能够支持跨平台，其实关键就是在于其*.class字节码文件，因为*.class字节码文件有一个统一标准的规范，里面是JVM运行的时需要的相关指令,各家的JVM必须能够解释编译执行标准字节码文件，因此Java是一种跨平台语言，再想想C++/C等语言为什么不是跨平台的，就是因为其源文件经过编译后生成的就是针对特定机器的汇编代码，所以呢~

字节码文件解析

在解析之前最好下载一个工具方便查看（**Bytecode viewer**）,当然也可以不用下载，直接使用JDK自带的命令如**javap –c –s –l –verbose** (字节码文件去掉扩展名)

一个简单的程序

    public class Test {
    private static final int MAX_COUNT=1000;
    private static int count=0;
    public int bar() throws Exception{
    	if(++count>=MAX_COUNT){
    		count=0;
    		throw new Exception("count overflow");
    	}
    	return count;
    }
    }

运行工具软件查看得下图：


<a href="http://www.yanyulin.info/pages/2014/03/bytecode.html">
<img src="http://www.yanyulin.info/pics/java/bytecode1.jpg" alt="烟雨林博客"/>
</a>


看到了吧，一个字节码文件由6部份组成，先看第一部份General Information,这一部份中
说明了JDK使用的版本号`Major version=51`表示使用的是JDK 7,`Minor version=0`表示的是次版本号，不信你可以试试下面这条语句

    System.out.println(System.getProperty("java.class.version"));

下面是constant pool=35,常量池中存放着类中定义的所有常量，大致包括类名，方法名，特征符以及字符串等，`Access flag=0x0021[public]`表识该类的访问权限，This class=cp_info_#1<Test>其中cp是const pool的缩写，表示这个类的信息保存在了1号常量池中，下面讲到constant pool时再说

super class=cp_info_#3也表示同一个意思，Interface count=0表示类没有实现接口

Fields count=2说明类中定义了两个成员变量，不信你看看刚才的源文件是不是有两个变量

Methods count=3表明类中定义的方法数是3(clinit对静态变量进行赋值由JVM调用， init为类的构造函数， bar用户自定义函数)

Attribute count=1表示是类格式属性


看看常量池如下，不截图了

    [01] CONSTANT_Class_info
    	Classname:cp_info_#2<Test>

表示Classname存放在2号常量池中

    [02] CONSTANT_Utf8_info
    	Length of byte array :4
    	Length of string:4
    	String: Test

表示类名是Test,长度是4，占用4个字节

其他类似

看看方法Method里的`<init>`即构造函数

<a href="http://www.yanyulin.info/pages/2014/03/bytecode.html">
<img src="http://www.yanyulin.info/pics/java/bytecode2.jpg" alt="烟雨林博客"/>
</a>

Name的信息在常量池cp_info_#17中

<a href="http://www.yanyulin.info/pages/2014/03/bytecode.html">
<img src="http://www.yanyulin.info/pics/java/bytecode3.jpg" alt="烟雨林博客"/>
</a>

从中可以看出其定义了字节码中类的构造函数的方法名

Descriptor描述的是函数的返回类型

<a href="http://www.yanyulin.info/pages/2014/03/bytecode.html">
<img src="http://www.yanyulin.info/pics/java/bytecode4.jpg" alt="烟雨林博客"/>
</a>

描述了函数的返回类型即为`void`类型

这个Access flags就不用多说了吧，表示的是函数访问权限 

缺省构造器中的“指令是面向过程的汇编语言。`aload_0`说的是把对象的引用保存到JVM的0号局部变量，并且把它压入栈。

invokespecial #1这条命令是调用j`ava.lang.Object`中的构造（这些信息保存在1号常量项里，好处是减少字节码的长度），`return`是执行完毕退出的意思。


`Bar`函数的分析类似，其字节码文件对应的指令如下

<a href="http://www.yanyulin.info/pages/2014/03/bytecode.html">
<img src="http://www.yanyulin.info/pics/java/bytecode5.jpg" alt="烟雨林博客"/>
</a>