# 写在最前面

大一是其他专业的，根本不知道有西二在线，转完专业自以为天下无敌，大一下爽玩半年，最后差点暴毙。所以决定发奋图强，毕竟再不学点什么就晚了，这也算是我最后的机会。虽然和大家一样是参加考核的，但是毕竟大二的老东西，稍微有点基础，所以写个笔记打个样，希望能给后来者一点点小小的帮助。先说一句，本人是蒟蒻，如果本文档出现任何错误或者写的不清楚的地方，请指出并且狠狠拷打我。但是小蒟蒻也有一颗成为大佬的心，写这篇其实主要目的之一是希望能帮到后人，还有一点就是激励自己能更新下去，也算是梳理一下自己学到的知识，一篇看起来不像笔记的笔记罢了（）

不过没有特地传播，也不会有人看见吧，希望（）

---- 2024.9.10, 22: 00

联系方式：
QQ：1813469946

# 环境

- 魔法：不提供
- IDE：vscode/pycharm社区版
- Conda安装
- 使用Conda配置虚拟环境？是为了避免依赖冲突。
==所以什么是Jupyter...==
# Python基础

暂略
## 重点复习的东西

- 数据结构List，Dict的使用
- Lambda匿名函数
- Decorator装饰器
- 类Class的使用，Magic Methods的使用
- re正则表达式的使用
- 列表推导式

毕竟要考，而且我也不大熟练，知识堪堪写过一遍而已



# CS61A

## 学习建议

CS61A这门课适合有一定基础的人听，不然很劝退，国外教材经典地和国内教材不一样，而且质量也差的比较多，比方说Java经典入门教程MIT 6.092，人家MIT设置的14个小时学完java，从基本语法到面向对象，课程+lab，国内可能得用一整年的时间（说的就是你，fzu！）。

本人从8月末开始准备考核，先花了五天的时间速通了一下python的语法，做完了原来考核的题目（除了正则表达式），后面就去稍微看了点爬虫和numpy库，由于数模比赛耽搁了一周多的时间，现在重新上github上看，发现考核内容较先前改变了不少，比如我上学期稍微看了点的神课cs61a，只不过上学期因为摆大烂没坚持下来（蒟蒻的证明），希望写这个文档之后能坚持下去吧（）
## 关于如何unlock作业

windows端在终端运行时使用`python ok --q question_name -u --local`，而非伯努利提供的`python3 ok -q short-circuit -u`

注意：
- python3改为python
- 由于我们无法使用伯努利账号，所以增加--local是必要的
- 由于是local测试，所以你写的代码不一定完全正确但是通过了

## 学习资料
- https://www.bilibili.com/video/BV1GK411Q7qp/?vd_source=0272bb7dd0d8d9302c55fc082442b9e3 （2022Fall）
- 课本链接：https://composingprograms.netlify.app/
- lab
- chatgpt
## Note

直接听lecture就行了，其他的有兴趣可以听，有基础的也可以直接啃书，不过难度比较大就是了。只需要注意L1从35min开始听，前面的是国内外课程特有的成绩计算环节（对于初听国外网课的人来说......不敢跳过啊！）

本人有点基础，上学期听了几个lc，开学第一周速通了一下python语法，所以就直接上课本和lab了。

### lab00

lab00链接：https://web.archive.org/web/20220811203413/https://cs61a.org/lab/sol-lab00/

先开个终端，cd到当前目录，每个lab都得先解锁之后，即`-q`之后才能做题目，直接输入`python ok --q python-basics -u --local`，来做解锁lab00的题目。

lab00的解锁题目不难，在此就不多写了，然后解锁了lab00之后是lab00的题目，打开lab00.py，显示代码如下：

```
def twenty_twenty_four():  
    """Come up with the most creative expression that evaluates to 2024  
    using only numbers and the +, *, and - operators.  
    >>> twenty_twenty_four()  
    2024    
    """    
    return ____
```

看`>>> twenty_twenty_four() `，显然在调用该函数的时候返回的是`2024`，所以直接把`____`改成`2024`如下，保存退出。

```
def twenty_twenty_four():  
    """Come up with the most creative expression that evaluates to 2024  
    using only numbers and the +, *, and - operators.  
    >>> twenty_twenty_four()  
    2024    
    """    
    return 2024
```

