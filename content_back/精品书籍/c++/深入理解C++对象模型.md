Date: 2013-11-18
Title: 深度探索C++对象模型
Category: 精品书籍
Tags: C++书库
Slug: objectModel
Img:pics/book/c++objectModel.jpg
summary:《深度探索C++对象模型》重点探索"对象导向程序所支持的C++对象模型"下的程序行为,对于"对象导向性质之基础实现技术"以及"各种性质背后的隐含利益交换"提供一个清楚的认识。检验由程序变形所带来的效率冲击。提供丰富的程序范例、图片，以及对象导向观念和底层对象模型之间的效率测量。专注于C++对象导向程序设计的底层机制，包括结构式语意、暂时性对象的生成、封装、继承，以及虚拟——虚拟函数和虚拟继承。

----------
电子书PDF格式下载:<a href="http://yunpan.cn/QUK3HwIaW6tu2" target="_blank" title="《深度探索C++对象模型》">点这里</a>

第0章 导读（译者的话）

第1章 关于对象（Object Lessons）

>1.1 C++对象模型（The C++ Object Model）

>1.2 关键词所带来的差异（A Keyword Distinction）

>1.3 对象的差异（An Object Distinction）

第2章 构造函数语意学（The Semantics of constructors）

>2.1 Default Constructor的建构操作

>2.2 Copy Constructor的建构操作

>2.3 程序转换语意学（Program Transformation Semantics）

>2.4 成员们的初始化队伍（Member Initialization List）

第3章 Data语意学（The Semantics of Data）

>3.1 Data Member的绑定（The Binding of a Data Member）

>3.2 Data Member的布局（Data Member Layout）

>3.3 Data Member的存取

>3.4 “继承”与Data Member

>3.5 对象成员的效率（Object Member Efficiency）

>3.6 指向Data Members的指针（Pointer to Data Members）

第4章 Function语意学（The Semantics of Function）

>4.1 Member的各种调用方式

>4.2 Virtual Member Functions（虚拟成员函数）

>4.3 函数的效能

>4.4 指向Member Functions的指针（Pointer-to-Member Functions）

>4.5 Inline Functions

第5章 构造、解构、拷贝 语意学（Semantics of Construction，Destruction，and Copy）

>5.1 无继承情况下的对象构造

>5.2 继承体系下的对象构造

>5.3 对象复制语意学（Object Copy Semantics）

>5.4 对象的功能（Object Efficiency）

>5.5 解构语意学（Semantics of Destruction）

第6章 执行期语意学（Runting Semantics）

>6.1 对象的构造和解构（Object Construction and Destruction）

>6.2 new和delete运算符

>6.3 临时性对象（Temporary Objects）

第7章 站在对象模型的类端（On the Cusp of the Object Model）

>7.1 Template

>7.2 异常处理（Exception Handling）

>7.3 执行期类型识别（Runtime Type Identification，RTTI）

>7.4 效率有了，弹性呢？