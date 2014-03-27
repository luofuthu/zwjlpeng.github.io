Date: 2014-02-22
Title: 快速介绍Linux（Linux入门教程）
Category: 编程语言
Tags: Linux汇总
Slug: linux1
Img:pics/linux.jpg
summary:文本模式登录(没有图形界面，类似于控制台)，在`VirtulBox`中进入了Linux后，按Ctrl+F1可以进入文本模式如下图,`Shell`是一个命令行解释器，它读取用户的输入，然后执行命令，用户通常通过终端(类似于Windows中的cmd.exe)向shell进行输入，Shell有好多种,Linux系统中以/开关的路径名是绝对路径名，否则为相对路径名...

1：严格意义上，可将操作系统定义为一种软件，它控制计算机硬件资源，提供程序运行环境，我们称此种软件为内核，它相对较小，位于环境中心

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux1.html">
<img src="http://www.yanyulin.info/pics/tech/linuxmen1.png" alt="烟雨林博客"/>
</a>
</center>

图一介绍：

>内核的接口称为系统调用（阴影部分）

>公用函数库(如glibc【即C语言库】)是构建在系统调用之上

>Shell是一种特殊的程序，它为其他应用程序提供一个接口

>登录Linux

>登录Linux有两种方式，一种是文本模式登录，一种是图形界面登录

>文本模式登录【没有图形界面，类似于控制台】，在VirtulBox中进入了Linux后，按Ctrl+F1可以进入文本模式如下图

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux1.html">
<img src="http://www.yanyulin.info/pics/tech/linuxmen2.png" alt="烟雨林博客"/>
</a>
</center>

输入用户名与密码即可登录成功结果如下

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux1.html">
<img src="http://www.yanyulin.info/pics/tech/linuxmen3.png" alt="烟雨林博客"/>
</a>
</center>

图中用户名是pengpeng,登录成功后进入用户的家目录**(所谓家目录即/home/pengpeng这个目录，Linux为系统的每个用户都在/home目录下创建了以用户名为名称的目录，作为用户登录成功后的当前目录)**

图三中命令介绍：

ls 列出当前目录所有文件，不包括隐藏文件

cd改变目录，`cd /home/pengpeng`【/home/pengpeng中/是根目录即根目录->home目录->pengpeng，采用的是绝对路径】【备注cd ~ 改变目录为当前家目录】

图形界面登录略

附:登录过程

用户在登录Linux系统时，输入用户名与密码，系统会在其口令文件/etc/passwd中查看校验是否为合法用户，口令文件如下

在终端上输入`vim /etc/passwd`【vim/vi是linux中的一种文本编辑器，默认只安了vi,安装vim输入以下命令sudo su apt-get install vim】

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux1.html">
<img src="http://www.yanyulin.info/pics/tech/linuxmen4.png" alt="烟雨林博客"/>
</a>
</center>

口令文件组成的意思如：

    pengpeng:x:1000:1000:pengpeng,,,:/home/pengpeng:/bin/bash

其中pengpeng是用户名 x对应的是用户密码【加密了】1000用户ID,1000用户组ID,pengpeng,,,注释字段，/home/pengpeng用户登录后进入的目录【即当前目录为家目录】，/bin/bash登录后用户默认使用的shell即Bourne shell

Shell

Shell是一个命令行解释器，它读取用户的输入，然后执行命令，用户通常通过终端(类似于Windows中的cmd.exe)向shell进行输入，Shell有好多种，如Bourne shell, C shell, Korn Shell,等，我们现在使用的一般都是Bourne shell

文件与目录

Linux文件系统是目录与文件组成的一种层次结构，目录的起点称为根【名称为/】,每个目录中都包括了两个特殊的文件.与..这两个文件是链接文件，分别指向当前目录与上一级目录

`cd .`即转向当前目录【其实不变】 

`cd ..` 返回上一级目录

Linux系统中以/开关的路径名是绝对路径名，否则为相对路径名

实例分析：ls的简要现

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux1.html">
<img src="http://www.yanyulin.info/pics/tech/linuxmen5.png" alt="烟雨林博客"/>
</a>
</center>

在终端上输入`vim lsM.c`创建如上文件

说明

`drent.h`中包括对目录进行的相关操作

`DIR`是一个目录结构

`struct dirent`是一个结构体，包涵目录或者文件的相关属性

编译`lsM.c`生成可执行文件，并执行

<center>
<a href="http://www.yanyulin.info/pages/2014/02/linux1.html">
<img src="http://www.yanyulin.info/pics/tech/linuxmen6.png" alt="烟雨林博客"/>
</a>
</center>

`Gcc`是C语言编译器, -o选项表示后面是输入的目标文件的文件名 lsM.c表示编译的源程序

`Ls`命令输入后可以发现生成了可执行的lsM

`./lsM` `.`可以发现当前目录中包括四个文件

注意：本程序的输出的文件未进行排序，而ls的输出一般是按照字母的顺序进行输出

Main函数使用了ISO C标准使用的风格,argc代表传给程序的参数个数，即`argv`中的个数

按惯例当程序返回0时表示正常结束，返回其他值表求出错

每个进程都有一个工作目录，有时称其为当前工作目录，所有的相对路径都是从工作目录开始解释，进程可以用`chrdir`更改其工作目录。

