Date: 2013-12-23
Title: .htaccess简明教程(SEO优化)
Category: 编程语言
Tags: 工具使用
Slug: htaccess
Img:pics/seo.jpg
summary:`.htaccess`文件可以用来优化网站，尽管.htaccess只是一个文件，但它可以更改服务器的设置，允许你做许多不同的事情，最流行的功能是可以创建自定义的404页面，.htaccess并不难，你可以给它想像成就是一个文本文件再加几条服务器的配置命令,确定服务器是否支持.htaccess

----------
.htaccess文件可以用来优化网站，尽管.htaccess只是一个文件，但它可以更改服务器的设置，允许你做许多不同的事情，最流行的功能是可以创建自定义的“404 error”页面，.htaccess并不难，你可以给它想像成就是一个文本文件再加几条服务器的配置命令

确定服务器是否支持.htaccess

如果主机是`unix`或`Linux`系统，或任何版本的`Apache`网络服务器，理论上都是支持`.htaccess`的,除非你的服务器提供商禁用了`.htacess`文件

.htaccess的主要功能:

>1:文件夹密码保护

>2:用户自动重定向

>3:自定义错误页面

>4:改变你的文件扩展名

>5:封禁特定IP地址的用户

>6:只允许特定IP地址的用户

>7:禁止目录列表

>8:使用其他文件作为index文件

创建`.htaccess`文件

Linux/unix以及一些其他类unix系统中可以直接单击右键进行创建，然后将文件命名为.htaccess，或者使用命令行工具`touch .htaccess`命令创建

Window系统下就有些麻烦啦，Windows会把.htaccess当作文件扩展名，一个文件没有名称只有扩展名是不允许被创建的，因此你可以先创建一个普通文件，上传到服务器上，如果服务器提供了在线更改，可以直接在线更改文件名，如果没有提供，可以通过FTP软件来进行更改，还有一种方式，可以在Windows下，下载一些能运行Linux/Unix命令的工具，如`git bash`,在`git bash`上输入`touch .htaccess`同样可以创建

.htaccess文件编写

>自定义错误页：通过自定义错误页将使你可以拥有个性化的错误处理页面，而不是你的主机提供商给你提供的错误页或没有任何页面

>>什么时候会出现错误页,最简单的例子就是当用户访问你网站上并不存在的页面时，出现的那个页面就是错误页

>>例子，将所有的404 error错误处理页转变成网站的首页(最通俗的理解就是当用户访问了网站上并不存在的页面时直接跳到首页上去)

>>`ErrorDocument 404 /index.html`

>>从上面的命令可以推出其他命令的处理方式，代码如下

>>`rrorDocument 错误处理代号 错误处理页面`

>>例如对服务器返回的500指定错误处理页面

>>`ErrorDocument 500 /500.html` 如果文件不在根目录下可以写成/目录名/文件名

>>401 - Authorization Required 需要验证

>>400 - Bad request 错误请求

>>403 - Forbidden 禁止

>>500 - Internal Server Error 内部服务器错误

>>404 - Wrong page 找不到页面

>>命令写法同上

>禁止显示网站的目录列表，当网站根目录下没有index.html，用户通过域名访问网站时会将整个网站的目录显示给用户,禁止方法如下：

>>`Options -Indexes`

>禁止或者允许特定IP地址访问网站

>>禁止特定的IP地址访问，命令如下：

>>`deny from 000.000.000.000`  其中`000.000.000.000`代表的是特定的IP地址，如果只指明其中的几个，则可以封禁整个网段的地址。如你输入`112.27.38.`，则将封禁`112.27.38.0～112.27.38.255`的所有IP地址

>>禁止所有人访问，用以下命令

>>`deny from all`

>>允许特定的IP地址访问，命令如下：

>>`allow from 000.000.000.000` 如果只指明其中的几个，则可以允许某个网段的地址。如你输入`112.27.38.`，则将允许`112.27.38.0～112.27.38.255`的所有IP地址访问网站


>index的替换文件,默认情况下，如果网站下没有index.`*`(`*`可以代表`php`,`html`,`htm`,`jsp`)
>在.htaccess中也没有禁止将目录显示出来，当用户通过域名访问网址时，会将整个网址的目录列出来，通过指定`index.*`替换文件，可以在服务器不存在`index.*`文件的情况下，使用该文件代替。

>> `DirectoryIndex index.php index.php3 messagebrd.pl index.html index.htm`

>重定向相关的命令(**最重要的**),重定向就是将请求重定向到同站内或站外的不同文档，这在你改变了一个文件名称，但仍然想让用户用旧地址访问到它时，变的极为有用，同时也可以通过重定向，将长url变成短url

>>重定向的相关例子

>>`Redirect /loc/file/dir/file.html http://www.othersite.com/sample.html` 将网址上访问特定的url重定向到其他网址

>>`Redirect /oldDir http://www.newsite.com/newDir`目录重定向，任何指向站点/oldDir目录的请求都将被重新指向新的站点,例如当用户访问`http://www.youroldsite.com/oldDir/index.html`将会被重定向到`http://www.newsite.com/newDir/index.html`（这里的www.youroldsite.com就是网站的域名，如[www.yanyulin.info](http://www.yanyulin.info)）

>密码保护

>>.htaccess用于网站目录的密码保护具有完美的安全性（即访问者必须知晓密码才可以访问目录，并且绝无“后门”可走）

>>相关命令，利用.htaccess将一个目录加上密码保护分两步，一：是在你的.htaccess文档里加上适当的几行代码，二是将.htaccess文档放进你要保护的目录下，代码如下

    AuthName "Section Name"
    AuthType Basic
    AuthUserFile /full/path/to/.htpasswd
    Require valid-user

>>`/full/parth/to/.htpasswd`则应该替换为指向`.htpasswd`文件,.htpasswd也是一个没有文件名文档，可以放置在你网站里的任何地方（此时`密码应加密`），但建议你将其保存在网站Web根目录外，这样通过网络就无法访问到它了,文件里的内容是username:password(用户名:密码)