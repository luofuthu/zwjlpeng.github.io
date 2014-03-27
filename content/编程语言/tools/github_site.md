Date: 2014-03-05
Title: github搭建网站优化(修复过多的302重定向请求)
Category: 编程语言
Tags: 工具使用
Slug: github_site
Img:pics/tools/github.jpg
summary:本博客采用**pelican**搭建，服务器采用的是免费的**github**,博客搭建完成后，需要在博客根目录下写上一个配置文件`CNAME`,其中`CNAME`写上自已的域名，然后在DNS域名解析器里写上三条A记录，等上24个小时，即可在全球任何地点访问自已的网站，本网站的DNS采用的是免费的DNSpod进行解析，但是如果你用百度或者谷歌对网站的速度...

----------

本博客采用**pelican**搭建，服务器采用的是免费的**github**,博客搭建完成后，需要在博客根目录下写上一个配置文件`CNAME`,其中`CNAME`写上自已的域名，然后在DNS域名解析器里写上三条A记录，等上24个小时，即可在全球任何地点访问自已的网站，本网站的DNS采用的是免费的<a href="https://www.dnspod.cn" target="_blank">DNSpod</a>进行解析，在DNSPod里的配置如下所示：

	主机记录	   记录类型	   线路类型	   记录值  	  MX优先级	   TTL		
	  www         A          默认  207.97.227.245     -         600
	    @         A          默认  207.97.227.245     -         600
	  	*         A          默认  207.97.227.245     -         600

经过了上述的设置之后，的确可以正常访问网站，但是如果你用百度或者谷歌对网站的速度进行诊断，会发现有非常多的302重定向请求

**什么是302重定向请求**

&nbsp;&nbsp;&nbsp;&nbsp;假设浏览器要访问服务器的a.html页面，服务器上没有a.html页面，在服务器上将所有对a.html页面的访问全部转向了访问 b.html,那么当用户访问a.html页面时，服务器就会产生一个应答，应答的类型就是302类型，同时应答消息里还会含有b.html的位置，浏览器在接收到302类型的消息后，会取出应答消息中的url重新发送一次请求，请求b.html


&nbsp;&nbsp;&nbsp;&nbsp;从上述过程的分析中，可以看出一次重定向，会发生两次请求，因些耗费了非常多的时间，当网站中有太多的重定向请求时，势必会影响网站的响应速度


&nbsp;&nbsp;&nbsp;&nbsp;github上搭建的博客，如何按照上述的DNS设置之后，网站由于产生了过多的重定向，会大大影响网站的响应速度，以下是采用上述设置之后，百度诊断网速的结果示意图，是不是很不理想，这样的响应速度不仅影响了用户体验，而且还会影响各大搜索引擎的收录

<center>
<a href="http://www.yanyulin.info/pages/2014/03/github_site.html">
<img src="http://www.yanyulin.info/pics/tools/github_site0.jpg"  alt="烟雨林博客" />
</a>
</center>

**解决方案**

>修改DNS域名解析器，此处即为DNSPod,在DNSPod里停用A记录，采用别名，即CNAME,将CNAME指向主机的域名即可，即指向`username.github.io`

代码如下：

	主机记录	   记录类型	   线路类型	     记录值  	    MX优先级	    TTL		
	  www       CNAME        默认   username.github.io     -         600
	    @       CNAME        默认   username.github.io     -         600
	  	*       CNAME        默认   username.github.io     -         600

>等一会，短点的话大概几分钟左右，长点估计行24小时，因为DNS也要将更改的域名广播出去~~~

测试，采用百度网速度诊断测试，测试后的结果如下图所示，网站的速度还行吧~~~

网站评分结果：

<center>
<a href="http://www.yanyulin.info/pages/2014/03/github_site.html">
<img src="http://www.yanyulin.info/pics/tools/github_site1.jpg"  alt="烟雨林博客"/>
</a>
</center>


网站重定向结果：

<center>
<a href="http://www.yanyulin.info/pages/2014/03/github_site.html">
<img src="http://www.yanyulin.info/pics/tools/github_site2.jpg"  alt="烟雨林博客"/>
</a>
</center>

**pelican搭建博客教程如下**：

<a href="http://www.yanyulin.info/pages/2013/11/pelican.html" target="_blank">
http://www.yanyulin.info/pages/2013/11/pelican.html</a>