Date: 2013-11-22
Title: Github上如何给别人贡献代码
Category: 编程语言
Tags: 工具使用
Slug: githubM
Img:pics/tools/github.jpg
summary:本篇重点介绍`Github`上如何给别人贡献代码，通过这个过程，也可以知道如果一个项目托管到Github上，团队成员之间合作的流程，给别人贡献代码，特别是一些开源组织，是件光荣的事,本篇博文仅随前篇博文[`Github`简明教程(入门篇)](http://www.yanyulin.info/pages/2013/11/github.html "Github简明教程(入门篇)")，当然我的独立博客也是采用Github搭建,如有错误，还请指出，同样大神们可以绕过。

----------
本篇博文仅随前篇博文[`Github`简明教程(入门篇)](http://www.yanyulin.info/pages/2013/11/github.html "Github简明教程(入门篇)")，当然我的独立博客也是采用Github搭建，我所介绍的Github正是我搭建博客过程中一点一点学习的过程，如有错误，还请指出，同样大神们可以绕过。

本篇重点介绍`Github`上如何给别人贡献代码，通过这个过程，也可以知道如果一个项目托管到Github上，团队成员之间合作的流程，给别人贡献代码，特别是一些开源组织，是件光荣的事

1、搜索你要贡献的代码仓库，在这里我创建了两个帐号，一个主帐号，里面有一个代码仓库mfjc，一个是将要贡献代码的帐号howard5888,搜索代码仓库如下图：
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github1.jpg" width="100%"/>
</a>
2、按下回车后，即会出现搜索到的库，如下图所示
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github2.jpg" width="100%"/>
</a>
3、点击上图中的仓库链接，进入mfjc仓库，点击右边的fork,fork的含义就是创建mfjc项目的副本作为你自已的项目
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github3.jpg" width="100%"/>
</a>
4、fork之后的图如下图所示，从下图可以看出mfjc已经处于自已的github帐号库中，同时也可以发现github还标明了该库的来源，因为只有标明了来源，后面你修改了文件才有提交的路径
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github3.jpg" width="100%"/>
</a>
5、修改或者增加仓库里的文件，可以选择在线修改，在线修改一般适合修改量较少，这里介绍的是采用Git工具，将代码仓库下载到本地，在本地修改之后再上传上去，相关命令如下：

	mkdir tmp #创建tmp目录
	cd tmp #切换到tmp目录
	git init #创建并初始化git库
	#增加远程git仓库
	git remote add origin https://github.com/howard5888/mfjc.git
	#将远程git库下载到本地
	git pull origin master
6、命令执行完后，可以看看从mfjc下载下来的文件，如下图所示
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github5.jpg" width="100%" height="30px"/>
</a>
7、假设我们修改了README.md文件，在这个文件里面增加了#test#，接下来要做的就是将修改后的代码库上传上去，命令如下：

	#会将当前目录tmp下所有文件都增加到本地库中
	git add .
	#提交更改
	git commit -am 'commit'
	#将库上传到github上
	git push -u origin master
8、上传完后，再回到github网站上，可以看到README.md文件内容已更改
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github6.jpg" width="100%"/>
</a>
9、最后就是将修改提交给主帐号的原作者，由它来决定是否合并你的修改，操作如下，点击Pull request后，跳转到下一个页面，在下一个页面上点击New pull Request
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github7.jpg" width="100%"/>
</a>

10、接下来的界面上显示了修改后的文件与原作者库里的文件有哪些地方不同
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github8.jpg" width="100%"/>
</a>

11、然后点击Click to create ....即可跳转到最后一个页面，在最后一个页面上写上自已的提交注释，点击Send Request即可
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github9.jpg" width="100%"/>
</a>
12、主帐号里的源作者即可收到你的提交请求，如果觉的可以的话，就会将你的请求同主干合并

13、估计还有很多人不知道如何与原作者的项目保持同步，**如何保持与原作者同步**，原作者估计肯定是一个勤劳的码神，而且又有重多的贡献者，因此与原作者保持同步是很重要的，而且在同步的过程中，你会看到别人每次提交的更改，**这也是Github最大的价值之一**，保持与原作者同步首先要做的就是重复第9步，之后会跳到如下页面

<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github10.jpg" width="100%"/>
</a>

14、点击上图中的红色框里，跳转到下一个页面，在下一个页面中，你会看到项目中的每次更新操作，如下图所示：
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github11.jpg" width="100%"/>
</a>

15、点击绿色方框里的Create...，进入下一个页写，写上title以及comment,点击Send pull,即可跳转到下一个页面，在下一个页面中间处点击Merge request,即可进行同步
<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/2github12.jpg" width="100%"/>
</a>

下一篇将介绍如何利用Github搭建属于自已的博客

[烟雨林个人博客](http://www.yanyulin.info "烟雨林个人博客")