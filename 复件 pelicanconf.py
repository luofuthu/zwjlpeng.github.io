﻿#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'gum'
AUTHOR = u'烟雨林'
SITENAME = u'烟雨林'
#SITEURL = 'http://zwjlpeng.github.io'
#SITEURL = 'http://localhost:8000'
SITEURL = 'http://www.yanyulin.info'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

#DISQUS_SITENAME = 'zwjlpeng'

#ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{slug}.html'

#CATEGORY_URL='category/{slug}.html'
#CATEGORY_SAVE_AS='category/{slug}.html'

#ARTICLE_URL = 'pages/{category}/{slug}.html'
#ARTICLE_SAVE_AS = 'pages/{category}/{slug}.html'

GOOGLE_ANALYTICS_ID = 'UA-45829467-1'
#GOOGLE_ANALYTICS_SITENAME='yanyulin.info'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
RELATIVE_URLS = False

STATIC_PATHS=["pics",]
# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/all.rss.xml'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ((u'程序员找工作','#'),
					(u'程序员的面经','#'),)

PAGINATION_PATTERNS = (
    (1, '/', '{name}.html'),
    (2, '{base_name}/', 'page/{name}{number}.html'),
)

CAT = [["编程语言","category/bian-cheng-yu-yan.html"],
			 ["程序员找工作","category/cheng-xu-yuan-zhao-gong-zuo.html"],
			 ["精品书籍","category/jing-pin-shu-ji.html"],		 
			 ["视频教程","category/shi-pin-jiao-cheng.html"],
			 ["玩转技术","category/wan-zhuan-ji-zhu.html"],
			 
			 ["投资理财","category/tou-zi-li-cai.html"],
			 ["程序员的面经","category/cheng-xu-yuan-de-mian-jing.html"],
			 ["烟雨杂谈","category/yan-yu-za-tan.html"]
			 ] 

DEFAULT_PAGINATION = 11

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
SOCIAL = (('Atlas', 'http://www.zhangxiaolong.org'),
          (u'我的微博', 'http://weibo.com/lamazi'),
          (u'IT公司笔试题','http://blog.csdn.net/column/details/job-school.html'),
         )
         
         
PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap","neighbors"]         
## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
