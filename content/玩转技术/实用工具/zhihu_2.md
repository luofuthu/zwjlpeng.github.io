Date: 2014-03-06
Title:一款自动发链接软件的实现细节分析
Category: 玩转技术
Tags:实用工具
Slug: zhihu_2
Img:pics/tech/zhihu.jpg
summary:阅读此篇博文之前，可以参阅上一篇博文<a href="http://www.yanyulin.info/pages/2014/03/zhihu_1.html" target="_blank">一款自动发链接的软件设计思路</a>，了解该软件的设计思路以及要解决的技术点，和为什么选择Java这种开发语言，**模拟浏览器的登录**，HtmlUnit如何模拟浏览器的登录，可以参考这篇文章<a href="http://www.yanyulin.info/pages/2013/11/fetchPage.html" target="_blank">爬虫的自我解剖(抓取网页HtmlUnit)</a>,由于HtmlUnit本身对JavaScript的支持不是好好...


----------

**源码下载**

<a href="http://pan.baidu.com/s/1mgG38yk" target="_blank">
自动发链接软件下载
</a>

阅读此篇博文之前，可以参阅上一篇博文<a href="http://www.yanyulin.info/pages/2014/03/zhihu_1.html" target="_blank">一款自动发链接的软件设计思路</a>，了解该软件的设计思路以及要解决的技术点，和为什么选择Java这种开发语言。


设计步骤：

1、**模拟浏览器的登录**，HtmlUnit如何模拟浏览器的登录，可以参考这篇文章
<a href="http://www.yanyulin.info/pages/2013/11/fetchPage.html" target="_blank">爬虫的自我解剖(抓取网页HtmlUnit)</a>,由于HtmlUnit本身对JavaScript的支持不是好好，而且也没有必要去加载网页的CSS文件，因此在使用HtmlUnit之前进行相关的配置，禁用CSS以及JavaScript,代码如下：

	final WebClient webClient=new WebClient(BrowserVersion.CHROME);
	webClient.getOptions().setCssEnabled(false);
	webClient.getOptions().setJavaScriptEnabled(false);
	webClient.getOptions().setActiveXNative(false);
	webClient.getOptions().setAppletEnabled(false);
	webClient.getOptions().setPopupBlockerEnabled(false);
	webClient.getOptions().setThrowExceptionOnScriptError(false);
	webClient.getOptions().setPrintContentOnFailingStatusCode(false);

2、经过了上述设置之后即禁用了CSS/JS和一些其他相关的插件，下面分析一下Post请求里的相关参数，打开Chrome浏览器，在网页的登录按钮旁点击审查元素，即可查看该处附近的相关html代码，相关Html代码如下所示(只列出比较关心的部份)

	<div class="email input-wrapper">
	<input required="" type="email" name="email" placeholder="邮箱">
	</div>
	<div class="input-wrapper">
	<input required="" type="password" name="password" maxlength="128" placeholder="密码">
	</div>
	<div class="button-wrapper command">
	<button class="sign-button" type="submit">登录</button>
	</div>

从上述的代码中可以看出Post请求里需要的相关的参数为email以及password,因此Post请求中这两项是必不可少的，模拟登录过程的代码如下图如示：

	final HtmlPage page=webClient.getPage("http://www.zhihu.com/#signin");
	List<HtmlForm> forms=page.getForms();
	HtmlForm login=forms.get(0);
	HtmlTextInput email=login.getInputByName("email");
	HtmlPasswordInput pwd=login.getInputByName("password");
	DomNodeList<HtmlElement> btn=login.getElementsByTagName("button");
	HtmlButton submit=(HtmlButton)btn.get(0);
	email.setText(key.trim());
	pwd.setText(map.get(key));
	submit.click();

到这里登录即以成功，是不是So easy,而且不用我们操作Cookie,此次模拟的是Chrome浏览器登录

**备注注解**

List<HtmlForm> forms=page.getForms();代表的是获取页面上的所有Form表单

HtmlForm login=forms.get(0);由于整个页面上只有一个表单，直接取第一个即可

HtmlTextInput email=login.getInputByName("email");获取页表上的email输入框

HtmlPasswordInput pwd=login.getInputByName("password");获取页面上的密码输入框

下面这两句是用来获取页面上的登录按钮

DomNodeList<HtmlElement> btn=login.getElementsByTagName("button");

HtmlButton submit=(HtmlButton)btn.get(0);

下面这两句是用来设置email与密码

email.setText(key.trim());

pwd.setText(map.get(key));

submit.click();这一句模拟的是用户点击行为

3、用户登录后，下一步的操作就是到论坛列表，也就是到问题列表去寻找问题，由于登录成功后HtmlUnit有cookie记录了访问的标识符，因此非常方便，代码如下：

	final HtmlPage questions=webClient.getPage("http://www.zhihu.com/topic");
	List<HtmlAnchor> hrefs=questions.getAnchors();
	List<String> hrefList=new LinkedList<String>();
	for(int i=0;i<hrefs.size();i++){
	   String href=hrefs.get(i).getAttribute("href");
	   if(href.contains("question")&&!href.contains("www"))
		 hrefList.add("http://www.zhihu.com"+href);
	}

**备注**

此名是到问题列表，注意此该用户仍处于登录状态

final HtmlPage questions=webClient.getPage("http://www.zhihu.com/topic")

