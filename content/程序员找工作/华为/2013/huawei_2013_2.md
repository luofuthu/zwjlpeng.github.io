Date: 2013-09-11
Title: 2013届华为校园招聘成都上机题目
Category: 程序员找工作
Tags: 华为笔试题
Slug: huawei_2013_2
Img:pics/huawei.jpg
summary:手机号码合法性判断，请实现手机号码合法性判断的`函数`，有一字符串，里面可能包含英文字母（大写、小写）、数字、特殊字符，现在需要实现一函数，请实现身份证号码合法性判断的函数。除满足以上要求外，需要对持有人生日的年、月、日信息进行校验，除成功的情况外，以上其他合法性判断的优先级依次降低。也就是说...

1.手机号码合法性判断（20分）

问题描述：

我国大陆运营商的手机号码标准格式为：国家码+手机号码，例如：8613912345678。特点如下：

1、 长度13位；

2、 以86的国家码打头；

3、 手机号码的每一位都是数字。

请实现手机号码合法性判断的函数（注：考生无需关注手机号码的真实性，也就是说诸如86123123456789这
样的手机号码，我们也认为是合法的），要求：

1） 如果手机号码合法，返回0；

2） 如果手机号码长度不合法，返回1

3） 如果手机号码中包含非数字的字符，返回2；

4） 如果手机号码不是以86打头的，返回3；

注除成功的情况外，以上其他合法性判断的优先级依次降低。也就是说，如果判断出长度不合法，直接返回1即可，不需要再做其他合法性判断。

	int verifyMsinsdn(char *inMsisdn) 

答：

	/*此题简单，按题循环一遍即可*/
	int verifyMsinsdn(char *inMsisdn)
	{
    	if(strlen(inMsisdn)!=13)
    	    return 1;
    	for(int i=0;i<13;i++)
    	    if(inMsisdn[i]<'0'||inMsisdn[i]>'9')
    	        return 2;
    	if(inMsisdn[0]!='8'||inMsisdn[1]!='6')
    	    return 3;
    	return 0;
	}

2.将一个字符串的元音字母复制到另一个字符串，并排序（30分） 

问题描述：

有一字符串，里面可能包含英文字母（大写、小写）、数字、特殊字符，现在需要实现一函数，将此字符串中的元音字母挑选出来，存入另一个字符串中，并对字符串中的字母进行从小到大的排序（小写的元音字母在前，大写的元音字母在后，依次有序）。

说明：

1:元音字母是a,e,i,o,u,A,E,I,O,U。

2:筛选出来的元音字母，不需要剔重；

3:最终输出的字符串，小写元音字母排在前面，大写元音字母排在后面，依次有序。

	void sortVowel (char* input, char* output); 

答

    /*
    	此题循环一遍将大写字母与小写字母分开存储
    	调用泛型算法分别对大写字母与小写字母进行排序
    	再将二者结合起来即可
    */
    #include<iostream>
    #include<cstring>
    #include<algorithm>
    using namespace std;
    void sortVowel (char* input, char* output)
    {
    	string tmpLow,tmpUpper;
    	for(char *p=input; *p!='\0';++p)
    	{
    		if('a'==*p||'e'==*p||'i'==*p||'o'==*p||'u'==*p)
    			tmpLow+=*p;
    		else if('A'==*p||'E'==*p||'I'==*p||'O'==*p||'U'==*p)
    			tmpUpper+=*p;
    	}
    	sort(tmpLow.begin(),tmpLow.end());
    	sort(tmpUpper.begin(),tmpUpper.end());
    	tmpLow+=tmpUpper;
    	strcpy(output,tmpLow.c_str());
    }

3.身份证号码合法性判断  

问题描述：

我国公民的身份证号码特点如下： 

1:长度为18位；

2:第1～17位只能为数字；

3:第18位可以是数字或者小写英文字母x。

4:身份证号码的第7~14位表示持有人生日的年、月、日信息。

例如：511002198808080111或51100219880808011x。

请实现身份证号码合法性判断的函数。除满足以上要求外，需要对持有人生日的年、月、日信息进行校验。年份大于等于1900年，小于等于2100年。需要考虑闰年、大小月的情况。所谓闰年，能被4整除且不能被100整除 或 能被400整除的年份，闰年的2月份为29天，非闰年的2月份为28天。其他情况的合法性校验，考生不用考虑。

函数返回值：

1） 如果身份证号合法，返回0；

2） 如果身份证号长度不合法，返回1；

3） 如果身份证号第1~17位含有非数字的字符，返回2；

4） 如果身份证号第18位既不是数字也不是英文小写字母x，返回3；

5） 如果身份证号的年信息非法，返回4；

6） 如果身份证号的月信息非法，返回5；

7） 如果身份证号的日信息非法，返回6（请注意闰年的情况）；

除成功的情况外，以上其他合法性判断的优先级依次降低。也就是说，如果判断出长度不合法，直接返回1即可，不需要再做其他合法性判断。

要求实现函数：
	int verifyIDCard(char* input)

输入 char* input，表示输入的身份证号码字符串

输出 无

返回 判断的结果，类型为int

示例

1） 输入：”511002111222”，函数返回值：1；

2） 输入：”511002abc123456789”，函数返回值：2；

3） 输入：”51100219880808123a”，函数返回值：3；

4） 输入：”511002188808081234”，函数返回值：4；

5） 输入：”511002198813081234”，函数返回值：5；

6） 输入：”511002198808321234”，函数返回值：6；

7） 输入：”511002198808081234”，函数返回值：0； 

答

	/*
		此题按照题意一步一步的写下来即可，没太多算法基础，主要考的就是思维的严密性
	*/
	#include<iostream>
	#include<memory>
	using namespace std;
	int verifyIDCard(char* input)
	{
	    if(strlen(input)!=18)
	        return 1;
	    for(char *p=input; p!=input+17;++p)
	        if(!isdigit(*p))
	            return 2;
	    if(!isdigit(input[17])&&input[17]!='x')
	        return 3;
	    char year[5]="",mon[3]="",date[3]="";
	    memcpy(year,input+6,4);
	    memcpy(mon,input+10,2);
	    memcpy(date,input+12,2);
	    if(atoi(year)<1900||atoi(year)>2100)
	        return 4;
	    if(atoi(mon)<1||atoi(mon)>12)
	        return 5;
	    if(4==atoi(mon)||6==atoi(mon)||9==atoi(mon)){
	        if(atoi(date)<1||atoi(date)>30)
	            return 6;
	    }
	    else
	    {
	        if(atoi(mon)==2)
	        {
	            if(atoi(year)%400==0)
	            {
	                if(atoi(date)<1||atoi(date)>29)
	                    return 6;
	            }
	            else 
	            if(atoi(date)<1||atoi(date)>28)
	                return 6;
	        }
	        else
	            if(atoi(date)<1||atoi(date)>31)
	                return 6;
	    }
	    return 0;
	｝