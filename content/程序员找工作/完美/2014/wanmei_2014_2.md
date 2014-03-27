Date: 2014-03-21
Title: 2014年完美世界校招笔试题技术类
Category: 程序员找工作
Tags: 完美笔试题
Slug: wanmei_2014_b
Img:pics/company/wanmei.jpg
summary:下面代码输出是什么？顺序搜索和二分搜索代表了搜索时间和预处理时间之间的折中，处理一个`n`元表格时，需要执行多少次二分搜索才能弥补对表进行排序所消耗的预处理时间？到商店里买`200`的商品返还`100`优惠券(可以在本商店代表现金),请问实际上折扣是多少?若二叉树中有`n`个度为2的结点，则该二叉树中的叶子结点为...

----------


一 选择题

4、下面代码输出是什么？

	void foo(void)
	{
		unsigned int a=6;
		int b=-20;
		(a+b>6)?puts(">6"):puts("<=6");
	}

5、顺序搜索和二分搜索代表了搜索时间和预处理时间之间的折中，处理一个n元表格时，需要执行多少次二分搜索才能弥补对表进行排序所消耗的预处理时间？（）

6、到商店里买200的商品返还100优惠券(可以在本商店代表现金),请问实际上折扣是多少?()

7、若二叉树中有n个度为2的结点，则该二叉树中的叶子结点为()

8、写出至少三种常用的设计模式，并简单介绍其用法或目的：

    1）
    
    2）
    
    3）
    
    4）

9、写出判断float f是否等于0的if语句（）


10、编译时的多态性通过`(      )`函数实现

11、

	class A{
	public:
		A(){}
		virtual ~A()
		char m_x;
	};
	A a;

`sizeof（a)`的值是`(   )`


图形学部分(引擎和客户端面选做)

1、图形学中，标准光照模型有`（  ）、（  ）、（  ）、（  ）`四个光照分量组成 


2、将向量`v=(4,3,-1)`,沿向量`n=(sin45,cos45,0)`,分解为平行和垂直于n的分量


3、`D3D9 Pixel Shader 2.0 shader` 最多支持多少条`(  )`算数指令


4、请写出D3D9的四种纹理寻址模式`( )、（ ）、（ ）、 （ ）`

5、请写出一个4*4矩阵用于旋转变换，此矩阵可以表示绕Y轴正向旋转a度

6、请简单描述一下材质，在游戏中，是如何表示材质的，请用C++定义一个材质结构，并描述出各成员的意义


7、主角的某个技能攻击范围是扇形的，请写代码实现检测施技能是否攻击到NPC


假设已知

1)2D情形

2）主角位置c

3）扇形半径

4）技能方向u

5）扇形角度

6）NPC位置

请尽可能高效


8、请用自已的语言翻译如下这段话?

    Frustum culling is a basic technique that every serious 3d engine is doing. 
	In its simplest form,all objects of the scene are tested for intersection 
	with the view frustum pyramid,this test can be conservative which means 
	that it is acceptable to have some objects being reported visible even 
	if they are not , this allows optimizations like acceptable to have some 
	objects by more coarse bounding primitives, We use AABB's(axis aligned 
	bounded boxes) and  OBB's(oriented bounding boxes) when we test against 
	the frustum pyramid.The test is done hierarchically which means first 
	some coarse enclosing objects(e.g. a terrain sector) are tested for visibility 
	while the testing is recursively refined down to the draw call level. 
	Frustum culling is implemented in the 3D engine as it is hardware 
	independent and the relevant structures are stored there.




**各位如果有更好的答案，请留言评价，方便更多的人**