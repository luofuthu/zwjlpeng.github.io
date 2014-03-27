Date: 2014-03-04
Title: git保存用户名与密码(避免用户名密码输入)
Category: 编程语言
Tags: 工具使用
Slug:git
Img:pics/tools/git.jpg
summary:由于本博客是托管于github之上，因此每次`git push -u origin master`时都得输入用户名与密码，是非常烦人的，经过一番尝试，原来可以写一个配置文件避免输入用户名与密码，这样通过git上传文件到github上就非常方便了,`git`工具是由linux之父开发的一款分布式代码管理工具，代码开源，功能强大，`git`开发的一般...

----------

**写在前面的话**

由于本博客是托管于github之上，因此每次`git push -u origin master`时都得输入用户名与密码，是非常烦人的，经过一番尝试，原来可以写一个配置文件避免输入用户名与密码，这样通过git上传文件到github上就非常方便了~~~


`git`工具是由linux之父开发的一款分布式代码管理工具，代码开源，功能强大，`git`开发的一般流程是首先从服务器上`clone`一份主干代码，相当于创建了分支，然后修改分支代码，最后将修改后的代码提交到服务器上，为了安全，每一提交都需要输入用户名与密码，肯定是很繁琐的，因此得想办法，避免每次提交时都需要输入**用户名与密码**

**方法**

1、设置环境变量，在我的电脑上单击右键->属性->高级->环境变量->系统变量->新建里写上如下代码：

	变量名：HOME
	变量值:%HOMEPATH

 如果使用的是Win7系统可以直接输入以下命令:

	setx HOME %USERPROFILE%

 以下是WinXP下的截图：


<center>
<a href="http://www.yanyulin.info/pages/2014/03/git.html">
<img src="http://www.yanyulin.info/pics/tools/git0.jpg"  alt="烟雨林博客"/>
</a>
</center>

2、在运行窗口（可以按Windows+R键）中输入如下命令，即可以打开%HOMEPATH%文件夹，在该文件夹下建立一个文件，文件名为`_netrc`

<center>
<a href="http://www.yanyulin.info/pages/2014/03/git.html">
<img src="http://www.yanyulin.info/pics/tools/git1.jpg"  alt="烟雨林博客"/>
</a>
</center>

命令如下：

	%HOMEPATH%

3、以记事本的形貌打开_netrc文件，在文件里面输入如下配置项：

	machine github.com
	login *****@gmail.com
	password ******

**备注**

代码中

machine：表示要上传的服务器，上述代码中表示要上专到github.com中

login：填入登录用户名，例子中应该填入github帐户名

password：填入登录密码，例子中应该填入github帐户密码

如有问题，可以联系我，联系方式，看博客下方邮箱