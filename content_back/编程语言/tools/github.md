Date: 2013-11-20
Title: Github简明教程(入门篇)
Category: 编程语言
Tags: 工具使用
Slug: github
Img:pics/tools/github.jpg
summary:Github作为一项目托管仓库，里面有着各种各样的高质量代码，本篇博客针对Git入门或者初学者，各位大神可以绕过，关于GitHub的强大之处可以自已百度谷歌去，知道GitHub也有一段时间了,全英文的网页，始终不如中文来得痛快，因此很多人还不会使用，在继续阅读本篇博客之前，如果还没有帐号的同学，先到github官网上申请一个帐号http://www.github.com

----------
Github作为一项目托管仓库，里面有着各种各样的高质量代码，本篇博客针对Git入门或者初学者，各位大神可以绕过，关于GitHub的强大之处可以自已百度谷歌去，在继续阅读本篇博客之前，如果还没有帐号的同学，先到github官网上申请一个帐号http://www.github.com

1、首先登录自已的帐号，创建属于自已的代码库
<a href="http://www.yanyulin.info" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/github1.jpg" width="100%"/>
</a>
2、然后跳转下一个页面，填写`repository name`,如：TEST，在`Add .gitgore`一项根据你所使用语言选择，其他的默认，然后`creat repository`
<a href="http://www.yanyulin.info" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/github2.jpg" width="100%"/>
</a>
做完上面的后，GitHub就生成了一个代码仓库，目前仓库中仅有三个文件，.gitingore/LICENSE/README.md,以及相应的远程仓库地址，这个地址可以使用git工具进行代码的下载与上传
<a href="http://www.yanyulin.info" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/github3.jpg" width="100%"/>
</a>

3.你可以点击上图中Test后面的`+`号新创建一个文件，或者直接选中页面中的一个文件对其进行修改以及删除，但是一般不采用这种方式，这种方式修改的效率太低，一般采用的方式均是通过git工具，将代码下载到
本地，在本地修改后，然后再上传到github托管的代码库中，例如如下（前提是已安装了git工具)

	mkdir tmp
	cd tmp
	git init
	touch test.md
	git add test.md
	git commit -am 'commit'	
	git remote add origin https://github.com/howard5888/TEST.git
	git pull origin master
	git push -u origin master
执行完上述命令后，再看看github里TEST仓库，就可以发现自已新增的文件test.md了
<a href="http://www.yanyulin.info" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/github4.jpg" width="100%"/>
</a>

执行完上面的代码后，打开github的TEST仓库，可以看到TEST仓库里多了一个test.md文件，上面命令中howard5888实际输入时要替换成自已的帐户号，在执行上面的命令上传文件时，会要求用户输入自已的用户名与秘密，在输入的过程中，是不回显的

相关命令解释如下:

1、mkdir tmp 在当前目录下创建一个新的目录 tmp

2、cd tmp 切换到tmp目录下

3、git init tmp目录作为一个本地仓库，初始库git库

4、touch test.md 在当前目录下创建了文件 test.md

5、git add test.md 将test.md文件增加到本地git库中

6、git commit -am 'commit' 提交，让上条增加文件命令生效

7、git remote add 向本地仓库中填加远程仓库地址，远程仓库地址别名是origin

8、git pull origin master 将orgin所代表的远程仓库地址里的master主干下载到本地仓库，即上传之 前先进行一次同步

9、git push -u origin master将本地仓库上传到origin所代表的远程仓库的master分支上

知道了在Github上如何创建仓库，可能还有很多人不知道如何去删除一个仓库，Github上删除仓库也是很容易的，就是有点难找，以删除TEST仓库为例，点击仓库右边的setting
<a href="http://www.yanyulin.info" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/github5.jpg" width="100%"/>
</a>
跳转进入下一个页面，在页面最下方，就有如下图所示的删除铵钮
<a href="http://www.yanyulin.info" target="_blank">
<img src="http://www.yanyulin.info/pics/tools/github6.jpg" width="100%"/>
</a>