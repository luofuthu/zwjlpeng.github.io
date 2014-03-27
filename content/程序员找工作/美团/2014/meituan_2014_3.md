Date: 2014-03-11
Title: 美团网校园招聘笔试题2014年研发类长沙
Category: 程序员找工作
Tags: 美团网笔试题
Slug: meituan_2014_C
Img:pics/meituan.jpg
summary:有ABCD四个人要在夜里过一座桥，他们通过这座桥分别需要耗时,`25`匹马赛跑，每次只能跑5匹马，最快能赛几次找出跑得最快的3匹马?赛跑不能计时，并假设每匹马的速度是恒定不变的。请给出答案并描述比赛过程,在有团购之前，大家都是现场买门票的，这个你懂的，公园的门票是5元;某天售票处开门时没有准备零钱,假设一天...

----------
**如有错误，或更加精简的方法，请留言，我会更正，以方便更多的人**

1、有ABCD四个人要在夜里过一座桥，他们通过这座桥分别需要耗时1、2、5、10分钟，现在只有一支手电，过桥时必须带有手电，并且同时最多只能两个人一起过桥。请问如何安排能够让四个人尽快都过桥。

>分析：由于A耗时最短，所以每次都安排A和另外一个人一起过桥，回来的时候A一个人回来。至于其他三个人的顺序，可以是任意的，这样总的时间是2+1+5+1+10=19.

>1、1和2先过去，时间为2

>2、1回来，时间为1 

>3、5和10过去，时间为10 

>4、2回来，时间为2 

>5、1和2再次回来，时间为2，完成。

所以总时间为：`2+1+10+2+2=17`


2、25匹马赛跑，每次只能跑5匹马，最快能赛几次找出跑得最快的3匹马?赛跑不能计时，并假设每匹马的速度是恒定不变的。请给出答案并描述比赛过程。

>详细解释见： <a href="http://blog.csdn.net/wanglongfei_hust/article/details/9797457" target="_blank">赛马问题</a>

3、在有团购之前，大家都是现场买门票的，这个你懂的，公园的门票是5元;某天售票处开门时没有准备零钱。假设一天来购票的依次有2N个人，其中有N个人有5元零钱，其它N个人只有10元面值的钱;假设每人只买一张票。请问任何人都不必为找零而等待的概率是多少?

4、有一个函数"int f(int n)"，请编写一段程序测试函数f(n)是否总数返回0，并添加必要的注视和说明。

5、用你熟悉的语言编写程序用两个栈(Stack)模拟队列(Quene)的先进先出操作，仅实现add、remove方法即可。


>清新啊描述思路;2)编写完整代码实现，编程语言不限。

详细解释见： <a href="http://www.yanyulin.info/pages/2014/03/offer.html" target="_blank">剑指offer</a>面试题7

>用两个栈实现队列

	#include <iostream>
	#include <stack>
	using namespace std;
	
	template <class T>
	class Queue
	{
	public:
		Queue()
		{
		}
		~Queue()
		{
		}
	
		void add(const T& t);
		T remove();
	private:
		stack<T> s1;
		stack<T> s2;
	};
	
	template <class T>
	void Queue<T>::add(const T& t)
	{
		s1.push(t);
	}
	
	template <class T>
	T Queue<T>::remove()
	{
		if (s2.size() <= 0)
		{
			while (s1.size() > 0)
			{
				T t = s1.top();
				s2.push(t);
				s1.pop();
			}
		}
	
		if (s2.size() == 0)
		{
			throw new exception("empty queue");
		}
	
		T t = s2.top();
		s2.pop();
	
		return t;
	
	}
	
	int main()
	{
		Queue<char> q;
	
		q.add('A');
		q.add('B');
		q.add('C');
		cout<<q.remove()<<endl;
		cout<<q.remove()<<endl;
		cout<<q.remove()<<endl;
	
		system("pause");
		return 0;
	}

6、编写函数，获取两端字符串的最长公共子串的长度，例如：
　　
	S1=GCCCTAGCCAGDE
	S2=GCGCCAGTGDE
　　
>这两个序列的最长公共子串GCCAG，也就是说返回值5。

>清闲描述思路;2)编写完整代码实现，编程语言不限。

7、(iOS开发选做)实现多线程都有哪几种方法?

8、(Android开发选做)关于Activity的生命周期，下拉statusbar时，桌面Activity会触发哪几个生命周期?系统关机时，弹出关机Dialog之后，此时，桌面Activity会触发哪几个生命周期?

9、(前端开放选做)请使用HTML和CSS完成如下布局：

<center>
<a href="http://www.yanyulin.info/pages/2014/03/meituan_2014_C.html">
<img src="http://www.yanyulin.info/pics/job/meituan0.jpg" alt="烟雨林博客"/>
</a>
</center>


10、(系统运维选做)有主机A，B，C通过`eth0`和同一个交换机相连，A的IP地址为`192.168.1.2`，子网掩码`255.255.255.0`，B的IP地址为`192.168.2.2`，子网掩码`255.255.255.0`，C的IP地址为`192.168.4.2`，子网掩码255.255.255.0。现希望A和B能够通信，A和C、B和C不能通信。
　　
假设能更改A和B的子网掩码，要如何设置A和B的子网掩码?


如果不能更改子网掩码，需要在A和B做什么设置?


A和B通信时，C是否能够通过`sniffer`截获A和B通信的报文，如果只能截获一部分报文，是哪一类报文?


C可以仅通过`sniffer`得知A和B的IP地址和MAC地址吗?如果能，如何获得?

**各位如果有更好的答案，请留言评价，方便更多的人**