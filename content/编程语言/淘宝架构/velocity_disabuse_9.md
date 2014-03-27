Date: 2014-03-23
Title: Velocity语法简明教程
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_9
Img:pics/company/taobao.jpg
summary:接触过`Linux Shell`脚本的，看起来也不陌生，很容易理解，详细如下，写过的对这些应该很熟悉，`{}`用来在一个很长的字符串中区分变量，`!`用来在变量值为空时，避免在页面上输出，`\`这个代表后面的是一个转义字符，照常输出，””括起来的东西，如果里面含有可以被veloctiy解释的照常解释，’’括起来的东...

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

接触过Linux Shell脚本的，看起来也不陌生，很容易理解，详细如下：

**`#`开头的脚本语句**

`#`开头的脚本语句如#set、#if 、#else、#end、#foreach、#end、#iinclude、#parse、#macro等。


例子：

	#foreach($tmp in $objs)  
	$tmp  
	#endif

`$`标识的变量

和JS差不多吧，是一种弱类型，变量不需要类型，也不需要事先声明，想到了就可以用，不过要注意一下的就是编程规范。

	$i、$msg、$TagUtil.options(...)  

**{}/!/\/””/’’特殊用法**

写过Linux Shell的对这些应该很熟悉，{}用来在一个很长的字符串中区分变量，!用来在变量值为空时，避免在页面上输出，\这个代表后面的是一个转义字符，照常输出，””括起来的东西，如果里面含有可以被veloctiy解释的照常解释，’’括起来的东东不再被velocity进行解释，而是直接输出。

    $some=”test”  
    $someone ##在页面上直接输出$someone  
    ${some}one ##在页面上输出testone  
    $test ##在页面上输出$test  
    $!test ##在页面上什么都不输出，因为test=null  
      
    \$some ##在页面上输出$some,$被转义了  
    “$some” ##在页面上输出test  
    ‘$some’ ##在页面上输出$some  

**逻辑运算符:== && || !**

这个没什么好讲的，学过任何一种语言或者脚本都有，看看就明白了。

**循环计数器**

Velocity循环计数数有一个比较特别的地方就是其循环计数变量不是从0开始，而是从1开始的，这一点从其配置文件中也可以很容易的看出来，配置文件如下：
	
	# Default name of the loop counter  
	# variable reference.  
	directive.foreach.counter.name = velocityCount  
	# Default starting value of the loop  
	# counter variable reference.  
	directive.foreach.counter.initial.value = 1 

从这个配置文件中可以看到的是循环变量的名字是velocityCount,这个名字如果你细看了例子六中的代码，应该也出现了。

**Velocity中的宏**

Velocity中的宏可以分为有参数与无参数两种情况，说白了，其实无参数也是有参数的一种特殊情况，学过C/C++都应该知道#define,把它理解成#define,就行了，如下是例子，一个是有参数的宏，一个是无参数的宏。
无参数的宏

    #macro( d )  
    <tr><td></td></tr>  
    #end  
    调用   
    #d()  


**有参数的宏**

	#macro( tablerows $color $somelist )  
	#foreach( $something in $somelist )  
	<tr><td bgcolor=$color>$something</td></tr>  
	#end  
	#end 

上面是带两个参数的宏。

**范围操作符**

也是一看就懂的，如果你学过Python,这个操作符代表的是一个集合，这里也是一个意思，代码如下：

	#foreach( $foo in [1..5] )  
	#foo  
	#end

**总结**

有太多的东西想分析得更加详细，但是总感觉时间有限，精力有限，无法渗透出更深层的东西，斗转星移，日月更迭，不经意间21天(1814400秒)的光阴已悄然无声的划过，没学过Spring,无法从最深层次去了解WebX,实在是一种悲哀，但我一直在努力，努力的看Spring,不是嘛,培根说，态度决定一切，生活本来就应该如此，那个谁说源码面前，了无秘密，我拿这句话与大家共勉