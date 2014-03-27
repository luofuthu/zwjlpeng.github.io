Date: 2014-03-15
Title:一款小米抢购软件实现源码分析(HttpClient)
Category: 玩转技术
Tags:实用工具
Slug: xiaomiqianggou
Img:pics/company/xiaomi.jpg
summary:软件采用的是`HttpClient`进行实现，通过`HttpClient`模拟浏览器发送Post请求，实现用户自动登录，并进行密码的修改操作，在这里顺便提一下HtmlUnit开源jar包，HtmlUnit是构建于HttpClient之上的一个开源Jar包，简单的说就是Java版的无窗口浏览器，速度挺快的，支持JS,但支持力度有限，HtmlUnit的使用可以参考如下博文...


----------

**源码下载**

<a href="http://pan.baidu.com/s/1jGr56tC" target="_blank">
小米抢购软件以及源码下载
</a>

**软件可以实现的功能**

1、小米抢购团队密码批量修改软件适用于小米抢购团队，在抢购完成之后防止成员修改密码

2、小米抢购团队密码批量修改软件修改密码速度取决于网速，`200`个号码一般1分钟左右修改完成

3、小米抢购团队密码批量修改软件采用的是多线程实现技术，`速度杠杠的`

4、小米抢购团队密码批量修改软件不是抢购软件

**源码分析**

软件采用的是HttpClient进行实现，通过HttpClient模拟浏览器发送Post请求，实现用户自动登录，并进行密码的修改操作

在这里顺便提一下HtmlUnit开源jar包，HtmlUnit是构建于HttpClient之上的一个开源Jar包，简单的说就是Java版的无窗口浏览器，速度挺快的，支持JS,但支持力度有限

HtmlUnit的使用可以参考如下博文

<a href="http://www.yanyulin.info/pages/2014/03/zhihu_2.html" target="_blank">
一款自动发链接软件的实现细节分析
</a>

<a href="http://www.yanyulin.info/pages/2013/11/fetchPage.html" target="_blank">
爬虫的自我解剖(抓取网页HtmlUnit)
</a>

HttpClient下载链接：

<a href="http://pan.baidu.com/s/1o6O7wnC" target="_blank">
HttpClient相关jar包下载
</a>

软件运行的效果图如下：

<a href="http://www.yanyulin.info/pages/2014/03/xiaomiqiaogou.html">
<img src="http://www.yanyulin.info/pics/tools/xiaomiqianggou_1.jpg" alt="烟雨林博客"/>
</a>

**输件界面代码采用的是substance.jar包中的疏皮肤库实现的，substance相关的jar包下载**

<a href="http://pan.baidu.com/s/1eQ7SHhC" target="_blank">
HttpClient相关jar包下载
</a>

**界面相关的代码**

	JFrame.setDefaultLookAndFeelDecorated(true);
	JDialog.setDefaultLookAndFeelDecorated(true);
	System.setProperty("java.awt.im.style", "on-the-spot");
	UIManager.setLookAndFeel(new org.pushingpixels.substance.api.skin.SubstanceOfficeSilver2007LookAndFeel());

**备注**

System.setProperty("java.awt.im.style", "on-the-spot");此行是为了解决Java输入法中的窗口跟随毛病，但是这种方法效果非常有限，要想彻底解决，估计还得更改源码


**界面采用的是java里面的table进行布局,给table设置数据模型**

	tm=new DefaultTableModel() {		
		private static final long serialVersionUID = 1L;
		@Override
		public Object getValueAt(int rowIndex, int columnIndex) {
			if(!vec.isEmpty())
				return ((Vector)vec.elementAt(rowIndex)).elementAt(columnIndex);  
			return null;
		}
		@Override
		public int getRowCount() {
			return vec.size();
		}	
		@Override
		public int getColumnCount() {
			return title.length;
		}
		public String getColumnName(int column){  
		return title[column];	
		}
		public void setValueAt(Object value,int row,int column){}//数据模型不可编辑，譔方法设置为空
		public boolean isCellEditable(int row,int column){  
		return false;
		}	
	};

**批量读取用户的帐号以及密码**

在导入用户的帐户与密码时会将上次导入的帐号与密码清空，代码如下

	vecInput.removeAllElements();
	vecInput.clear();
	vec.removeAllElements();
	vec.clear();
	String strURL=file.getSelectedFile().getAbsolutePath();
	String data = null;
	br = new BufferedReader(new InputStreamReader(new FileInputStream(strURL)));
	while((data = br.readLine())!=null)
	{
		if(data.trim().length()==0)
			continue;
		String []str=data.split(" ");
		if(str[0].trim().length()==0)
		{
			vecInput.removeAllElements();
			vecInput.clear();
			vec.removeAllElements();
			vec.clear();
			JOptionPane.showMessageDialog(null,"导入了错误数据，请检查","导入结果",JOptionPane.INFORMATION_MESSAGE);
			return ;
		}
		vecInput.add(str[0].trim());
	}
	objThis.setTitle("批量修改密码"+"--已导入帐号("+vecInput.size()+"个)");

**备注**

代码中的vecInput用来存放用户的帐号，vec用来存放用户的密码，此处假设的是用户的密码都是同一个数，因此可以不用存储，在后绪的程序中直接使用这个密码即可

**模拟post请求登录界面**

Httpclient可以模拟post/get请求，操作都是非常方便的，代码如下所示，在模拟post或者get请求时需要先打开浏览器查看一下post请求的参数设置情况：

模拟登录之前需要设置一些超时参数如下：

	httpClient = new HttpClient();
	httpClient.getHttpConnectionManager().getParams().setSoTimeout(10000);
	httpClient.getHttpConnectionManager().getParams().setConnectionTimeout(10000);

如下是post请求的相关参数

	PostMethod postMethod=new PostMethod("https://account.xiaomi.com/pass/serviceLoginAuth");
			NameValuePair[] data = { new NameValuePair("passToken", ""),  
									 new NameValuePair("user",email.trim()),
									 new NameValuePair("pwd", pwd.trim()),
									 new NameValuePair("callback", "https://account.xiaomi.com"),
									 new NameValuePair("sid", "passport"),
									 new NameValuePair("hidden", ""),
									}; 

设置post请求：

	postMethod.setRequestBody(data);
	postMethod.getParams().setParameter(HttpMethodParams.RETRY_HANDLER,null);

开始执行post请求：

	status = httpClient.executeMethod(postMethod);

判断post请求执行是否成功，成功后进行计数操作：

	if(status==200)
		{
			Vector<String> tmp=new Vector<String>();
			tmp.add(email);
			tmp.add("失败(被更改了)");
			try {
				sem.acquire();
				vec.add(tmp);
				tm.fireTableDataChanged();
				sem.release();
			} catch (InterruptedException e) {
				sem.release();
				e.printStackTrace();
			}
				postMethod.releaseConnection();
				postMethod.abort();
				httpClient=null;
				postMethod=null;
				continue;
		}

程序中还使用了多线程操作，具体可以参考程序源码