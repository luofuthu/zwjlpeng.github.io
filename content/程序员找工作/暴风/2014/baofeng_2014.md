Date: 2013-11-23
Title: 2014年暴风笔试试卷A
Category: 程序员找工作
Tags: 暴风笔试题
Slug: baofeng_2014_A
Img:pics/baofeng.jpg
summary:已知一个二叉树的先序遍历和中序遍历得到的序列为`ABDEGCFH`和`DBGEAFHC`，请;将内存中一张宽为X，高为Y的RGB32格式的图片向右旋转90度。源地址BYTE *pSrc为指向图片的首地址，目标地址BYTE *pDst为输出的目标缓冲区，备注：RGB32是一种图像格式，它用4个连续BYTE来表示一个像素，图片的存储方式为一行一样连续存：

----------
如有错误，或更加精简的方法，请留言，我会更正，以方便更多的人
暴风影音2014年A郑，据说可以解决`户口`
注:以下如无特殊说明，均假设计算机编程环境为`intel x86`的`32位CPU`,编译器为VS,编程语言首选C语言，也可以使用自已熟悉的编程语言。

1、已知一个二叉树的先序遍历和中序遍历得到的序列为`ABDEGCFH`和`DBGEAFHC`，请:

>1:根据先序遍历和中序遍历计算出该二叉树的结构图

>2:根据1的结果，计算该二叉树的后序遍历后序遍历结果

>3:完成后序遍历代码（不得使用迭代函数）

>答案如下

>1:结构图如下：

<a href="http://www.yanyulin.info/pages/2013/11/baofeng_2014_A.html">
<img src="http://www.yanyulin.info/pics/daan/bd1.jpg"/>
</a>

>2:后序遍历结果是`DGEBHFCA`

>3:代码如下：

	void postorder(BinarySearchTree T)
	{
	BinarySearchTree preNode, currNode;
	stack<BinarySearchTrees;

	preNode = NULL;
	s.push(T);
	while(!s.empty())
	{
		currNode = s.top();
		if(preNode == NULL || preNode->m_pLeft == currNode || preNode->m_pRight == currNode)
		{
			if(currNode->m_pLeft)
				s.push(currNode->m_pLeft);
			else if(currNode->m_pRight)
				s.push(currNode->m_pRight);
		}
		else if(currNode->m_pLeft == preNode)
		{
			if(currNode->m_pRight)
				s.push(currNode->m_pRight);
		}
		else
		{
			cout << currNode->m_nValue;
			s.pop();
		}
		preNode = currNode;
	}
	}

2、将内存中一张宽为X，高为Y的RGB32格式的图片向右旋转90度。源地址BYTE *pSrc为指向图片的首地址，目标地址BYTE *pDst为输出的目标缓冲区，备注：RGB32是一种图像格式，它用4个连续BYTE来表示一个像素，图片的存储方式为一行一样连续存：
<table border="1px">
<tr>
<td>
A
</td>
<td>
B
</td>
</tr>
<tr>
<td>
C
</td>
<td>
D
</td>
</tr>
</table>
如上表为宽度为2且高度为2的图像，共4个像素，在内存中存储为`A[4]B[4]C[4]D[4]`,`void rotate(BYTE *pSrc, BYTE *pDest, int X, int Y){ }`

解：此问题先考虑每个像素占一个字节的情况，然后再将问题扩展为占四个字节的情况。假设现在有8个像素，宽度为4高度为2，即

ABCD

EFGH

旋转之后变为宽度为2，高度为4,即

EA

FB

GC

HD

A[0][0]->A[0][1]

B[0][1]->B[1][1]

C[0][2]->C[2][1]

D[0][3]->D[3][1]

E[1][0]->E[0][0]

F[1][1]->F[0][1]

G[1][2]->G[0][2]

H[1][3]->H[0][3]

第0行的变为了第`(x-1)`列，其中原矩阵中的列号与旋转矩阵的行号相同，第`（x-1）`行变换为了第0行，其中原矩阵的列号与旋转矩阵的行号相同这里用i表示行，j表示列，则旋转后的`pDest[j][x-i-1] = pSrc[i][j]`，然后将其扩展为4字节问题，即赋值时要一次性复制4字节。代码如下

    typedef char BYTE;
    const int size = 4;//4字节
    void rotate(BYTE *pSrc, BYTE *pDest, int x, int y)
    {
    	for(int i = 0; i < x; i++)
    	{
    		for(int j = 0; j < y; j++)
    		{
    			int dpos = (j * x + (x - i - 1) ) * size;
    			int spos  = (i * y + j) * size;
    			for(int k = 0; k < size; k++)//每次复制4个字节
    				pDest[dpos + k] = pSrc[spos + k];
    		}
    	}
    }

3、给定字符串A和B，输出A和B中第一个最长公共子串，比如A="wepiabc"，B="pabcni"则输出“abc”

    #define MAXLEN 50
    void LCS(char *A, char *B, char *sub, int tmp[][MAXLEN])
    {
    	int i, j, max, pos, len_a, len_b;
    	len_a = strlen(A);
    	len_b = strlen(B);   	
    	max = 0;
    	pos = -1;  
    	for(i = 0; i < len_a; i++)
    	{
    		for(j = 0; j < len_b; j++)
    		{
    			if(A[i] == B[j])
    			{
    				if(i == 0 || j == 0)
    					tmp[i][j] = 0;
    				else
    					tmp[i][j] = tmp[i-1][j-1] + 1;
    				if(max < tmp[i][j])
    				{
    					max = tmp[i][j];
    					pos = i;
    				}
    			}
    		}
    	}
    	sub[max] = '\0';
    	for(i = 0; i < max; i++)
    		sub[max-i-1] = A[pos - i];
    }

4、 TCP建立连接需要几次握手过程？为什么会采用这么多次握手，请简述过程。若最后一次握手失败，会怎样处理?

解：TCP建立连接需要3次握手,过程如下图所示，第三次握手失败，服务器端处于SYN_RCVD状态，服务器端发送复位报文请求建立连接。

<a href="http://www.yanyulin.info/pages/2013/11/baofeng_2014_A.html">
<img src="http://www.yanyulin.info/pics/daan/bd2.jpg"/>
</a>

5、ClassA是一个类，那么语句ClassA a, *b[2], c[3], &d = a;执行时调用到ClassA的构造函数次数为

解:4次

6、32位系统中
    
    struct
    {
    	char buf[2];//4字节
    	int i;//4字节
    	char c;//4字节
    }sT;
请问sizeof(sT)=?多少

解:12

7、甲和乙进行打靶比赛，各打两发子弹，中靶数量最多的人获胜，甲每发子弹中弹的概率是60%，而乙每发子弹中靶的概率是30%，则比赛中乙战胜甲的可能性(`C`)

`A` 小于5%    `B` 在5%~12%之间  ` C` 在10%~15%之间    `D` 大于15%

8、请回答下列程序执行后的输出结果

	char *A = "this is a string!", *B = NULL;
	int n = 10;
	memcpy(B,A,n);
	printf(B);

解:因为B是野指针，会导致运行时错误。

9、分别指出下列操作系统是哪一种类型？（单用户单任务/单用户多任务/多用户单任务/多用户多任务）

DOS、Windows 7、Windows 2003、Linux、Unix

`DOS`：单用户单任务

`Windows 7`：多用户多任务

`Linux、Unix`：多用户多任务

`Windows 2003(Windows Server 2003)`：多用户多任务

`Windows XP`及以前`Windows`版本：单用户多任务