import requests
from xml.dom import minidom

xml="""<?xml version="1.0"?>
<methodCall>
<methodName>weblogUpdates.ping</methodName>
<params>
<param>
<value><string>http://www.yanyulin.info/</string></value>
</param>
<param>
<value><string>http://www.yanyulin.info/sitemap.xml</string></value>
</param>
</params>
</methodCall>"""

	
headers={'Content-Type':'text/xml'}
resp=requests.post('http://ping.baidu.com/ping/RPC2',data=xml,headers=headers).text

if "<int>0</int>" in resp:
	print("ping success")
else:
	print("ping failed")


