Date: 2013-11-18
Title: 被人误解的SIZEOF
Category: 编程语言
Tags: C++
Slug: sizeof
Img:pics/c++.jpg
summary:sizeof是一个函数吗?sizeof与strlen究竟有什么区别?sizeof(int)(*p)的值是多少?有多少程序员去认真的分析过sizeof究竟是什么东西，有多少程序员知道sizeof在跨平台方面的重要作用，有多少程序员知道它的具体用法，本文分析了sizeof是个什么东东。

----------

sizeof是一个函数吗?

sizeof与strlen的区别?

sizeof(int)(*p)的值是多少?

	int a[10];
	sizeof(a);//是多少?
	sizeof(a[10]);//是多少？
	void f(int a[10])
	{
     cout<<sizeof(a)<<endl;//值是多少
	}
1:对于第一个问题，sizeof 不是一个函数，而是一个语言内置的关键字，不信你试试sizeof 4与sizeof(int),打印结果均是4，如果是函数，肯定要加上括号，即然没加括号，那么sizeof是啥呢:),如果还不信，你可以找任何一本C++/C程序语言书查查，sizeof是32个关键字中的一个，如果没有，你就换本书吧:)

即然是关键字为什么又要加括号呢？你可以试一下sizeof int 与`sizeof(int)`,第一个会编译通不过，而第二个确能编译通过，想想C/C++语言的规定，int前只能加signed.unsigned,auto,const,volative,用来修饰变量的存储方式，可没有提到前面可以加sizeof呦，如果前面加sizeof表示是什么存储方式呢:)

2:sizeof是关键字，strlen是一个标准C语言库函数，用来求取字符串的长度，`char *str="abacd"`,`sizeof str`与`strlen（str)`，编译一下，看看结果就知道了:),一个结果是4,一个结果是5，结果为4是因为一个指针占4字节，结果为5是因为串长abacd刚好5个字符，不作解释

3:`sizeof(int)(*p)`的值是多少?这个其借助1，已经分析的很详细了，其实就是取*p的值，对其转化成int类型的数据，再测量譔数据占的内存字节数，显然一个int型数据占4个字节

	int a[10];
	//下面的结果是多少?
	sizeof(a)

测量结果是多少呢？这个结果是40，sizeof在此处测量的是一个数组的大小

	int a[10];
	sizeof(a[10])是多少?

细心的人会发现a[10]已经越界访问了，此处使用sizeof并不会报错，因为越界错误是运行时异常，编译器不作检查，此时a[10]编译器认为就是数组里的一个整形变量，结果当然也是4

	void f(int a[10])
	{
	cout<<sizeof(a)<<endl;//值是多少?
	}

上面这个输出的值是多少呢？你可以写个程序试一下，结果是4，为什么呢，是因为C/C++语言规定函数无法以数组作为参数或者返回值，上面的函数在实际的编译过程中会被转化成

	void f(int *a)
	{
	 cout<<sizeof(a)<<endl;//值是多少?
	}

因为a是一个指向整形的指针，结果为4也是很显然的