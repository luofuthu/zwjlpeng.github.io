Date: 2013-06-11
Title: 2013年华为校招机试(一)
Category: 程序员找工作
Tags: 华为
Slug: huawei_2013_1
Img:pics/huawei.jpg
summary:通过键盘输入任意一个字符串序列，字符串可能包含多个子串，子串以空格分隔，请编写一个程序，自动分离出各个子串，并使用’,’将其分隔，并且在最后也补充一个’,’，并将子串存储;将一个字符串中出现次数最少的字符删掉，并保证删除后的字符顺序不变，如果出现次数最少的字符有多种，则这几种字符都要删除，该字符串长度不会超过20个字符。

----------
通过键盘输入任意一个字符串序列，字符串可能包含多个子串，子串以空格分隔，请编写一个程序，自动分离出各个子串，并使用’,’将其分隔，并且在最后也补充一个’,’，并将子串存储。

如果输入`”abc def ghi d”`,结果将是`abc,def,gh,i,d`

要求实现函数`Void DivideString(const char *pInputStr,long IinputLen,char *pOutputStr);`

输入：

`pInputStr`:输入字符串

`IinputLen`:输入字符串的长度

输出：

`pOutputStr`:输出字符串，字符串已开辟好，与输入字符串等长

注意：只需要完成该函数功能算法，中间不需要有任何IO的输入输出

解，首先去掉字符串前面开始的空格，然后遍历字符串，遇到空格时，将标志设为真，先不处理，等下次时循环时，若标志为真，则在字符前加一,号即可

    void DivideString(const char *pInputStr,long IinputLen, char *OutputStr)
    {
    int cnt=0,i=0;//计数
    bool flag=false;
    while(pInputStr[i]==' ')//去掉前面的空格
    i++;
    for(;i<IinputLen;i++)
    {
    if(pInputStr[i]==' ')
    {
    flag=true;
    continue;
    }
    if(flag)//如果flag为true,说明有空格，则将空格变成了, 
    {
    flag=!flag;
    OutputStr[cnt++]=',';
    }
    OutputStr[cnt++]=pInputStr[i];
    }
    OutputStr[cnt]='\0';
    }
二:将一个字符串中出现次数最少的字符删掉，并保证删除后的字符顺序不变，如果出现次数最少的字符有多种，则这几种字符都要删除，该字符串长度不会超过20个字符。 例如：源字符串为`“abcdd”`，删除后为`“dd”`

解：此题主要是内存移位操作

    char *deleteMin(char *InputSrc,int ILen)
    {
    int sz[26]={0};
    int min=20,i;//最小出现次数
    for(i=0;i<ILen;i++)
    ++sz[InputSrc[i]-'a'];
    for(i=0;i<26;i++)
    if(sz[i]<min&&sz[i]!=0)
    min=sz[i];
    for(int t=0;*(InputSrc+t);++t)
    if(sz[InputSrc[t]-'a']==min)
    {
    memcpy(InputSrc+t,InputSrc+t+1,ILen-t);
    --t;//因为跳过了一位
    }
    return InputSrc;
    }