Date: 2013-11-18
Title: Assert(断言)实现机制剖析
Category: 编程语言
Tags: C++学习
Slug: assert
Img:pics/cplus.jpg
summary:断言(assert)的作用是用来判断程序运行的正确性，确保程序运行的行为与我们理解的一致。其调用形式为assert(logic expression),如果逻辑表达式为假，则调用abort()终止程序的运行，断言是程序高手经常使用的一种调试程序的方式，在调试程序时，在需要观察的点设置断言，在发布程序时，通过预编译宏指令将断言去掉，提高程序的开发效率，本文详细分析了断言的实现机制。

----------
断言(assert)的作用是用来判断程序运行的正确性，确保程序运行的行为与我们理解的一致。其调用形式为assert(logic expression),如果逻辑表达式为假，则调用abort()终止程序的运行。

查看MSDN帮助文档，可以得到assert的解释信息如下：
	
	The ANSI assert macro is typically used to identify logic errors during program development, 
	by implementing the expression argument to evaluate to false only when the program is 
	operating incorrectly. After debugging is complete, assertion checking can be turned off 
	without modifying the source file by defining the identifier NDEBUG. NDEBUG can be defined 
	with a /D command-line option or with a #define directive. If NDEBUG is defined with #define, 
	the directive must appear before ASSERT.H is included.
翻译过来大概意思就是assert是通过判断其参数的真假来标识程序的逻辑错误，调试结束后可以通过定义NDEBUG来关闭assert断言。

查看include/assert.h头文件可以得到assert相关的宏写义如下：

	#ifdef  NDEBUG
	#define assert(exp)     ((void)0)
	#else
	#ifdef  __cplusplus
	extern "C" {
	#endif
	_CRTIMP void __cdecl _assert(void *, void *, unsigned);
	#ifdef  __cplusplus
	}
	#endif
	#define assert(exp) (void)( (exp) || (_assert(#exp, __FILE__, __LINE__), 0) )
	#endif  /* NDEBUG */
解释：

	#ifdef NDEBUG 
	//当调试完成后，如果定义了NDEBUG,关闭断言，优化生成的代码
	#define assert(_Expression)  ((void)0)
接下来的代码意思是定义如下函数（此函数用于打印出出错信息）：
	
	_wassert(_In_z_ const wchar_t * _Message,
			 _In_z_ const wchar_t *_File,
			 _In_ unsigned _Line);
有兴趣的可以在assert.c中看到其实现，函数先要把错误的报告模式以及程序的类型(控制台程序还是GUI程序)决定assert是向标准错误输出打印还是以消息框形式出现，最后调用了abort（）函数来终止程序的运行。 对于extern “C” 有时间再解释，好了，到最后，终于看到了assert的宏定义了

	#define assert(_Expression) 
	(void)( (!!(_Expression)) || (_wassert(_CRT_WIDE(#_Expression), 
										   _CRT_WIDE(__FILE__), 
										   __LINE__),
										   0) 
		  )
asset断言后返回的结果始终是void(1)/void(0),原因就在于逗号表达式。
Assert断言在程序的作用

Assert的例子：

	#include<iostream>
	#include<assert.h>
	using namespace std;
	void main()
	{
	int tmp=0;
	assert(tmp==1)
	printf("%d\n",tmp);
	}
解释：因为tmp=0,tmp==1为false,故程序运行的时候传给assert宏的参数为false,因此调用的结果是先向stderr打印一条出错信息，然后通过调用 abort 来终止程序运行。如果改成tmp=1,则程序完全正常运行。 如里在程序中想关闭assert宏断言，可以如下defnie NDEBUG

	#include<iostream>
	#define NDEBUG
	#include<assert.h>
	using namespace std;
	void main()
	{
	int tmp=0;
	assert(tmp==1)
	printf("%d\n",tmp);
	}

你会发现即出tmp=0,也不会再出现断言信息，解释请看顶部

作用：

 1. 断言可以用来检查传给函数参数的合法性
 2. 一个断言一般只用来检查一个条件，便于分析程序
 3. 断言前后最好空一格[编程风格的问题，按你自已的喜好，适合自已就最好]
 4. 断言只是用来检查程序的逻辑正确性，不能代替条件替换
 5. 断言比printf语句这种形式的打印好使
 6. 断言参数可以是函数调用,但是函数返回值要是真假,如assert(sort()),解释看上面源码分析

