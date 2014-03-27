Date: 2014-02-22
Title: Linux里的输入输出（Linux快速入门）
Category: 编程语言
Tags: Linux汇总
Slug: linux2
Img:pics/linux.jpg
summary:Linux系统中每个文件均有一个文件描述符（文件描述符是一个整数），当内核打开一个文件或者创建一个文件时，返回一个文件描述符，读写文件就可以使用它,输入输了关的函数,程序的执行实例被称为进程，`Unix`系统确保每个进程都有一个唯一的数字标识符，称为进程ID.线程也有ID,但ID只在它所属的进程内起作用...

阅读本博文之前可以参考以下文章

<a href="http://www.yanyulin.info/pages/2014/02/linux1.html" target="_blank">
快速介绍Linux（Linux入门教程）
</a>

Linux系统中每个文件均有一个文件描述符（文件描述符是一个整数），当内核打开一个文件或者创建一个文件时，返回一个文件描述符，读写文件就可以使用它

在shell中运行的每个新程序都对应三个文件描述符，标准输入，村准输出，标准出错输出，简单命令`ls`三个文件描述符都指向终端（**linux中将设备都当作文件来操作**），`Shell`中也提供了重定向文件输出，将输出重定向到某个文件如：

    ls > file.txt

将`ls`的输出重定向到`file.txt`（**此时可以发现控制台上没有输出**）

输入输了关的函数

不带缓冲的I/O函数有`open,read,write,lseek,close`（`即中间没有一个缓存区作为过渡`）

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux2.html">
<img src="http://www.yanyulin.info/pics/tech/linuxio.jpg" alt="烟雨林博客"/>
</a>
</center>

注解:

>Linux系统中规定标准输入的文件描述符为0,标准输出为1,标准错误输出为2,`STDIN_FILENO`与`STDOUT_FILENO`分别指定了输入输出的来源

>Read函数返回读的字节数，当到达文件未尾时返回0，如果发生读错误返回-1

>标准I/O，标准I/O函数提供一种带缓冲的I/O函数，并简化了对输入出输出的处理，如fgets(标准函数)函数能读一个完整的行。而read（不带缓存）只能以字节读取。

程序与进程

程序的执行实例被称为进程，`Unix`系统确保每个进程都有一个唯一的数字标识符，称为进程ID.

进程控制的三个主要函数：`fork exec waitpid`

示例程序：

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux2.html">
<img src="http://www.yanyulin.info/pics/tech/linuxio1.png" alt="烟雨林博客"/>
</a>
</center>

程序解释如下：

>标准I/O函数fgets从标准输入中一次读取一行，fgets读取的字符串以换行符做做为结束，面execlp要求其参数是以null结束，故要进行转换。

>`Fork`创建新进程，新进程是调用进程的复制品，fork向父进程返回新创建进程的ID,对子进程而言，返回的是0,(**fork调用一次，返回两次**)

>父进程希望等待子进程终止，则需要调用函数waitpid函数，其参数为要等待进程的ID

线程与线程ID

>线程的提出是为了利用多处理器的并行性，以及程序任务的划分。进程中的所有线程共享地址空间，文件描述符，堆栈，以及进程相关属性。正因为这些特性，才产生了线程的同步问题。

>线程也有ID,但ID只在它所属的进程内起作用，离开了其所属的进程，谈线程没意义。

出错处理：

>文件<errno.h>中定义了符号errno(函数返回的错误代码)可被赋予的各种常量，这些常量均以字符E开头，如EMSGSIZE表示消息过长。	要使用errno需要包函<errno.h>这个头文件，同时在<string.h>中也提供了

>将错误代码转换成有意义的字符串操作函数如：

	char *strerror(int errno);

在`<stdio.h>`中也提供了基于`errno`在标准出错上产生一条出错消息的函数

	void perror(const char *msg)//输出msg指向的字符串，后一冒号，一空格，接着是errno值对应的出错信息，最后是一个换行符。

示例程序如下：

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux2.html">
<img src="http://www.yanyulin.info/pics/tech/linuxio2.png" alt="烟雨林博客"/>
</a>
</center>