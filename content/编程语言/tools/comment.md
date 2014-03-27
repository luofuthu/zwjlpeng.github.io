Date: 2014-03-02
Title: 博客添加第三方评论系统多说评论框
Category: 编程语言
Tags: 工具使用
Slug:comment
Img:pics/tools/duoshuo.jpg
summary:今天`分享`一下，博客如何添加**第三方评论系统**，国外的第三方评论系统已经做的相当强大，如`disqus`,但国外终究是国外，与国内行情不同，如`disqus`不支持**微博、QQ、人人、百度贴吧**登录以及分享等，国内的第三方评论系统起步较国外晚，但做的也相当不错，如**多说、友言、评论啦**等，比较符合国内的行情，本博客...

----------

`博客`已经基本搭建完成，前前后后历时将近两周，采用的是开源工具`Pelican`搭建，服务器采用的是强大的分布式代码托管库`Github`,两者的教程可以参考下面的链接，本博客总共破费了`我3美元`：

><a href="http://www.yanyulin.info/pages/2013/11/pelican.html" target="_blank">
pelican搭建属于自已的博客</a>

><a href="http://www.yanyulin.info/pages/2013/11/github.html" target="_blank">
Github简明教程(入门篇)</a>

><a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
Github上如何给别人贡献代码</a>

><a href="http://www.yanyulin.info/pages/2014/01/pelican_question.html" target="_blank">
pelican创建博客常见问题汇总
</a>

今天`分享`一下，博客如何添加**第三方评论系统**，国外的第三方评论系统已经做的相当强大，如`disqus`,但国外终究是国外，与国内行情不同，如`disqus`不支持**微博、QQ、人人、百度贴吧**登录以及分享等，国内的第三方评论系统起步较国外晚，但做的也相当不错，如**多说、友言、评论啦**等，比较符合国内的行情，本博客最初搭建时采用的第三方评论系统为`disqus`,最后发现`disqus`除了上述的缺点之外，还有一个非常严重的问题，就是在`IE7/IE6`下，`disqus`会出现问题，即不能很好的跨浏览器，使用了将近两周，于是弃之，改用了国内的多说

**为什么采用第三方评论系统**

>1.数据库以及空间贵，我等屌丝还支付不起

>2.第三方评论系统具有强大的反垃圾机制，可以有效的过滤垃圾流言

>3.添加容易，界面操作方便，省去了我们自已写代码

>4.功能比较强大，都带有自已的`分享按钮`以及**微博、QQ、人人、百度贴吧**登录

**多说评论框***

>1.支持国内目前主流的SNS,如**微博、QQ、人人、百度贴吧**,国外嘛，也没必要，你懂的~

>2.团队技术实力还是比较强大

>3.`多说`支持`SEO优化`,这是其最为突出的地方，也最吸引人的...

>4.评论系统反馈比较及时，界面美观，提供自定义....


**重点**

1.向博客中添加评论系统，首先要在多说网上注册自已的帐号，注册帐号后要验证自已的域名，邮箱等，如下图所示：

<center>
<a href="http://www.yanyulin.info/pages/2014/03/comment.html">
<img src="http://www.yanyulin.info/pics/tools/duoshuo1.jpg"  alt="烟雨林博客"/>
</a>
</center>

2.点击管理员左侧的工具，获取通用代码，或者直接复制下面的代码，将该代码粘贴到博客中需要添加评论的地方，即可

    <!-- Duoshuo Comment BEGIN -->
    	<div class="ds-thread"></div>
    <script type="text/javascript">
    var duoshuoQuery = {short_name:"yanyulin"};
    	(function() {
    		var ds = document.createElement('script');
    		ds.type = 'text/javascript';ds.async = true;
    		ds.src = 'http://static.duoshuo.com/embed.js';
    		ds.charset = 'UTF-8';
    		(document.getElementsByTagName('head')[0] 
    		|| document.getElementsByTagName('body')[0]).appendChild(ds);
    	})();
    	</script>
    <!-- Duoshuo Comment END -->
   
**备注**代码中的的`short_name`要改写成添加站点时`http://www.XXXX.duoshuo.com`中的`XXXX`部分，添加成功后，运行图我如下图如博文下面的评论框所示

3.给博文添加最新评论，效果如我的博客右侧栏如示，代码如下：

	<ul class="ds-recent-comments" data-num-items="7" data-show-title="0" data-show-avatars="1" data-show-time="1" data-show-admin="0" data-excerpt-length="40"></ul>
	<div class="clear"></div>
	<!--多说js加载开始，一个页面只需要加载一次 -->
	<script type="text/javascript">
	var duoshuoQuery = {short_name:"yanyulin"};
	(function() {
	    var ds = document.createElement('script');
	    ds.type = 'text/javascript';ds.async = true;
	    ds.src = 'http://static.duoshuo.com/embed.js';
	    ds.charset = 'UTF-8';
	    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ds);
	})();
	</script>
	<!--多说js加载结束，一个页面只需要加载一次 -->

**备注**代码中的的`short_name`要改写成添加站点时`http://www.XXXX.duoshuo.com`中的`XXXX`部分

最终的结果如下图所示

<center>
<a href="http://www.yanyulin.info/pages/2014/03/comment.html">
<img src="http://www.yanyulin.info/pics/tools/duoshuo2.jpg"  alt="烟雨林博客"/>
</a>
</center>

如有问题，可以联系我，联系方式，看博客下方邮箱