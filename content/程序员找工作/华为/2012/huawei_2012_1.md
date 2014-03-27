Date: 2012-11-11
Title: 2012年华为成都校招机试
Category: 程序员找工作
Tags: 华为笔试题
Slug: huawei_2012_1
Img:pics/huawei.jpg
summary:去掉一个数组里的最大值与最小值，求数组元素的平均值,对一个`数组`，将数组中偶数从大到小排序，奇数从小到大排序,奇数和偶数交叉着放且输出数组第一位放奇数  若奇数和偶数不等长，则把剩下的直接放到数组中,本题思路先对数组无论奇偶排一下序，数组变成有序后，此时奇数是从小到大排序，偶数也是从小到大...

1：去掉一个数组里的最大值与最小值，求数组元素的平均值。

函数接口为：

	float avescore(float score[] ,int n)

答：

    /*解析：此题比较简单，循环一遍，记下数组的最大值与最小值以及总和，然后在求的总和里面减掉最大值与最小值，再求平均数即可，时间复杂度为O(n),代码不多，如下：*/
    float avescore(float score[] ,int n)
    {
    	float max=0,min=score[0],sum=0;
    	for(int i=0;i<n;i++)
    	{
    		sum+=score[i];
    		max=max<score[i]?score[i]:max;
    		min=min>score[i]?score[i]:min;
    	}
    	return (sum-max-min)/(n-2);
    }


2: 对一个数组，将数组中偶数从大到小排序，奇数从小到大排序,奇数和偶数交叉着放且输出数组第一位放奇

数  若奇数和偶数不等长，则把剩下的直接放到数组中。

函数接口为：
	void sortArray(int a[],int n)

解析

>本题思路先对数组无论奇偶排一下序，数组变成有序后，此时奇数是从小到大排序，偶数也是从小到大

>排序的，假设排序好的数组为

>2 1 6 8 9 

>然后再循环一次，在循环中如下处理

>按题意要求奇数打头故执行如下

>第一次执行

>序列变成 1 2 6 8 9

>第二次执行1 8 6 2 9

>第三次执行 1 8 9 2 6

>第四次执行 1 8 9 6 2

>第五次执行 18 9 6 2 

>由上序执行可以看出思路了吧，时间复杂度可能有点高，介于`O(n)-O(n^2)`

答
    
    /*解析，本题思路先遍历一遍数组，得出数组中的奇数个数与偶数个数，根据奇偶个数分别开辟空间
    再使用泛型算法对两个数组进行排序，奇数数组根据题意应该从小到大排序，偶数数组应是从大到小
    进行排序，再将排好序的数组根据题意要求重新赋值到原数里里
    算法的空间复杂度O(n),不是很好的一个算法*/
    #include<iostream>
    #include<algorithm>
    using namespace std;
    int cmpG( const void *a , const void *b ) 
    { 
    	return *(int *)a - *(int *)b; 
    }
    int cmpL( const void *a , const void *b ) 
    { 
    	return *(int *)b - *(int *)a; 
    }
    void sortArray(int score[] ,int n)
    {
    	int maxO=0,maxE=0,oIndex=0,eIndex=0;
    	int *od=0,*ev=0;
    	for(int i=0;i<n;i++)
    		score[i]%2==0?++maxE:++maxO;
    	od=new int[maxO];
    	ev=new int[maxE];
    	for(int j=0;j<n;j++)
    		score[j]%2==0?ev[eIndex++]=score[j]:od[oIndex++]=score[j];
    	qsort(od,maxO,sizeof(int),cmpG);
    	qsort(ev,maxE,sizeof(int),cmpL);
    	oIndex=eIndex=0;
    	for(int k=0;k<n;k++)
    		if((k%2==0&&oIndex<maxO)||(k%2!=0&&eIndex>=maxE))
    			score[k]=od[oIndex++];
    		else if((k%2!=0&&eIndex<maxE)||(k%2==0&&oIndex>=maxO))
    			score[k]=ev[eIndex++];
    	free(od);
    	free(ev);
    }