打开终端，输入`python ok --local`，然后得出如下结果：

```
=====================================================================
Assignment: Lab 0
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    2 test cases passed! No cases failed.
```

恭喜你也恭喜我，lab00完成了

~~以前有做过lab00的就是不一样~~
### 第一章：使用函数构建抽象

到了lab01，就开始有点难了，先看课本再说。

#### 1.开始

虽然课本里没写，但是我还是建议你在你的IDE里输入一串代码：

```
import this
```

然后运行它，会出现如下的语句：

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

送给自己，也送给竟然能看到我这篇文档的人。

然后就是经典的，每个程序员都要做的事情：

```
print("Hello World!")
```

```
Hello World!
```

不妨也试试

```
print("Hello, I'm ShaddockNH3")  
print('I don\'t like study!',end=' ')  
print("I love sleeping!")
```

国内的教程肯定就直接开始跟你讲什么转义字符，什么python里单引号双引号一个意思，然后就是经典编程八股，从print到input，到if，else，while，for，再到list之类种种，可能一学期就结束了。但是CS61A就不一样了，甚至不跟你讲input，直接给你给你上强度，第一章里就直接上各种高阶应用，什么装饰器啊，lambda啊，推导式啊......

不说啥了，直接开始下一节。

#### 1.2 编程要素

其他没什么好说的，主要说一下纯函数和非纯函数

- 纯函数
 即有一些输入并返回一些东西，课本里写的是绝对值函数abs()，代码如下：

```
a=abs(-1)  
print(a)
print(abs(-1))
```

输出结果为

```
1
1
```

- 非纯函数
即有一些输入并返回一些东西，然后产生一些“副作用”，比如print()函数，print()函数的返回值是None，然后“副作用”是输出里面的某些东西，代码如下

```
print(1)
print(print(1))
```

输出结果为

```
1
1
None
```

很多人看到这里一下不理解，~~包括本蒟蒻~~，为什么print()函数也要设置返回值，我自己的理解是因为这是一种一致性，任何函数都要返回点什么东西，要记住print()函数打印的功能知识print()函数的副产物，而不是它的返回值

课本到这里就结束了，看的云里雾里的，也不知道课本到底讲了啥，我也不知道，不过补充几点东西

1. print()函数默认带换行符，如果想要自定义，则用我上文中1.1提及的方式可以自定义
2. 在print()函数中，"," 在二者间加入空格的意思
3. 

#### 1.3 定义新的函数

首先需要说明的是，课本里用的是交互式的东西，我很不喜欢，毕竟刚上手的是C/C++，和python差距还是蛮大的，所以这里尽量都不使用交互式的方式

课本里举得第一个例子是平方函数，~~我经常拼错square~~，直接上函数，和国内教材就有很大不同，c primer plus里也是直接上的函数，甚至先讲的循环再讲的if，else语句。不必多说，直接上例子

```
def square(x):  
    return x*x  
a=square(4)  
print(a)
```

输出为`16`

那么到这里，不免手痒，想自己试试输入某个值，检验一下自己写的函数，除了交互式的方式之外，那么肯定就是输入。

不妨先试试以下代码，未来再解释：

```
def square(x):  
    return x * x  
  
while True:  
    a = input()  
    if a == 'q':  
        break  
    if a.isdigit():  
        print(square(int(a)))  
    else:  
        print("请输入一个整数数字！")
```

上述代码的功能是输入整数并且打印平方，直到输入的是q，结束

不过上面的代码仍然有点问题，只能处理非带有小数的情况，在此按下不表，以后一起解释

接下来就是函数调用函数的例子，比如说我想求两个数的平方和：

```
def square(x):  
    return x * x  
  
def sum_square(x,y):  
    return square(x)+square(y)  
  
print(sum_square(1,2))
```

输出：

```
5
```

我们不妨试试把两个函数的位子调换一下：

```
def sum_square(x,y):  
    return square(x)+square(y)  
  
def square(x):  
    return x * x  
  
print(sum_square(1,2))
```

输出：

```
5
```

学过c/c++的人可能有点懵，为啥调换了函数位子之后还能正常运行呢？

