Date: 2014-03-17
Title: Java语言的反射机制分析
Category: 编程语言
Tags: Java分析
Slug: reflection
Img:pics/java.jpg
summary:`Java`语言的反射机制就是在运行时对于任意一个类，都能够通过反射机制知道这个类的所有属性与方法，这种动态获取类的信息以及通过动态获取类的信息构造类对象并调用对象方法的功能 称为`Java`语言的反射机制，根据如上描述`Java`语言反射机制提供了以下三个功能，运行时获取对象所属的类别信息，运行时获取类的成员变量与方法...

----------
Java语言的反射机制就是在运行时对于任意一个类，都能够通过反射机制知道这个类的所有属性与方法，这种动态获取类的信息以及通过动态获取类的信息构造类对象并调用对象方法的功能 称为Java语言的反射机制。
根据如上描述Java语言反射机制提供了以下三个功能：

1:运行时获取对象所属的类别信息

2:运行时获取类的成员变量与方法

3:运行时构造一个类的对象

例子：一个简单的JavaBean，添加了一个构造函数

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection.jpg" alt="烟雨林博客"/>
</a>

上面的代码没有什么好说的，就是设置了三个私有成员变量，然后通过`Eclise`的代码生成工具生成了三个成员变量的Setter/Getter方法，以及一个构造函数。能说的就是注意一下`String`是一个`final`类型的常成员变量，但是`C/C++`中`string`以及MFC中`CString`好像不是~~

代码二

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection1.jpg" alt="烟雨林博客"/>
</a>

上面的代码也很简单，第一个直接通过类名，来获取相关的类的信息，无论是Java还是C++中类名都是相当于为这个语言引入了一个新的类型，可以理解为语言的内置类型，但是比内置类型要复杂，但是C++里面的反射机制估计没有Java语言强大，因为Java语言是通过加载字节码文件来运行，而字节码文件作为一种中间文件，一种支持跨平台的标准，里面含有一些信息可以标识出类的详细信息，而C++则直接将程序编译成与特定机器相关的汇编指针进而转化成机器码

如下是C++代码，可以简单的理解成Java的反射机制

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection2.jpg" alt="烟雨林博客"/>
</a>

代码三：Java连接数据库的时候经常遇到的一种形式

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection3.jpg" alt="烟雨林博客"/>
</a>

代码也很容易理解，第一行是通过详细的类名，在运行时动态注册一个类，也就是将一个类的信息放进内存，后面是各种打印，以及生成类的对象，在生成类的对象的过程中调用的是类的默认构造函数，如果单步调试运行跟踪可以发现newInstance是通过Java反射机制调用其默认的无参构造函数，代码如下：

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection4.jpg" alt="烟雨林博客"/>
</a>

代码四:通过Java反射机制获取类的各种信息

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection5.jpg" alt="烟雨林博客"/>
</a>

以上代码是要获取的类Pojo的各方面的信息

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection6.jpg" alt="烟雨林博客"/>
</a>


上面的代码是获取各种信息的过程，获取的只是一小部分信息，其实能够获取的还有挺多，例如注释anotation,父类的方法，父类的属性，父类的构造函数等等。

Java反射机制最重的要就是能够在运行的时候调构造出类对象，并调用其相应的方法，如下是一个简单的例子：


<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection7.jpg" alt="烟雨林博客"/>
</a>

上面的代码通过反射机制获得了Java里的getTestA/setTestA两个方法，并通过setAccessible改变了属性的访问权限，将属性值打印出来。

补充:
Java为什么能够实现反射机制?

Java为什么能够实现反射机制，其实上文已经隐含的表达了，关键是在由Java代码编译成字节码文件的过程中，这是一个中间阶段，在字节码文件中除了编译生成的字节码文件以外还有类的各方面信息。

如以下是Pojo字节码文件的前48字节


<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection8.jpg" alt="烟雨林博客"/>
</a>

第一行中含有编译此类的JDK版本号，如00/32换算成十进制表示的是次版本号为00，主版本号为50，其中50表示的就是使用的是JDK 6,看到这时，也就可以明白了为什么在编译类时高版本的JDK可以执行低版本编译器编译的类，而低版本的JDK却不行，问题就在于每一个类中均有一个JDK版本号，其中第一行还说明了类中常量池的数，方法数，属性数，访问标记等，第二行表示的就是类名，第三行就是父类名，父类名前的几个应该是常量池的索引号。

因此JDK编译生成的字节码文件中含有相当多的关于类中各种信息的说明，Java能够实现反射也就不足为奇了
最后是一个查看字节码文件的工具byteviewer

<a href="http://www.yanyulin.info/pages/2014/03/reflection.html">
<img src="http://www.yanyulin.info/pics/java/reflection9.jpg" alt="烟雨林博客"/>
</a>


由上图可以得出的是一个字节码文件 可以划分为五部份，第一部份是General Information也就是刚才看到的第一行，第二部分是常量池，第三部份是接口，第四部份是属性，第五部份是方法，如果看方法，你会发现一个很惊讶的问题就是Java里的构造函数在编译后均改名为init,这和C++很不同，最后就是类格式属性。