获取页面上的所有超链接

List<HtmlAnchor> hrefs=questions.getAnchors();

后面几句是将以问题开头的几个超链接放入`hrefList`中

4、有了超链接之后，就可以直接回复问题，然后带上自已网站的链接了吗？是的，但是这样做，发上去的帖子很容易被删除，而且很容易封号，最好的办法在这篇文章<a href="http://www.yanyulin.info/pages/2014/03/zhihu_1.html" target="_blank">一款自动发链接的软件设计思路</a>中我已经列出来的，可以参考，代码如下

<textarea style="width:100%;height:450px" >
	static public String Search(String ques) {
		WebClient  webClient=new WebClient(BrowserVersion.CHROME);
		webClient.getOptions().setCssEnabled(false);
		webClient.getOptions().setJavaScriptEnabled(false);
		String str = null;
		try {
			str = new String(ques.getBytes("GBK"),"GBK");
		} catch (Exception e) {
			e.printStackTrace();
		}
		String url=UrlEncoded.encodeString(str,"GBK");
		HtmlPage page = null;
		try {
			page = webClient.getPage("http://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word="+url);
		} catch (Exception e) {
			e.printStackTrace();
		}
		DomNodeList<DomElement> doms=page.getElementsByTagName("dd");
		String res=null;
		for(int i=0;i<doms.size();i++)
		{
			HtmlDefinitionDescription def=(HtmlDefinitionDescription)doms.get(i);
			if(def.getAttribute("class").contains("dd answer")){
				String ans=def.asText();
				int  start=0;
				if(ans.indexOf("答：")>-1)
					start=start+2;
				if(ans.indexOf("推荐答案")>-1)
					start=start+4;
				int end=ans.length();
				if(ans.contains("[详细]"))
					end=end-4;
				res=ans.substring(start,end);
				break;
			}
		}
	    webClient.closeAllWindows();			
		return res;
	}
</textarea>

**备注**

从上面的代码中你也可以看出，此处采用的是从百度知道里搜出来的结果进行粘贴的

此时需要对问题进行转码，否则在搜索的结果中会出现码码问题

5、有了问题也有了答案，下一步的操作就是将问题粘贴到答案处，此处的过程仍然是一个post请求的过程，仍然是模拟post请求，同样的方法查看post请求的参数：

<center>
<a href="http://www.yanyulin.info/pages/2014/03/zhihu_2.html">
<img alt="烟雨林博客" src="http://www.yanyulin.info/pics/tech/zhihu3.jpg"/>
</a>
</center>

从上面的请求参数中可以看出模拟post请求需要什么参数了吧，其中id与_xsrf均可以从问题页面中获取，代码如下：

	HtmlDivision text=(HtmlDivision)topic.getElementById("zh-question-detail");
	String id=text.getAttribute("data-resourceid");
	HtmlInput _xsrf1=(HtmlInput)topic.getElementByName("_xsrf");
	String _xsrf=_xsrf1.getAttribute("value");

得于了id,与_xsrf之后，将从百度知道搜索出来的答案作为content即可发送了，代码如下：

	WebRequest request=new WebRequest(new URL("http://www.zhihu.com/answer/add"));
	HttpMethod post=HttpMethod.POST;
	List<NameValuePair> params=new ArrayList<NameValuePair>();
	params.add(new NameValuePair("id",id));
	params.add(new NameValuePair("_xsrf",_xsrf));
	System.out.println(ZhiDaoVerify.head);
	params.add(new NameValuePair("content",new String(searchRes.getBytes("UTF-8"),"UTF-8")));
	params.add(new NameValuePair("anon","0"));
	request.setCharset("UTF-8");
	request.setRequestParameters(params);
	request.setHttpMethod(post);
	try{
		webClient.getPage(request);
		LinkStastics.countLinks(hrefList.get(j).trim());
	}catch(Exception e){
		System.out.println(e.getMessage());
	}

6、上面代码中有一个`LinkStastics.countLinks`此处是一个统计函数，用来统计本次发贴是否成功，即发完贴后再去扫描一下问题页面的回复，是否包含了刚才发送的，代码如下，此处以我的个人博客<a href="http://www.yanyulin.info" target="_blank">www.yanyulin.info</a>为例

	static public int countLinks(String ques){
		WebClient  webClient=new WebClient(BrowserVersion.CHROME);
		webClient.getOptions().setCssEnabled(false);
		webClient.getOptions().setJavaScriptEnabled(false);
		try {
			HtmlPage page = webClient.getPage(ques);
			DomNodeList<DomElement> doms=page.getElementsByTagName("div");
			for(DomElement dom:doms){
				if(dom.getAttribute("tabindex").equals("-1")){
					String text=dom.asText();
					if(text.contains("http://www.yanyulin.info")){
						++cnt;
						array.add(ques);
					}
				}
			}
		} catch (Exception e) {
		   System.out.println(e.getMessage());
		}
	  return 0;
	}

7、还有一个问题就是发贴帐号肯定不止一个，如何多个帐号都对同一个帖子进行回复，而且回答的内容一样，必然会引起管理员的怀疑，以至封号，解决办法自已看源码吧，代码都差不多，自已把源码下下来，看看吧，不难~~

8、程序的运行截图，大家可以自已运行一下，如果有什么问题，可以在博文下面留言