因为python是解释性语言，意味着代码是按照顺序逐行解释和执行的，而不是像C/C++那样子先预编译所有的函数声明

在python中，我们还可以使用函数来定义函数，比如说这样：

```
def square(x):  
    return x*x  
  
g=square  
  
print(g(5))
```

输出：

```
5
```

可见“动态绑定”两个字的含金量，如果把代码向下写：

```
def square(x):  
    return x*x  
  
g=square  
  
print(g(5))  
  
g=5  
  
print(g)
```

输出：

```
25
5
```

g竟然从一个函数变成了一个数！

原因是因为python的绑定是一种动态绑定，变量可以动态地绑定不同类型对象的

接下来就是这本书很逆天也是比较难理解的东西了，环境：

~~就写到这里，剩下明天再更新，争取明天一天更完lab01，lab01我自己也还没做过~~

~~比较难绷，可能好多东西落下了；另外github上传仓库给我研究半天，最后发现公钥配成私钥了，昨天加今天加在一起估计搞了一个多小时才上传成功（）~~

接下来接着看环境，求解表达式的环境由帧构成，全局帧只有一个，每个函数都有自己的局部帧。课本里的那个例子或许还不够清晰，参见如下代码：

```
x=10  
  
def square(x):  
    print("x in square =",x)  
    return x*x  
  
a=square(3)  
  
print("x in global =",x)  
print("a in global =",a)
```

输出如下：

```
x in square = 3
x in global = 10
a in global = 9
```

可见函数square()内的x与全局环境中的x不是一个x，可以把函数内部的x理解为一个变量，只是一个==代指==罢了，与全局环境中的x没有多大关系。用专业点的话来说就是实现者为函数的形参选择的名称不应该影响函数行为，如果我把square函数中的所有x都改成y，一样不影响函数的作用

下面就提到了抽象的概念（面向对象的东西）

抽象函数，即用户不需要知道函数的内部实现是什么，知道这个函数是干啥的就行了。举个很简单的例子，我不需要知道计算机的内部构造，但是我依旧能很轻松地在上面~~玩各种奇怪的act小游戏，比如说alice in cradle~~一样，难道玩个小h油就需要知道计算机是怎么由一大堆奇怪的部件组成的吗？显然不需要 ，我只需要知道怎么打开电脑，找到网站，然后下载爽玩就行了。

就好像课本里讲的例子一样，我不关心计算机内部是怎么实现的，我只关心结果，无论黑猫白猫，能抓到老鼠的就是好猫（暂不考虑效率）

```
def square1(x):  
    return x*x  
  
def square2(x):  
    return x*(x+1)-x  
  
print(square1(4))  
print(square2(4))
```

二者输出完全一致

其他先略，有时间再来细看
#### 1.4 设计函数

先引用一下课本的话，扔在这里先

- 不要重复自己（Don't repeat yourself）是软件工程的核心原则。这个所谓的 DRY 原则指出，多个代码片段不应该描述重复的逻辑。相反，逻辑应该只实现一次，为其指定一个名称后多次使用。如果你发现自己正在复制粘贴一段代码，那么你可能已经找到了进行函数抽象的机会。

课本里先讲了文档：

```
def square(x):  
    '''  
    计算平方  
    '''    return x*x  
  
help(square)
```

```
Help on function square in module __main__:

square(x)
    计算平方
```

补充一下注释：
```
'''
在python中，由两对三个单引号内部的是注释
可以跨行
'''

#我也是注释，但是我不能跨行

```

注释会自动被解释器忽略，这是给人类看的东西，就好像先前说的抽象一样，在实现完了某个函数之后，我们只需要知道它是干啥的，不需要知道它的内部是如何实现的，具体的实现可以忘掉了，不过为了维护，我们还是要给里面的步骤写注释，免得几周后发现代码内部实现地有问题，又得从头开始理解

接下来举个例子，关于计算立方体体积的

```
def V(a,b,c):  
    return a*b*c  
def V1(a,b,c=1):  
    return a*b*c  
'''  
def V2(a,b=3,c):  
    return a*b*c#错误实现  
'''  
  
def V3(a,b=2,c=3):  
    return a*b*c  
  
print(V(4,5,6))  
print(V1(4,5,6))  
print(V3(4,5,6))  
print(V1(4,5))  
print(V3(4,5))  
print(V3(4))
```

