Date: 2014-01-08
Title: pelican创建博客常见问题汇总
Category: 编程语言
Tags: 工具使用
Slug: pelican_question
Img:pics/pelican.jpg
summary:No valid files found in content errors当用`pelican`创建博客时出现此问题的原因是因为`pelican`创建博客时读取到`contents`目录下的md文件，而md文件需要`markdown`的相库库解析，`pelican`此时缺少该库，因此可以通过以下命令安装`markdown`的相应库

----------
1、No valid files found in content errors

当用`pelican`创建博客时出现此问题的原因是因为`pelican`创建博客时读取到`contents`目录下的md文件，而md文件需要`markdown`的相库库解析，`pelican`此时缺少该库，因此可以通过以下命令安装`markdown`的相应库

	pip install markdown

如果你还没有安装`pip`工具，可以参考下面一篇文章安装`pip`工具

[pelican搭建属于自已的博客](http://www.yanyulin.info/pages/2013/11/pelican.html "pelican搭建属于自已的博客")

安装完问题大概即可解决

2、markdown即md文件中可不可以包含其他元数据?pelican要求md文件必须包含

	title:XXX
	date: XXX

用户也可以创建自定义的元数据，例如给每一篇文章增加一个修改日期

	Modified: 2012-08-08

在后绪的模板页中可以直接访问该元数据，例如在`article.html`中可以使用以下代码

	{% if article.modified %}
	Last modified: {{ article.modified }}
	{% endif %}

如果需要在`article.html`以外的地方使用该元数据，需要在使用的地方加上如下语句

	{% if article and article.modified %}

3、如何禁用feed

pelican中禁用feed的产生是非常容易的，只需要在配置文件`pelicanconf.py`中加入如下几条语句即可完成

	FEED_ALL_ATOM = None
	CATEGORY_FEED_ATOM = None
	TRANSLATION_FEED_ATOM = None

4、warning about feeds generated without SITEURL being set properly

RSS and Atom feeds要求URL必须是绝对链接，而不是相对链接，因此为了产生正确的链接，pelican要求在配置文件中必须设置SITEURL选项，否则产生的RSS与Feeds可能不正确

5、如何给一篇文章指定URL

在需要指定URL的文章或者页面中包括两个元数据`url`与`save_as`,例如以下代码

	url: override/url/
	save_as: override/url/index.html
这个代码指定了本篇文章的url为override/url/index.html

6、如何将一篇文章设置为主页

根据上面的第5条很容易将一篇文章设置为网站的主页，如下代码即可实现将 content/pages/home.md设为主页

	Title: [www.yanyulin.info](http://www.yanyulin.info)
	Date: 2014-01-08
	URL:
	save_as: index.html
	文章正文内容!

7、如何给一篇文章指定一个特定模板

给一篇文章指定一个特定的模板也很简单，只需要在文章中添加如下元数据，并且确保该模板文件在模板中存在即可

    Template: template_name

8、如果还不知道怎么使用pelican创建博客，看如下教程

[pelican搭建属于自已的博客](http://www.yanyulin.info/pages/2013/11/pelican.html "pelican搭建属于自已的博客")

