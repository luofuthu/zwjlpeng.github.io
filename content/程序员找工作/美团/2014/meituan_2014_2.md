Date: 2014-03-10
Title: 美团网校招笔试题2014年研发东北
Category: 程序员找工作
Tags: 美团网笔试题
Slug: meituan_2014_B
Img:pics/meituan.jpg
summary:一堆硬币，一个机器人，如果是反的就翻正，如果是正的就抛掷一次，无穷多次后，求正反的比例,概率题：一个汽车公司的产品，甲厂占`40%`，乙厂占`60%`，甲的次品率是1%，乙的次品率是2%，现在抽出一件汽车时次品，问是甲生产的可能性,100盏等，熄熄灭灭，求最后亮的,链表翻转,给出一个链表和一个数k,一个函数`access()`,调用频率不能...

----------
**如有错误，或更加精简的方法，请留言，我会更正，以方便更多的人**

1、一堆硬币，一个机器人，如果是反的就翻正，如果是正的就抛掷一次，无穷多次后，求正反的比例

解析：假设某个阶段正面硬币的比例为p，则反面的比例为1-p，下一次翻转后，p的部分分为p/2的正面、p/2的反面，而1-p的反面部分全部变为正面。趋于平衡时，前后两次正反的比例应相等，即：p/(1-p)=(p/2+(1-p))/(p/2)，得到p=2/3。

更直接一点，翻转前后正面（反面）相等，即p=p/2+(1-p)，直接得到p=2/3。

2、概率题：一个汽车公司的产品，甲厂占40%，乙厂占60%，甲的次品率是1%，乙的次品率是2%，现在抽出一件汽车时次品，问是甲生产的可能性

解：p=1/4利用贝叶斯,感谢网友指正~

3、100盏等，熄熄灭灭，求最后亮的

解：应该是相当于求1-100这100个数的因子个数，因子个数为奇数的就是亮的灯。又因为所有的数分解为两个不相同的数的时候为两个因子，因此只有平方数满足要求。共有10盏灯。
    
    1 （1）
    4（1，2，4）
    9 （1，3，9）
    16 （1，2，4，8，16）
    25
    36
    49
    64
    81
    100

4、链表翻转,给出一个链表和一个数k，比如链表1→2→3→4→5→6，k=2，则翻转后2→1→4→3→6→5，若k=3,翻转后3→2→1→6→5→4，若k=4，翻转后4→3→2→1→5→6，用程序实现. 

解:

    #include <iostream>
    using namespace std;
    
    struct ListNode
    {
    	int m_nValue;
    	ListNode *m_pNext;
    };
    
    ListNode* CreateList(int val)
    {
    	ListNode *pHead = new ListNode;
    
    	pHead->m_nValue = val;
    	pHead->m_pNext = NULL;
    
    	return pHead;
    }
    
    void InsertNode(ListNode **pHead, int val)
    {
    	ListNode *pNode = new ListNode;
    	pNode->m_nValue = val;
    	pNode->m_pNext = NULL;
    
    	while ((*pHead)->m_pNext != NULL)
    	{
    		(*pHead) = (*pHead)->m_pNext;
    	}
    
    	(*pHead)->m_pNext = pNode;
    	(*pHead) = pNode;
    }
    
    void PrintList(ListNode *pHead)
    {
    	while (pHead != NULL)
    	{
    		cout<<pHead->m_nValue<<" ";
    		pHead = pHead->m_pNext;
    	}
    	cout<<endl;
    }
    
    ListNode* Reverse(ListNode *pHead)
    {
    	if (pHead == NULL || pHead->m_pNext == NULL)
    	{
    		return pHead;
    	}
    
    	ListNode *pPre = NULL;
    	ListNode *pCurrent = pHead;
    	ListNode *pPost = pHead->m_pNext;
    
    	while (pCurrent->m_pNext != NULL)
    	{
    		pCurrent->m_pNext = pPre;
    		pPre = pCurrent;
    		pCurrent = pPost;
    		pPost = pPost->m_pNext;
    	}
    	pCurrent->m_pNext = pPre;
    
    	return pCurrent;
    }
    
    
    
    ListNode* ReverseList(ListNode *pHead, int k)
    {
    	if (pHead==NULL || pHead->m_pNext==NULL)
    	{
    		return pHead;
    	}
    
    	ListNode *pPre = NULL;
    	ListNode *pCurrent = pHead;
    	ListNode *pPost = pHead->m_pNext;
    	ListNode *pStart = NULL;
    	ListNode *pEnd = NULL;
    
    	int n = 0;
    	pEnd = pCurrent;
    	pEnd->m_pNext = NULL;
    	while (pPost != NULL)
    	{
    		++n;
    		if (n == (k+1))
    		{
    			pStart = pPre;
    			pEnd->m_pNext = ReverseList(pCurrent, k);
    
    			return pStart;
    		}
    		else
    		{
    			pCurrent->m_pNext = pPre;
    			pPre = pCurrent;
    			pCurrent = pPost;
    			pPost = pPost->m_pNext;
    		}
    	}
    
    	pCurrent->m_pNext = pPre;
    	pStart = Reverse(pCurrent);
    	return pStart;
    }
    
    int main()
    {
    	ListNode *pHead = NULL;
    	ListNode *head = NULL;
    	int n;
    	cout<<"输入链表中节点的个数 n："<<endl;
    	cin>>n;
    	cout<<"请输入n个整数值："<<endl;
    	for (int i=0; i<n; ++i)
    	{
    		int data;
    		cin>>data;
    
    		if (pHead == NULL)
    		{
    			pHead = CreateList(data);
    			head = pHead;
    		}
    		else
    		{
    			InsertNode(&pHead, data);
    		}
    	}
    
    	int k;
    	cout<<"请输入k:"<<endl;
    	cin>>k;
    	head = ReverseList(head, k);
    	PrintList(head);
    
    	system("pause");
    	return 0;
    }

5、一个函数access(),调用频率不能超过R次/sec，用程序实现一个函数，当超过R次/sec时返回access false，不超过时返回success

解：

	#define false 0
	#define success 1
	int getcurrentms()
	{
	  struct timeval tv;
	  gettimeofday(&tv,NULL);
	  return tv.tv_sec*1000+tv.tv_usec/1000; //得到毫秒数
	}
	
	bool count_access()
	{
	  static int count=0;
	  static int time_ms_old=0,time_ms_now;
	  if(count==0)
	  {
	time_ms_old=getcurrentms();
	  }
	  count++;
	  access();
	  if(count>=R)
	  {
	time_ms_now=getcurrentms();
		if(time_ms_now-time_ms_pld>=1000)
			return false;
		else
			return success;
	  }
	  return success;
	}

6、一个m*n的矩阵，从左到右从上到下都是递增的，给一个数elem，求是否在矩阵中，给出思路和代 码.

解: 思路:从矩阵的右上角开始判断即可,每次可以消除一行或一列,详见<a href="http://www.yanyulin.info/category/jing-pin-shu-ji.html" target="_blank">精品书箱</a>剑指offer一书.



**各位如果有更好的答案，请留言评价，方便更多的人**