```
120
120
120
20
60
24
```

python自己携带的函数，request库numpy库内的函数等很多都有默认值，比如说，，，

#### 1.5 控制

终于到了if，else和while了，~~先上个体育课先~~，前面其实有很多东西讲的 不是很清楚，我的评价是还是自己理解的不够深

看了一遍1.5，感觉对于有基础的来说没啥好讲的，接着就是灾难一般的1.6

#### lab01

不多说了，直接上lab01

下载地址：https://web.archive.org/web/20220924154230/https://cs61a.org/lab/sol-lab01/

和lab00一样，先做解锁题目，输入`python ok -q control -u --local`开始答题Q2

```
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Control > Suite 1 > Case 1
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Control > Suite 1 > Case 2
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     if x > 0:
...         print('positive')
...     else:
...         print(0)
>>> how_big(7)  # Be careful with quotation marks!
'big'
>>> print(how_big(7))  # Be careful with quotation marks!
big
>>> how_big(12)
huge
positive
>>> print(how_big(12))
(line 1)? huge
(line 2)? positive
(line 3)? None
-- OK! --

>>> print(how_big(1), how_big(0))
(line 1)? positive
(line 2)? 0
(line 3)? None None
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> n = 3
>>> while n >= 0:  # If this loops forever, just type Infinite Loop
...     n -= 1
...     print(n)
(line 1)? 2
(line 2)? 1
(line 3)? 0
(line 4)? -1
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> negative = -12
>>> while negative: # If this loops forever, just type Infinite Loop
...    if negative + 6:
...        print(negative)
...    negative += 3
(line 1)? 6
-- Not quite. Try again! --

(line 1)? -12
(line 2)? -9
(line 3)? -3
-- OK! --

---------------------------------------------------------------------
OK! All cases for Control unlocked.

Cannot backup when running ok with --local.
```

Q3`python ok -q short-circuit -u --local`

有点难绷，伯努利好像取消了这个，那么下一个

Q4`python ok -q debugging-quiz -u --local`

```
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 1
(cases remaining: 7)

Q: In the following traceback, what is the most recent function call?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) g(x + x, x)
1) h(x + y * 5)
2) f("hi")
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) g(x + x, x)
1) h(x + y * 5)
2) f("hi")
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 2
(cases remaining: 6)

Q: In the following traceback, what is the cause of this error?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) there was a missing return statement
1) the code attempted to add a string to an integer
2) the code looped infinitely
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 3
(cases remaining: 5)

Q: How do you write a doctest asserting that square(2) == 4?
Choose the number of the correct choice:
0) def square(x):
       '''
       square(2)
       4
       '''
       return x * x
1) def square(x):
       '''
       doctest: (2, 4)
       '''
       return x * x
2) def square(x):
       '''
       input: 2
       output: 4
       '''
       return x * x
3) def square(x):
       '''
       >>> square(2)
       4
       '''
       return x * x
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 4
(cases remaining: 4)

Q: When should you use print statements?
Choose the number of the correct choice:
0) To ensure that certain conditions are true at certain points in your code
1) To investigate the values of variables at certain points in your code
2) For permanant debugging so you can have long term confidence in your code
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 5
(cases remaining: 3)

Q: How do you prevent the ok autograder from interpreting print statements as output?
Choose the number of the correct choice:
0) Print with 'DEBUG:' at the front of the outputted line
1) Print with # at the front of the outputted line
2) You don't need to do anything, ok only looks at returned values, not printed values
? 0
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 6
(cases remaining: 2)

Q: What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 -i lab01.py
1) python3 ok -q sum_digits --trace
2) python3 ok -q sum_digits
3) python3 ok -q sum_digits -i
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 7
(cases remaining: 1)

Q: Which of the following is NOT true?
Choose the number of the correct choice:
0) It is generally good practice to release code with assertion statements left in
1) Debugging is not a substitute for testing
2) It is generally bad practice to release code with debugging print statements left in
3) Testing is very important to ensure robust code
4) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) It is generally good practice to release code with assertion statements left in
1) Debugging is not a substitute for testing
2) It is generally bad practice to release code with debugging print statements left in
3) Testing is very important to ensure robust code
4) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
? 4
-- OK! --

---------------------------------------------------------------------
OK! All cases for debugging-quiz unlocked.

Cannot backup when running ok with --local.
```

