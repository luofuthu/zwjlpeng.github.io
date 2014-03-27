Date: 2013-11-29
Title:界面编程模仿篇(模仿腾讯QQ登录界面) 
Category: 玩转技术
Tags:界面编程 
Slug: qqLogin
Img:pics/tech/qq.jpg
summary:写了几天的`爬虫`，过几天再继续写，今天偷会懒，写了个仿`QQ登录界面`，截图如下，怎么样，还凑和吧，如果是大神的，请不要见笑，截图如下，明天争取完成，完成后，将附上文档与代码上传到本人的`github`上，进行开源,如果大家愿意，后绪一块更改，注意，我强调的只是**界面**,QQ?你想吧内部的各种通信协议，分布式数据库，大数据的处理，各种缓存...。

写了几天的爬虫，过几天再继续写，今天偷会懒，写了个仿QQ登录界面，截图如下，怎么样，还凑和吧，如果是大神的，请不要见笑，截图如下，明天争取完成，完成后，将附上文档与代码上传到本人的github上，进行开源,如果大家愿意，后绪一块更改，注意，我强调的只是**界面**,QQ?你想吧内部的各种通信协议，分布式数据库，大数据的处理，各种缓存...

<a href="http://www.yanyulin.info/pages/2013/11/qqLogin.html">
<img  src="http://www.yanyulin.info/pics/tech/qq_1.jpg"/>
</a>

上面程序运行界面中的所有图片都来自QQ2013，本篇文章就介绍如何从`QQ2013`中获取图片，了解了这个过程后，你也可以自已Diy图片，然后将图片替换，设计自已的`非主流QQ`

1、与本程序相关的图片保存在两个地方，`%appdata%\Tencent\QQ\Temp`以及QQ安装目录下的Resource文件夹下`D:\Program Files\Tencent\QQ\Resource.1.97.8200`,从这些文件夹下选取你自已需要的图片，`备注Resource.1.97.8200文件夹Resource后面的数字可能会不同`

<a href="http://www.yanyulin.info/pages/2013/11/qqLogin.html">
<img src="http://www.yanyulin.info/pics/tech/qq_2.jpg"/>
</a>

2、QQ的部份图片保存在rdb文件里，而且图片的格式是gft,下载两款软件，对rdb进行解压，以及对gft格式的文件进行格式转换，转换时最好转成png格式的，软件下载地址：

><a href="http://yunpan.cn/QUMdYmtPW3tsP" target="_blank">rdb文件解压缩</a>

><a href="http://yunpan.cn/QUMdBFZeLrSRa" target="_blank">gft格式转换器</a>

3、对于QQ登录界面，部份图片保存的位置如下图中红色方框如示，在LoginPanel以及LoginUI里

<a href="http://www.yanyulin.info/pages/2013/11/qqLogin.html">
<img  width="100%" src="http://www.yanyulin.info/pics/tech/qq_3.jpg"/>
</a>

4、gft格式图片的转换，如下图所示，先导出当前项，然后将导出的文件拖到`GFT转换.exe`里，即可完成转换

<a href="http://www.yanyulin.info/pages/2013/11/qqLogin.html">
<img  src="http://www.yanyulin.info/pics/tech/qq_4.jpg"/>
</a>

5、从上面的过程中，可以看出QQ图片保存在哪了吧，你完全可以用自已的图片替换掉rdb文件里的图片，这样QQ运行的时候，就变成了你的图片了，在替换之前，最好先备份下