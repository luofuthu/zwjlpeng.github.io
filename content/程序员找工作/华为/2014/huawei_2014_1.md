Date: 2013-11-18
Title: 2014年华为校招机试(一)
Category: 程序员找工作
Tags: 华为
Slug: huawei_2014_1
Img:pics/huawei.jpg
summary:通过键盘输入一串小写字母(a~z)组成的字符串,请编写一个字符串过滤程序，若字符串中出现多个相同的字符，将非首次出现的字符过滤掉;通过键盘输入一串小写字母(a~z)组成的字符串,请编写一个字符串压缩程序，将字符串中连续出席的重复字母进行压缩，并输出压缩后的字符串,压缩规则：仅压缩连续重复出现的字符。

----------
通过键盘输入一串小写字母(a~z)组成的字符串。请编写一个字符串过滤程序，若字符串中出现多个相同的字符，将非首次出现的字符过滤掉。
比如字符串“abacacde”过滤结果为“abcde”。
要求实现函数：`void stringFilter(const char *pInputStr, long lInputLen, char *pOutputStr)`

输入

`pInputStr`：输入字符串

`lInputLen`：  输入字符串长度       
  
输出  

`pOutputStr`： 输出字符串，空间已经开辟好，与输入字符串等长；
 
注意 只需要完成该函数功能算法，中间不需要有任何IO的输入输出

示例
 
输入：“deefd”        输出：“def”

输入：“afafafaf”     输出：“af”

输入：“pppppppp”     输出：“p”

    #include<algorithm>
    #include<iostream>
    using namespace std;
    void stringFilter(const char *pInputStr, long lInputLen, char *pOutputStr)
    {
    	for(int i=0;i<lInputLen;i++)
    		if(find(pInputStr,pInputStr+i,pInputStr[i])==pInputStr+i)
    			*pOutputStr++=pInputStr[i];
    }
通过键盘输入一串小写字母(a~z)组成的字符串。请编写一个字符串压缩程序，将字符串中连续出席的重复字母进行压缩，并输出压缩后的字符串。

压缩规则：仅压缩连续重复出现的字符。比如字符串"abcbc"由于无连续重复字符，压缩后的字符串还是"abcbc"。

压缩字段的格式为"字符重复的次数+字符"。例如：字符串"xxxyyyyyyz"压缩后就成为"3x6yz"。

要求实现函数：` void stringZip(const char *pInputStr, long lInputLen, char *pOutputStr);`
`pInputStr`：输入字符串

`lInputLen`：输入字符串长度

`pOutputStr`： 输出字符串，空间已经开辟好，与输入字符串等长；

注意只需要完成该函数功能算法，中间不需要有任何IO的输入输出

示例 

输入：“cccddecc”   输出：“3c2de2c”

输入：“adef”     输出：“adef”

输入：“pppppppp” 输出：“8p”
    
    void stringZip(const char *pInputStr, long lInputLen, char *pOutputStr)
    {
    	for(int i=0;i<lInputLen;)
    	{
    		for(int j=i,count=0;j<lInputLen&&(pInputStr[j]==pInputStr[i]);j++,++count);
    		count>1?(*pOutputStr++=count+48,*pOutputStr++=pInputStr[i],i+=count):(*pOutputStr++=pInputStr[i],i+=count);
    	}
    }