last的意思是最新，substitue意思是代替，最后一个的1）理解成debugging对测试来说不好了，难绷，英语不好导致的

继续就是写代码了......

Q5

```
def falling(n, k):  
    """Compute the falling factorial of n to depth k.  
  
    >>> falling(6, 3)  # 6 * 5 * 4  
    120    >>> falling(4, 3)  # 4 * 3 * 2  
    24    >>> falling(4, 1)  # 4  
    4    >>> falling(4, 0)  
    1    """    sum,i=1,1  
    while i<=k:  
        sum,n,i=sum*n,n-1,i+1  
    return sum
```

测试：`python ok -q falling --local`

```
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

继续Q6

```
def sum_digits(y):  
    """Sum all the digits of y.  
  
    >>> sum_digits(10) # 1 + 0 = 1  
    1    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12  
    12    >>> sum_digits(1234567890)  
    45    >>> a = sum_digits(123) # make sure that you are using return rather than print    >>> a  
    6    """    sum=0  
    while y/10!=0:  
        sum+=y%10  
        y//=10  
    return sum
```

`python ok -q sum_digits --local `

```
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

弱弱地说一句，感觉比以前的lab01：hog简单多了啊！

Q7

`python ok -q if-statements -u --local`

```
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What If? > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
(line 1)? 10
(line 2)? foo
-- OK! --

---------------------------------------------------------------------
What If? > Suite 1 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def bake(cake, make):
...    if cake == 0:
...        cake = cake + 1
...        print(cake)
...    if cake == 1:
...        print(make)
...    else:
...        return cake
...    return make
>>> bake(0, 29)
(line 1)? 1
(line 2)? 29
(line 3)?
-- Not quite. Try again! --

(line 1)? 1
(line 2)? 29
(line 3)? 29
-- OK! --

>>> bake(1, "mashed potatoes")
(line 1)? mashed potatoes
(line 2)? mashed potatoes
-- Not quite. Try again! --

(line 1)? mashed potatoes
(line 2)? "mashed potatoes"
-- OK! --

---------------------------------------------------------------------
OK! All cases for What If? unlocked.

Cannot backup when running ok with --local.
```

最后那个mashed potatoes还一下没反应过来，继续

Q8

`python ok -q double_eights --local`

```
def double_eights(n):  
    """Return true if n has two eights in a row.  
    >>> double_eights(8)  
    False    >>> double_eights(88)  
    True    >>> double_eights(2882)  
    True    >>> double_eights(880088)  
    True    >>> double_eights(12345)  
    False    >>> double_eights(80808080)  
    False    """  
    num = n % 10  
    if num == 8:  
        a = True  
    else:  
        a = False  
    n //= 10  
  
    while n > 0:  
        if n % 10 == 8 and a == True:  
            return True  
        elif n % 10 == 8:  
            a = True  
        else:  
            a = False  
        n //= 10  
  
    return False
```

逻辑有点乱

```
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

lab01结束，总体评价很简单，比以前的hog简单多了（）

这里看到1.5就能写了，感觉就是一些很基础很基础的语法的应用和理解

#### 1.6 高阶函数

##### 1.6.1 作为参数的函数

函数也可以作为参数，还记得前文所说的，只要有重复代码就可以被抽象出来的话吗？

课本里的三个例子就很好地描述了这样的情况，我们都要求ki从1到100的和，只是ki不一样罢了。

```
def sum_nature(n):  
    sum,k=0,1  
    while k<=n:  
        sum,k=sum+k,k+1  
    return sum  
  
def sum_square(n):  
    sum,k=0,1  
    while k<=n:  
        sum,k=sum+k*k,k+1  
    return sum  
  
def sum_cube(n):  
    sum,k=0,1  
    while k<=n:  
        sum,k=sum+k*k*k,k+1  
    return sum  
  
