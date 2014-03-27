Date: 2013-06-11
Title: 2013年谷歌校招笔试(一)
Category: 程序员找工作
Tags: 谷歌笔试题
Slug: google_2013_1
Img:pics/google.jpg
summary:使用C语言将一个1G字节的数组从头到尾全部设置为’A’,在一台典型的当代PC上，需要花费的CPU时间的数量级最接近;在某些极端要求性能的场合，我们需要对程序进行优化，关天优化，以下说法正确的是;对如下C语言程序在普通的X86PC上运行输出正确的是;方程X1+X2+X3+X4=30,有多少满足的整数解。

----------
一：单选题

1：使用C语言将一个1G字节的数组从头到尾全部设置为’A’,在一台典型的当代PC上，需要花费的CPU时间的数量级最接近：(`B`)

A 0.001秒 B 1秒 C 100秒 D 2小时

2：在某些极端要求性能的场合，我们需要对程序进行优化，关天优化，以下说法正确的是(`D`)

A 将程序整个用汇编语言改写会大大提高程序性能

B 在优化前，可以先确定哪部分代码最费时，然后对这部份代码用汇编改写，使用汇编的语句越少，程序运行的越快。

C:使用汇编语句虽然可以提高程序的性能，但会降低程序的可移植性，所以应该绝对避免

D:适当调整汇编指令的顺序，可以缩短程序的运行时间 

3:对如下C语言程序在普通的X86PC上运行输出正确的是(`B`)

    Char * f()
    {
    Char x[512];
    Sprintf(x ,”hello world”);
    Return x+6;
    }
    Main()
    {
    Printf(“%s”,f());
    }
A 程序可能崩溃，也可能输出`hello world`

B 程序可能崩溃，也可能输出 `world`

C 程序可能崩溃，也可能输出`hello`

D 程序一定崩溃

4:方程`X1+X2+X3+X4=30`,有多少满足`X1>=2,X2>=0,X3>=-5,X4>=8`的整数解（`A`）

A 3276  B:3654 C:2925 D:17550

5:一个袋子里装了100个苹果，100个香蕉，100个桔子，100个梨，如果每分钟从里面随机抽取一种水果，那么最多过多少分钟肯定至少能拿到一打相同种类的水果(1打=12)（`D`）

A:40 B:12 C:24 D:45

6:双败淘汰赛与淘汰赛相仿，也是负者出局，但负一场并未淘汰，只是跌入负者组，在负者组再负者（即总共已负两场）才被淘汰，现在有10个人来参加又败淘汰赛，假设我们取消最后胜利组冠军的比赛，那么一共需要多少场比赛？（`B`）

A:16 B:17 C:18 D:19 E:20

7:n个结点的二叉树，最多可以有多少层(`D`)

A: n/2 B:log(n) C:n-1 D:n

8:下面哪一个序列不是上图的一个拓扑排序？（`C`）

A:ebfgadch B:aebdfch C:adchebfg D:aedbfgch

9：假如某主机安装了2GB内存，在其上运行的某支持MMU的32位Linux发行版中，一共运行了X,Y,Z三个进程，下面关于三个进程使用的内存方式，哪个是可行的(`D`)

A.X,Y,Z的虚拟地址空间都映射到0-4G的虚拟地址上

B.X在堆上分配总大小为1GB的空间，Y在堆上分配200MB,Z在堆上分配500MB，并且内存映射访问一个1GB的文件。

C.X在堆上分配1GB,Y在堆上分配800MB,Z在堆上分配400MB

D.以上访问方式都是可行的

10：当使用TCP协议编程时，下列问题哪个是由程序员考虑和处理的(`D`)

A:乱序数据包的传递 

B数据传输过程中的纠错 

C:网络拥塞处理 

D:发送数据的格式与应用层的协议

二：程序设计与算法

1：给定三个整数a,b,c实现函数int median(int a,int b,int c),返回三个数的中位数，不可以使用sort,要求整数操作（比较,位运行，加减乘除)次数尽量少，并分析说明程序最坏和平均情况下使用的操作次数

    int median(int a,int b,int c)
    {
    int abMax=((a+b)+abs(a-b))/2;
    int acMax=((a+c)+abs(a-c))/2;
    if(abMax!=acMax)
    return abMax<acMax?abMax:acMax;
    else
    return ((b+c)+abs(b-c))/2;
    }

2：给定一个key(只含有ASCII编码的小写英文字母),例如kof，然后对input的string(只含有ASCII编码的小写英文字母)利用这个key进行排序，顺序是:先按照key中的字符顺序，然后对key中不包含key的字符，按a-z排序

    #include<iostream>
    #include<algorithm>
    #include<string.h>
    using namespace std;
    int main()
    {
    char key[4]="kof";
    char str[50]="wqtewqtewkwetiowoweff";
    sort(str,str+strlen(str));
    int flag=0;
    for(int i=0;i<strlen(key);i++)
    {
    for(int j=0;j<strlen(str);j++)
    {
    if(key[i]==str[j])
    {
    for(int k=j;k>flag;k--)
    {
    str[k]=str[k-1];
    }
    str[flag]=key[i];
    ++flag;
    }
    }
    }