Date: 2013-11-24
Title: pelican搭建属于自已的博客
Category: 编程语言
Tags: 工具使用
Slug: pelican
Img:pics/pelican.jpg
summary:`WordPress`、`Zblog`、各种`cms`,功能都很强大，各种插件，各种牛X，各种方便，但在我看来，也正是因为功能的太过强大，显得太笨重，修改起来太过麻烦，更可耻的是还需要数据库的支持，我这样的叼丝学生估计还负担不起，而国外提供免费数据库的空间绝大多数都不太稳定，国内空间别提了，各种泪,静态博客生成器:`Jeklly`非常棒

----------
一直都想搭建一个属于自已的博客，无耐总是抽不出时间，9月份完工作，10月份却又有搞不完的事，一拖再拖，前不久才将自已的博客搭建完成

搭建博客工具的选择：

`WordPress`、`Zblog`、各种`cms`,功能都很强大，各种插件，各种牛X，各种方便，但在我看来，也正是因为功能的太过强大，显得太笨重，修改起来太过麻烦，更可耻的是还需要数据库的支持，我这样的叼丝学生估计还负担不起，而国外提供免费数据库的空间绝大多数都不太稳定，国内空间别提了，各种泪

静态博客生成器:`Jeklly`非常棒，基于`octopress`也相当的不错，可惜都是基于ruby语言的，对ruby语言压根就不了解，最终选择了基于`python`的`pelican`

`pelican`搭建博客需要了解的名词

- `Github`
- `python`
- `pelican`
- `Jinja2`
- `markdown`
- `git`
- `sitemap`
-  `pip`

最初是在Linux下搭建博客，正在捉急的进行到一半途中，linux系统让我弄的崩溃了，最后是在Windows下搭建完成，不过linux下是类似的，因为搭建过程是在Git Bash中完成，Git Bash中的命令就是仿unix的

**前提了解github的使用，可以看看我写的Github相关文章**

1、<a href="http://www.yanyulin.info/pages/2013/11/github.html">Github简明教程(入门篇)</a>

2、<a href="http://www.yanyulin.info/pages/2013/11/githubM.html">Github上如何给别人贡献代码</a>

步骤一：下载相关的软件，`pelican`是基于`python`的，因此`python`是不可少的，与`github`进行连接
`git`工具也是不可少的，另外还得下载的三个工具是`python`的`pip`工具以及`markdownpad`编辑器还有`Windows`下的`make`工具，如果是在linux下，此处工作相当简单，相关软件的下载链接，请查看我个人博客的原始博文

1、<a href="http://yunpan.cn/QUF66GnJ7WU7W" target="_blank">python3下载</a>

2、<a href="http://yunpan.cn/QUF6BFpTcgeLc" target="_blank">git下载</a>

3、<a href="http://yunpan.cn/QUF66RuY8ziq5" target="_blank">pip下载</a>

4、<a href="http://yunpan.cn/QUF6BpkxgdpLb" target="_blank">windows下make下载</a>

5、<a href="http://yunpan.cn/QUF66w7tQLcQd" target="_blank">markdown下载</a>

**`pip`工具的安装**

`python3`下安装pip

	//已安装python3
	//下载easy_install的tar.gz的源码
	//然后解压
	C:\python32\python setup.py install
	C:\python32\Scripts\easy_install pip
	//把C:\python32\Scripts这个路径也加到PATH里

**`window`下make工具的安装**

	//将下载的`make.exe`文件添加到path路径中

基他软件直接点击exe安装即可

步骤二:安装`pelican`,安装了`Git`后，打开`Git Bash`输入以下命令

	pip install pelican

步骤三:创建博客，在Git Bash命令行窗口中输入如下命令

	mkdir blog
	cd blog
	pelican-quickstart

第三条命令执行后会提示你输入博客的配置项，除了`SITENAME`配置项外，其他均可选择默认，在后绪的开发过程中，可以在`pelicanconf.py`中进行修改，执行完上述命令后，即可生成一个基本的博客架构，如下图所示

    blog/
    ├── content  # 存放你要写的博客
    │   └── (pages)  #单纯的页面
    ├── output   # 生成的输出文件
    ├── develop_server.sh# 方便开启测试服务器
    ├── Makefile # 方便管理博客的Makefile
    ├── pelicanconf.py   # 主配置文件
    └── publishconf.py   # 主发布文件，可删除

用`markdown`写博文，要记住的是博文必须放在`content`目录下，`pelican`会将`content`目录下的所有文章输出到`output`目录下，然后放到服务器上，`markdown`写博文的预览图如下：

<a href="http://www.yanyulin.info/pages/2013/11/pelican.html">
<img src="http://www.yanyulin.info/pics/markdown.jpg"   alt="烟雨林博客" width="100%"/>
</a>

写完后执行如下命令，即可在本机上预览博客,预览地址为`http://localhost:8000/`

	make publish
	make serve

步骤四:将博客部署到`github`上，博客最终是要放到互联网上供人看的，此处就是将博客上传上去，在上传之前，要确保`github`上有一个仓库命令规是`username.github.io`,其中`username`为你的`github`帐号

	//切换到输出目录
	cd output
	git init
	git add .
	git remote add origin https://github.com/username.github.io.git
	git pull origin master
	git commit -am 'commit'
	git push -u origin master

执行完上面命令后即将博客上传至`github`服务器上，打开浏览器输入`http://username.github.io`即可访问，如果你觉的上面的命令过于复杂，你也直接可以将其添加到Makefile中

步骤五:给博客挑选主题，博客的初始主题当然是不好看，你可以自已下载`pelican`相关的主题，然后安装，当然你也可以像我一样更改主题模板，创建属于自已的

	git clone https://github.com/getpelican/pelican-themes.git
	cd pelican-themes
	pelican-themes -i bootstrap2

在`pelicanconf.py`中添加`THEME = 'bootstrap2'`即可，然后重新`make publish`即可

步骤六：给博客加上评论系统，在Disqus上申请一个站点，记牢Shortname。 在pelicanconf.py添加如下命令，当然你也可以选择国内的多说或者其他的

	DISQUS_SITENAME = Shortname

步骤七：给自已的博客加上谷歌分析，可选，去去Google Analytics申请账号，记下跟踪ID。 在pelicanconf.py添加

	GOOGLE_ANALYTICS = 跟踪ID

步骤入：独立域名与DNS解析

在Godaddy上用支付宝花购买为期一年的顶级域名，并去修改Nameservers为这两个地址：`f1g1ns1.dnspod.net`、`f1g1ns2.dnspod.net`。

在Dnspod上添加新域名，并申请一条A记录指向Github Pages的ip:`207.97.227.245`；

在Pelican主目录新建CNAME文件，添上刚刚申请的域名，如我的`www.yanyulin.info`

Pelican官方文档: http://docs.getpelican.com/en/3.2