print(sum_nature(4))  
print(sum_square(4))  
print(sum_cube(4))
```

输出：

```
10
30
100
```

代码的整体框架都很类似，我们不妨将函数抽象出来

```
def nature(k):  
    return k  
  
def square(k):  
    return k*k  
  
def cube(k):  
    return k*k*k  
  
def sum_num(n,func=nature):#用上上面学的  
    sum,k=0,1  
    while k<=n:  
        sum,k=sum+func(k),k+1  
    return sum  
  
print(sum_num(4,nature))  
print(sum_num(4,square))  
print(sum_num(4,cube))  
  
print(sum_num(4))
```

输出：
```
10
30
100
10
```


##### 1.6.2 作为通用方法的函数

这里开始难度就有点抽象起来了，计算黄金比例的例子，逐行解析一下：

```
def improve(update, close, guess=1):  
    while not close(guess):  
        guess = update(guess)  
    return guess  
```

首先需要弄明白，这里的update和close并不是python内置的函数，而是自定义的函数，也就是1.6.1所指代的，可以被当作参数传入的函数，根据名字定义，这个函数实现如下功能：

猜数字（初始未1），当猜的这个数字不接近你预期中的值时（while not close），根据update函数所提供的方法更新guess值，从而继续猜测，最终达到某个精度后结束，并且返回猜测值

```
def golden_update(guess):  
    return 1 / guess + 1  
  
def square_close_to_successor(guess):  
    return approx_eq(guess * guess, guess + 1)  
  
def approx_eq(x, y, tolerance=1e-15):  
    return abs(x - y) < tolerance  
```

这几行代码其实是数学知识，课本里的要求是求解黄金比例的某个精确值，golden_updata实现的是黄金比例的递推更新方法，而下一个函数则是实现是否足够接近

下面贴两个黄金比例的式子，其实就是把黄金比例的计算式子转换成了代码：

   $\phi = 1 + \frac{1}{\phi}$
   $\phi^2 = \phi + 1$

用第一个式子递推计算，用第二个式子进行判断是否精度足够高了

接下来就是要调用函数了：

```
result = improve(golden_update, square_close_to_successor)  
print(result)
```

这里的golden_update和square_close_to_scccessor都是在上文自己定义的，计算黄金比例的更新函数和比较黄金比例是否接近的函数，把他们放进我们一开始定义的improve函数，即实现猜数字的函数。总的来说，代码如下：

```
def improve(update, close, guess=1):  
    while not close(guess):  
        guess = update(guess)  
    return guess  
  
def golden_update(guess):  
    return 1 / guess + 1  
  
def square_close_to_successor(guess):  
    return approx_eq(guess * guess, guess + 1)  
  
def approx_eq(x, y, tolerance=1e-15):  
    return abs(x - y) < tolerance  
  
result = improve(golden_update, square_close_to_successor)  
print(result)
```

输出：

```
1.6180339887498951
```

==与标准黄金比例对比暂略==

##### 1.6.3 嵌套定义

引出这个的意思就是说，上面的例子，golden_update和square_close_to_successor的定义都是在全局环境中定义的，虽然现在的函数很少，但是如果是在做一个项目，可能会涉及到很多名字一样的函数，也有可能会找不到这个函数之类的。这两个函数很显然他们的用途很少，基本上只可能在计算黄金比例的时候用到，所以没必要把函数定义写在全局帧，简单更改一下代码：

```
def find_golden(guess=1):  
    def improve(update, close, guess=1):  
        while not close(guess):  
            guess = update(guess)  
        return guess  
  
    def update(guess):  
        return 1 / guess + 1  
  
    def close(guess):  
        return approx_eq(guess * guess, guess + 1)  
  
    def approx_eq(x, y, tolerance=1e-15):  
        return abs(x - y) < tolerance  
  
    return improve(update, close, guess)  
  
print(find_golden())
```

其实感觉这么解释怪怪的，先这么理解吧，后面有更好的理解方式再来改


==平方根例子先掠过 ，有点没看懂==

~~先去写ds去了，到截止时间了~~
##### 1.6.4 作为返回值的函数

按照课本里的例子可以理解成复合函数
























# 生成式AI认识：

随便放张图先

