Date: 2013-12-7
Title:微软2014年校招笔试题
Category: 程序员找工作
Tags: 微软笔试题
Slug: microsoft_2014_A
Img:pics/microsoft.png
summary:Which statement(s) is(are) `correct` about thread and process？Whichstatement below regarding TCP(Transmission Control `Protocol`) is(are) correct? Select all that apply,Initialize integer `i `as `0`, what's the value of i after the following operation?(5 Points)i += i > 0 ?。

----------
**如有错误，或更加精简的方法，请留言，我会更正，以方便更多的人**

1、Which statement(s) is(are) correct about thread and process？Select all that apply.(5 Points)

A、Threads share the same address space of the parent process;Processes share the same address space of the parent process.

B、Changes to the main thread(cancellation，priority change，etc.) may affect the behavior of the other threads of the process; Changes to the parent process does not affect child processes.

C、Multiple threads mar cause deadlock,while multiple processes won't cause deadlock.

D、Threads can directly communicate with other threads of its process; Processes must use inter-process communication to communicate with sibling processes.
E、None of the above.

2、Which statement(s) below regarding TCP(Transmission Control Protocol) is(are) correct? Select all that apply.(5 Points)

A、TCP provides a way for applications to send encapsulated IP datagrams and send them without having to establish a connection.

B、TCP supports multicasting.

C、Port numbers below 1024 are called well-known ports and are reserved for standard services. For example,port 21 is reserved for FTP protocol, and port 25 is for SMTP protocol.

D、TCP handles package loss reliably.

E、None of the above.

3、Initialize integer i as 0, what's the value of i after the following operation?(5 Points)i += i > 0 ? i++ : i --

A、-2

B、-1

C、0

D、1

E、2

4、Which of the follwing sequence(s) could not be a postorder tree walk result of a binary search tree?(5 Points)
A、1,2,3,4,5
B、3,5,1,4,2
C、1,2,5,4,3
D、5,4,3,2,1

5、When a dll is loaded into memory, which part(s) can be shared between processes?(5 Points)

A、code segment

B、static variable

C、global variable

D、external difinitions and references for linking

E、BSS segment

6、How many times is f() called when calculating f(10)?(5 Points)

    int f(int x)
    {
    	if(x <= 2)
    		return 1;
    	return f(x - 2) + f(x - 4) + 1;
    }
A、14

B、18

C、20

D、24

E、None of the above.

7、Asume you have an object to describe customer data:(5 Points)

    {
      ID（7 digit numeric）
      Family Name（string）
      Account Balance（currency）
    }

If you have 500,000 Chinese customers records represented by instances of this object type , what set of data structures is best to get fast retrieval of customers (1) get IDs from Name and (2) get Name from ID?

A、(1) Tree with Hash(100 bucket) at leaves(2) Tree with linked list at leaves.

B、(1) Tree with linked list at leaves(2) Array.

C、(1) Tree with linked list at leaves(2) Hash(10,000 buckets)

D、(1) Sort linked list(2) Array.

8、Let's assume one type of cancer may be mis-diagnosed in the examination. 5 out of 100 people with this cancer will be diagnosed as not having it , and 1 out of 100 people without this cancer will be diagnosed as having it. We know the chance of getting this cancer is around 0.1%. One person was examined and diagnosed of having this cancer, which of the following value if the closest to the chance of is really having it?(5 Points)

A、90%

B、50%

C、30%

D、10%

9、In which case(s) would you use an outer join?(5 Points)

A、The table being joined have NOT NULL columns.

B、The table being joined have only matched data.

C、The columns being joined have NULL values.

D、The table being joined have only unmatched data.

E、The table being joined have both matched and unmatched data.

10、As shown in the graph , start from node B , traverse the nodes on a Depth-First Search(DFS) algorithm , which is(are) the possible traversa sequence(s)? Select all that apply.(5 Points)

<a href="http://www.yanyulin.info/">
<img src="http://www.yanyulin.info/pics/microsoft_2014_1.jpg"/>
</a>

A、BADECF

B、BADEFC

C、BCAFDE

D、BCFDEA

E、BFDECA

11、The best time complexity of quick sort algorithm is:(5 Points)

A、O(lgn)

B、O(n)

C、O(nlgn)

D、O(n*n)

12、Which of the following method(s) CANNOT be used for Text-encryption:(5 Points)

A、MD5

B、RSA

C、RC4

D、DES

13、To speed up data access , we build cache system. In one system , The L1 cache access time is 5 ns , the L2 cache access time is 50 ns and the memory access time is 400 ns. The L1 cache miss rate is 50% , the L2 cache miss rate is 10%. The average data access time of this system is:(5 Points)

A、5

B、30

C、45

D、50

E、55

14、Which is(are) valid function pointer declaration(s) below ? Select all that apply.(5 Points)

A、void* f(int);

B、int (*f)();

C、void (*f(int , void(*)(int)))(int);

D、void (*(*f)(int))();

15、Which of the following method(s) could be used to optimize the speed of a program ? (5 Points)

A、Improve memory access pattern to decrease cache misses.

B、Use special instructions(e.g. vector instructions) to replace compiler generated assembly code.

C、Change an algorithm from recursive implementation to iterative implementation.

D、Loop unwinding.

16、Which regular expression(s) matches the sentence "www.microsoft.com" ? (5 Points)

A、^\w+\.\w+\.\w+$

B、[w]{0,3}.[a-z]*.[a-z]+

C、.[c-w.]{3,10}[.][c-w.][.][a]|.+

D、[w][w][w][microsoft]+[com]+

E、\w*

17、In the image below , if the function is designed to multiply two positive numbers which line number in the image contains the biggest functional bug(assume no overflow)? (5 Points)

    int Fun(int A, int B)
    {
    	int C=0;
    	for (int i=0;i<B;++i)
    	{
    	C+=C;
    	}
    	return C;
	}

A、Line 1

B、Line 2

C、Line 3

D、Line 4

E、Line 5

18、Which of the following can be referred to as attack method(s)? Select all that apply.(5 Points)

A、Vulnerability scan

B、SQL Injection

C、Drive-by downloading

D、Brute force

19、A table CANNOT have one or more of the following index configurations.(5 Points)

A、No indexes

B、A clustered index

C、clustered index and many non-clustered indexes

D、Many clustered index

20、Which of the following is(are) true about providing security to database servers ? Select all that apply.(5 Points)

A、Do not host a database server on the same server as your web server

B、Do not host a database server on a server based system

C、Do not use blank password for SA account

D、Employ a centralized administration model

第二部分测试时间为60分钟，满分50分。请务必在回答问题前仔细阅读变成题目。您可以选用C、C++、C#或者Java 其中任何一种编程语言，并且保证您的代码可以正确编译和有正确的结果。另外，请一定要注意您的代码的质量。

21、Given a singly linked list L: (L0 , L1 , L2...Ln-1 , Ln). Write a program to reorder it so that it becomes(L0 , Ln , L1 , Ln-1 , L2 , Ln-2...).

    struct Node
    {
    	int val_;
    	Node* next;
    };

Notes:

1、Space Complexity should be O(1) 

2、Only the ".next" field of a node is modifiable.

**各位如果有更好的答案，请留言评价，方便更多的人**