Date: 2014-03-04
Title: pelican博客搭建设置分页和分页保存位置
Category: 编程语言
Tags: 工具使用
Slug: pelican_page
Img:pics/pelican.jpg
summary:本篇**博客**紧随前几篇博客而来，<a href="http://www.yanyulin.info/pages/2013/11/pelican.html" target="_blank" >pelican搭建属于自已的博客</a>、<a href="http://www.yanyulin.info/pages/2014/01/pelican_question.html" target="_blank" >pelican创建博客常见问题汇总</a>、<a href="http://www.yanyulin.info/pages/2014/03/comment.html" target="_blank" >博客添加第三方评论系统多说评论框</a>、<a href="http://www.yanyulin.info/pages/2014/03/navigator.html" target="_blank" >pelican创建博客如何设置导航条</a>，今天介绍一下pelican创建博客中如何进行博客的分页，分页效果可以参考本博客首页底部效果图，该效果图类似于百度搜索的分页机制，一次性不会显示出全部分页...

----------
本篇**博客**紧随前几篇博客而来

<a href="http://www.yanyulin.info/pages/2013/11/pelican.html" target="_blank" >pelican搭建属于自已的博客</a>

<a href="http://www.yanyulin.info/pages/2014/01/pelican_question.html" target="_blank" >pelican创建博客常见问题汇总</a>

<a href="http://www.yanyulin.info/pages/2014/03/comment.html" target="_blank" >博客添加第三方评论系统多说评论框</a>

<a href="http://www.yanyulin.info/pages/2014/03/navigator.html" target="_blank" >pelican创建博客如何设置导航条</a>

今天介绍一下pelican创建博客中如何进行博客的分页，分页效果可以参考本博客首页底部效果图，该效果图类似于百度搜索的分页机制，一次性不会显示出全部分页，会随用户的选择的分页显示出该分页前几分页以及后几分页，话不多说，截图如下：



<center>
<a href="http://www.yanyulin.info/pages/2014/03/pelican_page.html">
<img  alt="烟雨林博客"  src="http://www.yanyulin.info/pics/tools/pelican_page0.jpg"/>
</a>
</center>

pelican创建上述分页机制的步骤如下：

1、更改配置文件pelicanconf.py，加入如下配置选项：

    DEFAULT_PAGINATION = 11
	PAGINATION_PATTERNS = (
    	(1, '/', '{name}.html'),
    	(2, '{base_name}/', 'page/{name}{number}.html'),
	)

**配置选项的含义**

   DEFAULT_PAGINATION = 11表示分页时一页显示11条

   PAGINATION_PATTERNS里面配置的是分页时各分布保存的位置，上述代码的含义就是第1分页保存在网站根目录下，从第二分页开始，保存在page目录下

2、Pelican采用的是`JinJa2`模板，最好先了解一下`JinJa2`,本博客中分页长度是11个长度，也就是上图中的分页小方块最多有11个，当分页数`>11`时，假设为12时，当用户点击第10页时，则会显示`2-12`页，当用户点击第1页时，则又会显示`1-11`页，实现代码如下(代码更改在模板中的pagination.html中)：

<textarea style="width:100%;height:450px" >
	{% if DEFAULT_PAGINATION %}
		{% set pageCut=11 %}
		{% set cut=5 %}
		<div class="navigation_b">
			<div class="pagination">		
				{% set currentpage=articles_page.number %}
				{% if currentpage-cut >0 and articles_paginator.num_pages-currentpage >= cut %}
					{% for j in range(currentpage-cut,currentpage) %} 
						{% if j ==currentpage %}
						   <span class="current">{{articles_page.number}}</span>
						{% elif j ==1 %}
						   <a href="{{ SITEURL }}/{{ page_name }}.html" class="inactive">{{ j }}</a>		
						{% else %}
						   <a href="{{ SITEURL }}/page/{{ page_name }}{{ j }}.html" class="inactive">
							{{ j }}
						   </a>
						   {% endif %}
					   {% endfor %}
					   {% for j in range(currentpage,currentpage+cut+1) %} 
						   {% if j ==currentpage %}
						     <span class="current">{{articles_page.number}}</span>
						   {% else %}
							  <a href="{{ SITEURL }}/page/{{ page_name }}{{ j }}.html" class="inactive">
							  {{ j }}
							  </a>
						   {% endif %}
						{% endfor %}
				 {% elif articles_paginator.num_pages > pageCut and articles_paginator.num_pages-currentpage<pageCut %}
					   {% for j in range(pageCut-1,-1,-1) %} 
							{% if articles_paginator.num_pages-j==currentpage %}
							  <span class="current">{{articles_page.number}}</span>
							{% elif articles_paginator.num_pages-j ==1 %}			
								<a href="{{ SITEURL }}/page/{{ page_name }{{ j }}.html" class="inactive">
								{{ j }}
								</a>
							{% else %}
							    <a href="{{ SITEURL }}/page/{{ page_name }}{{ articles_paginator.num_pages-j }}.html" class="inactive">
									{{ articles_paginator.num_pages-j }}
								</a>
							{% endif %}
						{% endfor %}	
				  {% else %}
							{% if articles_paginator.num_pages < pageCut %}
								{% set realPage=articles_paginator.num_pages %}
							{% else %}
								{% set realPage=pageCut %}
							{% endif %}
							{% for j in range(1,realPage+1) %} 
								{% if j ==currentpage %}
							  <span class="current">{{articles_page.number}}</span>
								{% elif j ==1 %}
								<a href="{{ SITEURL }}/{{ page_name }}.html" class="inactive">
									{{ j }}
								</a>
								{% else %}
								  {% if j ==currentpage %}
							  	   <span class="current">{{articles_page.number}}</span>
							  	  {% else %}
									<a href="{{ SITEURL }}/page/{{ page_name }}{{ j }}.html" class="inactive">
										{{ j }}
									</a>
								  {% endif %}
								{% endif %}
							{% endfor %}									
						{% endif %}
			<a href="{{ SITEURL }}/{{ page_name }}.html">首页</a>
			{% if articles_paginator.num_pages == 1 %}
					<a href="{{ SITEURL }}/{{ page_name }}.html">
						尾页
					</a></div>
			{% else %}
					<a href="{{ SITEURL }}/page/{{ page_name }}{{articles_paginator.num_pages}}.html">
						尾页
					</a></div>
			{% endif %}
    </div>
    {% endif %}
</textarea>

上述的代码看起来比较长，去掉CSS样式后可以直接使用

**备注，程序注解**

1、`{% if DEFAULT_PAGINATION %}`表示的是如果设置了分布时，则执行后绪代码

2、`{% set pageCut=11 %}`设置一变量，代表的是每页显示的条目数

3、`{% set cut=5 %}`表示的是以用户当前点击的分页为坐标，该分页前后应该都显示`5页`(如果当前页前面或者后面分页数不足五页要在程序中进行处理)

4、`articles_page.number`代表的是当前所处的分页

5、`articles_paginator.num_pages`代表的是总共的分页数目

6、`{{ SITEURL }}`代表的是网站域名，在配置文件中可以查到，此处就是<a href="www.yanyulin.info"  target="_blank">http://www.yanyulin.info</a>

7、`{{ page_name }}`代表的是分页名，其中分页名还含有分页所在的目录，即假如分页pelican.html在page目录下的category目录中，则分页名实际上为**category/pelican**


**如有问题，可以联系我，联系方式，看博客下方邮箱**