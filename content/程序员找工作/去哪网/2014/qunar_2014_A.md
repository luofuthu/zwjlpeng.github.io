Date: 2014-03-08
Title:去哪儿网校招笔试题2014年软研|测试|前端
Category: 程序员找工作
Tags: 去哪网笔试题
Slug: qunar_2014_A
Img:pics/qunar.jpg
summary:写一个函数，转换相对路径为绝对路径,题目的大概意思就是要求写出一个`strcpy`函数，用于字符串的复制,题目的大概意思就是在海量数据中，如何求出前100个最小的数，大概就是这样的，解决方法是用堆,、一个10*10的矩阵（可以理解为棋盘），随时生成一组数据填入矩阵,数据库有考试成绩表scg,包含属性,分数少于60的学号和科目，要求...


----------

一、编程题

1、写一个函数，转换相对路径为绝对路径，例如输入路径为`/home/abs/../temp/new/../`，输出路径为：`/home/temp`

2、题目的大概意思就是要求写出一个strcpy函数，用于字符串的复制

3、题目的大概意思就是在海量数据中，如何求出前100个最小的数，大概就是这样的，解决方法是用堆

4、一个10*10的矩阵（可以理解为棋盘），随时生成一组数据填入矩阵，任何一个位置的数字，除4进行计算，按照余数进行着色，余数为0着色为red，1为blue，2为green，3为black，可以理解为生成4种颜色的棋子放入棋盘，如果存在其中同色五星连珠的情况（规则通五子棋），找出任意一组，输出5个棋子的位置下标值


5、数据库有考试成绩表scg,包含属性：

存储ID 学号(sno) 科目(cno) 分数(grade)

1 s001 c01 90

2 s001 c02 72

3 s002 c01 95

...

写SQL,求：

a)分数少于60的学号和科目，要求有:学号、科目、分数

b)超过2科分数>=90的人的学号和科目数，按科目数由大到小排序，要求有：学号、科目数(>=90分)

c)每个人成绩最好的三个科目，按学号、分数排序，要求有：学号、科目、分数

d)每科目，前2名的分数差:科目、第一名学号、第二名学号、第一分数、第二分数、分数差

当数据来源为文本文件(tab分割)时，写程序求上题b/c/d,程序语言不限(shell/python/java等均可，或者使用伪代码描述计算步骤

参考答案如下：

a) 

    SELECT sno, cno, grade
    FROM scg
    WHERE grade < 60;
    

b)

    SELECT sno, COUNT(cno)
    FROM scg
    WHERE grade>=90
    GROUP BY sno HAVING COUNT(cno)>2
    ORDER BY COUNT(cno) DESC;

c)
    
    SELECT TOP 3 sno, cno, grade  
    FROM scg
    GROUP BY sno
    ORDER BY sno, grade;

d)
    
    SELECT cno, first.sno, second.sno, first.grade, second.grade, first.grade-second.grade
    FROM 
    ( 
    SELECT TOP 1 * 
    FROM scg 
    GROUP BY cno 
    ORDER BY grade
    ) first,
      (
    SELECT TOP 1 *
    FROM
    ( SELECT TOP 2 * 
    FROM scg
    GROUP BY cno
    ORDER BY grade DESC
    ) two
    GROUP BY two.cno
    ORDER BY two.grade
    ) second
    ;

**欢迎大家将答案粘贴在后面的评论框里，我会选出最好的答案作为本题的标准答案，以方便更多的师弟师妹们**

到此为止