Date: 2014-03-08
Title: 人人网校招笔试题2014年软件研发类
Category: 程序员找工作
Tags: 人人网笔试题
Slug: renren_2014_A
Img:pics/renren.jpg
summary:给定一个有序数组a,长度为`len`,和一个数X,判断A数组里面是否存在两个数，他们的和为`X`,给定有n个数的数组a,其中超过一半的数为一个定值，在不进行排序的情况下，不开设额外数组的情况下，以最高效的算法找出这个数,人人网最近在研发一个攒人口的新功能，用于回馈长期支持人人网的用户，人品值标识着用户在人人网的尊贵程序...

----------

技术类笔试题

1、给定一个有序数组a,长度为len,和一个数X,判断A数组里面是否存在两个数，他们的和为X

    bool judge(int *a ,int len, int x)

存在的话反回true,不存在的话返回false

参考答案：

解题思路：`hash table`

时间复杂度：`O(N)`

空间复杂度：`O(N)`

    #include <iostream>
    
    using namespace std;
    
    int hash_table[100];
    
    bool judge(int *a, int len, int x)
    {
    	memset(hash_table, 0, sizeof(hash_table));
    	for (int i=0; i<len; ++i)
    	{
    		hash_table[x - a[i]] = 1;
    	}
    
    	for (int i=0; i<len; ++i)
    	{
    		if (hash_table[i] == 1)
    		{
    			return true;
    		}
    	}
    
    	return false;
    }
    
    int main()
    {
    	int len = 10;
    	int a[10] = {1, 3, 5, 7, 9, 4, 2, 8, 10, 6};
    	int x = 19;
    
    	if (judge(a, len, x))
    	{
    		cout<<"Yes"<<endl;
    	}
    	else
    	{
    		cout<<"No"<<endl;
    	}
    	system("pause");
    	return 0;
    }


2、给定有n个数的数组a,其中超过一半的数为一个定值，在不进行排序的情况下，不开设额外数组的情况下，以最高效的算法找出这个数

    int find(int *a, int n)

参考答案：

时间复杂度为O(n)

空间复杂度为O(1)

    #include <iostream>
    
    using namespace std;
    
    int find(int *a, int n)
    {
    	int t = a[0];
    	int count = 0;
    	for (int i=0; i<n; ++i)
    	{
    		if (count == 0)
    		{
    			t = a[i];
    			count = 1;
    			continue;
    		}
    		else
    		{
    			if (a[i] == t)
    			{
    				count++;
    			}
    			else
    			{
    				count--;
    			}
    		}
    	}
    
    	return t;
    }
    
    int main()
    {
    	int n = 10;
    	int a[10] = {1, 3, 2, 3, 3, 4, 3, 3, 3, 6};
    
    	cout<<find(a, n)<<endl;
    
    	system("pause");
    	return 0;
    }
    
3、人人网最近在研发一个攒人口的新功能，用于回馈长期支持人人网的用户，人品值标识着用户在人人网的尊贵程序，除此之外它还有一个更经济的功能，第一个获得100万人品值的用户将获得一份人人网的实物大奖，攒人品的规则是这样的，人人网首先会给每个老用户发放一个【自动攒人品的手】，每秒种可以自动获得1点人品（且人品值是随着时间连续获得的，即每0.5秒就会获得0.5点人品值）。人品值可以用来兑换各种各样的加速攒人品的道具，道具列表及价如如下：

<center>
<a href="http://www.yanyulin.info/pages/2014/03/renren_2014_A.html" target="_blank">
<img src="http://www.yanyulin.info/pics/job/renren0.jpg" alt="烟雨林博客"/>
</a>
</center>

a)如果每一种道具可购买无限多次，效果叠加，作为人人网的一名老用户且有钻研精神的你，对这场人品竞赛是志在必得，因此在功能上线前提前想好了最佳方案以便确保成位第一位获得100万人品的用户，请给最快攒到100万人品的策略

b)如果每一种道具可购买无限多次，效果叠加，但每一次购买后该道具会成原来价格的1.2倍，请给出最快攒到100万人品的策略

参考值：

`log(1000000)=75.78` 备注log底数为1.2

`log(7000)=45.56` 备注log底数为1.2

`log(2000)=41.69` 备注log底数为1.2

`log(500)=34.09` 备注log底数为1.2

`log(100)=25.26` 备注log底数为1.2