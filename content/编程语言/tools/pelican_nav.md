Date: 2014-03-03
Title: pelican创建博客如何设置导航条
Category: 编程语言
Tags: 工具使用
Slug:navigator
Img:pics/pelican.jpg
summary:`Pelican`搭建博客中，如果比较懒，可以直接使用官方提供的主题，官方提供的主题均比较简单，做一些简单的博客还是可以的，但要想做到美观、大方似乎还得努力，今天分享一下，**本博客**(当然也是采用pelican搭建的)在搭建过程中，如何使用pelican创建自定义的菜单，菜单的样式如下图所示,Pelican是基于`Jinja2`模板的，因此...

----------

Pelican搭建博客中，如果比较懒，可以直接使用官方提供的主题，官方提供的主题均比较简单，做一些简单的博客还是可以的，但要想做到美观、大方似乎还得努力，今天分享一下，**本博客**(当然也是采用pelican搭建的)在搭建过程中，如何使用pelican创建自定义的菜单，菜单的样式如下图所示：

<center>
<a href="http://www.yanyulin.info/pages/2014/03/navigator.html">
<img  alt="烟雨林博客" src="http://www.yanyulin.info/pics/tools/nav1.jpg"/>
</a>
</center>

本博客的搭建过程：

><a href="http://www.yanyulin.info/pages/2013/11/pelican.html" target="_blank">
pelican搭建属于自已的博客</a>

><a href="http://www.yanyulin.info/pages/2013/11/github.html" target="_blank">
Github简明教程(入门篇)</a>

><a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">
Github上如何给别人贡献代码</a>

><a href="http://www.yanyulin.info/pages/2014/01/pelican_question.html" target="_blank">
pelican创建博客常见问题汇总
</a>

><a href="http://www.yanyulin.info/pages/2014/03/comment.html" target="_blank">
博客添加第三方评论系统多说评论框
</a>

Pelican是基于Jinja2模板的，因此在设置菜单时有必要了解一些JinJa2的语法以及相关函数

**菜单设置步骤**

1、配置文件`pelicanconf.py`的设置

    DISPLAY_PAGES_ON_MENU = False
    DISPLAY_CATEGORIES_ON_MENU = True

**备注**

`DISPLAY_PAGES_ON_MENU = False`表示的是单独页即`page`文件夹里的标题不显示在导航菜单中


`DISPLAY_CATEGORIES_ON_MENU = False`表示的是目录,即文章分类要显示在导航菜单中

2、在目录中，有些目录不想显示在导航条中，如本博文中的<a href="http://www.yanyulin.info/category/cheng-xu-yuan-zhao-gong-zuo.html" target="_blank">程序员找工作</a>以及<a href="http://www.yanyulin.info/category/cheng-xu-yuan-de-mian-jing.html" target="_blank">程序员的面经</a>可以在配置文件中写上如下语句，表示不想显示的目录：

	LINKS =  ((u'程序员找工作','#'),
			  (u'程序员的面经','#'),)

3、设置好上述的配置文件后，打开你自已的主题，例如本博文的主题是`pelican-themes/gum`,找到templates文件夹下的base.html，写下如下代码：

	<!--表示的是如果是首页时，对样式进行的设置，效果如本博文稿www.yanyulin.info主页导航栏-->
	{% if page_name == "index" %}	  					
	<li  class="current-menu-item current_page_item "><a href="{{ SITEURL }}">烟雨首页</a></li>
	{% else %}
	<li><a href="{{ SITEURL }}">烟雨首页</a></li>
	{% endif %}
    <!--看看菜单栏里是否有菜单-->
	{% for title, link in MENUITEMS %}
	<li ><a href="{{ link }}">{{ title }}</a></li>
	{% endfor %}
    <!--看看page目录下的页标题是否显示-->
	{% if DISPLAY_PAGES_ON_MENU %}
    {% for p in PAGES %}
	<li><a href="{{ SITEURL }}/{{ p.url }}">{{ p.title }}</a></li>
	{% endfor %}
	{% else %}
	<!--关键部件，即显示目录名字到导航条上-->
	{% if DISPLAY_CATEGORIES_ON_MENU %}
    <!--过滤掉不想显示的目录-->
    {% set dit=[] %}
    {% for txm ,null in LINKS %}
	{% if dit.append(txm) %}
	{% endif %}
    {% endfor %}
    <!--开如显示-->
	{% for cat, null in categories  %}
    {% if cat not in dit %}
    {% if category == cat %}					  							
	<li class="current-menu-item current_page_item "><a href="{{ SITEURL }}/{{ cat.url }}">{{ cat }}</a></li>
    {% else %}
	<li><a href="{{ SITEURL }}/{{ cat.url }}">{{ cat }}</a></li>
	{% endif %}
	{%endif%}
	{% endfor %}
	{% endif %}
	{% endif %}

**备注**多看上面注释，代码不难理解

4、更改了上述主题后，将原有主题卸载，重新安装，如下是以本博文主题`gum`为例子，代码如下：
    
    pelican-themes -r gum
    
    pelican-themes -i pelican-themes/gum

如有问题，可以联系我，联系方式，看博客下方邮箱