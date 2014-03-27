Date: 2012-11-12
Title: 2012年华为校招南京机试
Category: 程序员找工作
Tags: 华为笔试题
Slug: huawei_2012_3
Img:pics/huawei.jpg
summary:给定一个字符串，寻找它的一个最大子字符串，该子字符串是`回文`。例如给定一个用例的字符，问题描述： 在给定字符串中查找所有特定子串并删除，若是没有找到响应`子串`，则不作任何操作，在计算机中，由于位宽限制，只能进行有限精度的十进制整数加减法，比如在32位宽计算机中，参与运算的操作数和结果必须...

一：给定一个字符串，寻找它的一个最大子字符串，该子字符串是回文。例如给定一个用例的字符串`”gabcdcbaef”`,那么最大回文 字串是”abcdcba”

函数声明为

	void huiwen(char input[], int len, char output[]) 

答：

	//如果是回文字符串，那么从字符串的最中间向两头分别遍历，则应该都是相等的
	void huiwen(char input[],int len, char output[])
	{
	    //start表示回文字串的起始位置
	    int max=0,left=0,start=0,left1=0;
	    for(int i=0;i<len;i++)
	    {
	        for(int t=0;t<=i;++t)//奇数
	        {
	            if(i+t>len)//避免发生了越界访问
	                break;
	            if(input[i-t]!=input[i+t])//从中间向两边遍历
	                break;
	            else 
	                ++left;
	        }
	        for(int t1=0;t1<=i;++t1)//偶数
	        {
	            if(i+t1-1>len)//避免发生了越界访问
	                break;
	            if(input[i-t1]!=input[i+t1+1])//从中间向两边遍历
	                break;
	            else 
	                ++left1;
	        }
	        int maxLeft=left>left1?(2*left-1):(2*left1);
	        if(maxLeft>max)
	        {
	            max=maxLeft;
	            start=i-maxLeft/2+1;//获取其起始地址
	        }
	        left=0;
	        left1=0;
	    }
	    memcpy(output,input+start,max);
	}

二：删除字符串中所有给定的子串

问题描述： 在给定字符串中查找所有特定子串并删除，若是没有找到响应子串，则不作任何操作。要求实现函数： 

	int delete_sub_str(const char *str, const char *sub_str, char *result_str)

输入: 

>str：输入的被操作字符串

>sub_str：需要查找并删除的特定子字符串

>输出: result_str：在str字符串中删除所有sub_str子字符串后的终局

>返回: 删除的子字符串的个数

子串匹配只考虑最左匹配情况，即只需要从左到右进行字串匹配的情况。比如：在字符串"abababab"中，采用最左匹配子串"aba", 可以匹配2个"aba"字串。若是匹配出从左到右位置2起头的"aba"，则不是最左匹配，且只能匹配出1个"aba"字串。输入字符串不会 跨越100 Bytes，请不用考虑超长字符串的情况。

示例 

输入：

    str = "abcde123abcd123"

    sub_str = "123"

输出：

    result_str = "abcdeabcd"

返回：

    2

输入：

	str = "abcde123abcd123"

	sub_str = "1234"

输出：

	result_str = "abcde123abcd123"

返回：

	0

答：

	int delete_sub_str(const char *str, const char *sub_str, char *result_str)
	{
	    int len=strlen(sub_str);//获取子串的长度
	    int cnt=0,index=0;
	    for(int t=0;t<strlen(str);++t)
	    {
	        for(int j=0;j<len;j++)
	            if(str[t+j]!=sub_str[j])
	                break;
	        if(j>=len)
	        {
	             ++cnt;
	             t=t+len-1;//删除子串
	        }
	        else
	        result_str[index++]=str[t];
	    }
	    result_str[index]='\0';
	    return cnt;
	}

三：在计算机中，由于位宽限制，只能进行有限精度的十进制整数加减法，比如在32位宽计算机中，参与运算的操作数和结果必须在-231~231-1之间。若是需要进行更大规模的十进制整数加法，需要使用特殊的方法实现，比如使用字符串保存操作数和结果，采纳逐位运算的方式进行。如下：9876543210 + 1234567890 = ?，让字符串 num1="9876543210"，字符串 num2="1234567890"，结果 保存在字符串 result = "11111111100"。-9876543210 + (-1234567890) = ?让字符串 num1="-9876543210"，字符串 num2="-1234567890"，终局保存在字符串 result = "-11111111100"。

要求编程实现上述高精度的十进制加法。

要求实现函数： 

	void add (const char *num1, const char *num2, char *result)

输入：

num1：字符串形式操作数1，若是操作数为负，则num1[0]为符号位-

num2：字符串形式操作数2，若是操作数为负，则num2[0]为符号位-

输出：result：保存加法计较终局字符串，若是终局为负，则result[0]为符号位。

当输入为正数时，+不会出今朝输入字符串中；当输入为负数时，-会出今朝输入字符串中，且必然在输入字符串最左边位置输入字符串所有位均代表有效数字，即不存在由0起头的输入字符串，比如"0012", "-0012"不会呈现；要求输出字符串所有位均为有效数字，终局为正或0时+不出今朝输出字符串，终局为负时输出字符串最左边位置为-。

答

	//只考虑同号的情况下，不同号情况类似【程序有点冗长，共同改进】
	void add (const char *num1, const char *num2, char *result)
	{
	    int len1=strlen(num1),len2=strlen(num2),flag=0;
	    if((num1[0]=='-'&&num2[0]!='-')||(num1[0]!='-'&&num2[0]=='-1'))//同为正数
	        return ;
	    const char *p1=num1+strlen(num1)-1,*p2=num2+strlen(num2)-1;
	    if(num1[0]=='-'&&num2[0]=='-')
	    {
	        num1++;
	        num2++;
	        p1=num1+strlen(num1)-1;
	        p2=num2+strlen(num2)-1;
	    }
	    int max=_cpp_max(len1,len2);
	    int index=0,carry=0;
	    for(int i=0;i<max;i++)
	    {
	        if(p1>=num1&&p2>=num2)
	        {
	            int tmp=*p1-48+*p2-48+carry;
	            if(tmp>=10)
	            {
	                result[index++]=tmp-10+48;
	                carry=1;
	            }
	            else
	            {
	                result[index++]=tmp+48;
	                carry=0;
	            }
	            p1--;
	            p2--;
	        }
	        else if(p1>=num1&&p2<num2)
	        {
	            int tmp=*p1-48+carry;
	            if(tmp>=10)
	            {
	                result[index++]=tmp-10+48;
	                carry=1;
	            }
	            else
	            {
	                result[index++]=tmp+48;
	                carry=0;
	            }
	            p1--;
	        }
	        else if(p1<num1&&p2>=num2)
	        {
	            int tmp=*p2-48+carry;
	            if(tmp>=10)
	            {
	                result[index++]=tmp-10+48;
	                carry=1;
	            }
	            else
	            {
	                result[index++]=tmp+48;
	                carry=0;
	            }
	            p2--;
	        }
	    }
	    if(*(num1-1)=='-'&&*(num2-1)=='-')
	        result[index++]='-';
	    result[index]='\0';
	    int left=strlen(result)/2;
	    if(strlen(result)%2==0)
	    {
	        left=left-1;
	        result[left]=result[left]^result[left+1];
	        result[left+1]=result[left]^result[left+1];
	        result[left]=result[left]^result[left+1];
	    }
	    for(int l=0;l<left;l++)
	    {
	        int tmp=result[l];
	        result[l]=result[strlen(result)-l-1];
	        result[strlen(result)-l-1]=tmp;
	    }
	} 