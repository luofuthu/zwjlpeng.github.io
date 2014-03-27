Date: 2013-11-28
Title:爬虫的自我解剖(抓取网页HtmlUnit) 
Category: 玩转技术
Tags:搜索引擎 
Slug: fetchPage
Img:pics/spider.jpg
summary:`网络爬虫`第一个要面临的问题，就是如何`抓取网页`，抓取其实很容易，没你想的那么复杂，一个`开源程序`,在写上上面的4行代码，运行，就可以得到[烟雨林博客](http://www.yanyulin.info "烟雨林")首页的全部内容，上面代码在运行的过程中会出现很多警告，出现这些警告的主要原因是由于以下两点,明白了上面的两点后，将代码重新改写一下，该禁用的就禁用，同时禁用一些不必要的功能，也有利于提高程序的运行效率,再者说网络爬虫也不需要CSS的支持滴。

网络爬虫第一个要面临的问题，就是如何抓取网页，抓取其实很容易，没你想的那么复杂，一个开源`HtmlUnit`包，4行代码就OK啦，例子如下：

	final WebClient webClient=new WebClient();
	final HtmlPage page=webClient.getPage("http://www.yanyulin.info");
	System.out.println(page.asText());
	webClient.closeAllWindows();
在程序中写上上面的4行代码，运行，就可以得到[烟雨林博客](http://www.yanyulin.info "烟雨林")首页的全部内容，上面代码在运行的过程中会出现很多警告，出现这些警告的主要原因是由于以下两点:

1、`HtmlUnit`对`Javascript`的支持不是很好

2、`HtmlUnit`对`CSS`的支持不是很好

明白了上面的两点后，将代码重新改写一下，该禁用的就禁用，同时禁用一些不必要的功能，也有利于提高程序的运行效率,再者说网络爬虫也不需要CSS的支持滴

	final WebClient webClient=new WebClient();
	webClient.getOptions().setCssEnabled(false);
	webClient.getOptions().setJavaScriptEnabled(false);
	final HtmlPage page=webClient.getPage("http://www.yanyulin.info");
	System.out.println(page.asText());
	webClient.closeAllWindows();
`HtmlUnit`的使用:
简介:`HtmlUnit`说白了就是一个浏览器，这个浏览器是用Java写的无界面的浏览器，正因为其没有界面,因此执行的速度还是可以滴，`HtmlUnit`提供了一系列的API,这些API可以干的功能比较多，如表单的填充，表单的提交，模仿点击链接，由于内置了`Rhinojs`引擎，因此可以执行`Javascript`

作用:web的自动化测试(最初的目的),浏览器，网络爬虫


重要API的使用
在介绍API的使用之前要先明白的一个问题是，WebClient,WebWindow,Page三者之间的关系，所有的页面最终都是在一个WebWindow对象里面，WebClient在创建时会自动的创建一个WebWindow对象，当调用getPage时会将新页面加载到WebWindow里，你可以理解成WebClient就是IE内核，WebWindow就是呈现页面的浏览器窗口，三者之间的关系图如下图所示：

1、模拟特定浏览器，也可以指定浏览器的相应版本(HtmlUnit最新版2.13现在可以模拟的浏览器有`Chrome`/`FireFox`/`IE`)

	//模拟chorme浏览器，其他浏览器请修改BrowserVersion.后面
	WebClient  webClient=new WebClient(BrowserVersion.CHROME);
2、查找特定元素，通过get或者XPath可以从HtmlPage中获得特定的Html元素，如下例子

方法一，通过get方法获取

	HtmlPage page=webClient.getPage("http://www.yanyulin.info");
	//从[烟雨林博客]上获取标签hed的内容
	HtmlDivision div=(HtmlDivision)page.getElementById("hed");
方法二，通过XPath获取，XPath通常用于无法通过Id搜索，或者需要更为复杂的搜索时，XPath的相关教程

[XPATH相关教程](http://www.w3school.com.cn/xpath/xpath_syntax.asp "xpath相关教程")

	//同样可以打印出hed的内容,//div中//表示搜索整个文档中的div,并将这些div
	//放入list中，然后获取第一个div
	final HtmlDivision div = (HtmlDivision) page.getByXPath("//div").get(0);
	System.out.println(div.asXml());

3、代理服务器的配置，代理的配置很简单，只需要配置好地址，端口，用户名与密码即可

	final WebClient webClient = new WebClient(BrowserVersion.CHROME, "http://127.0.0.1", 8087);
	final DefaultCredentialsProvider credentialsProvider = (DefaultCredentialsProvider) webClient.getCredentialsProvider();
	credentialsProvider.addCredentials("username", "password");

4、模拟表单的提交

	//获取表单	
	final HtmlForm form = page.getFormByName("form");
	//获取提交按扭
	final HtmlSubmitInput button = form.getInputByName("submit");
	//一会得输入的
	final HtmlTextInput textField = form.getInputByName("userid");
	textField.setValueAttribute("test");
	//点击提交表单
	final HtmlPage page = button.click();
API的使用就介绍到这，网络爬虫中主要目的就是获取页中所有的链接，代码如下：

	java.util.List<HtmlAnchor> achList=page.getAnchors();
	for(HtmlAnchor ach:achList){
	System.out.println(ach.getHrefAttribute());
	}
最后来个例子，HtmlUnit模拟浏览器登录`小米网站帐户`，程运运行的截图如下，`红色方框`表示登录成功跳转到下一个页面出现的帐号：

<a href="http://www.yanyulin.info/pages/2013/11/fetchPage.html">
<img alt="烟雨林博客"  src="http://www.yanyulin.info/pics/art/xiaomi.jpg" width=100%/>
</a>

本博文源代码下载:

><a href="https://github.com/zwjlpeng/Crawler_Self_Analysis" target="_blank">源码下载</a>

><a href="http://yunpan.cn/QURZedFfjFWfQ" target="_blank">Java皮肤库下载</a>

><a href="http://yunpan.cn/QURZ5UXwjnk6W" target="_blank">HtmlUnit源码包下载</a>

><a href="http://yunpan.cn/QURZ5uZLwFmM9" target="_blank">HtmlUnit的Jar包下载</a>




