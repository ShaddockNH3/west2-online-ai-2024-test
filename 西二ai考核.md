# 写在最前面

大一是其他专业的，根本不知道有西二在线，转完专业自以为天下无敌，大一下爽玩半年，最后差点暴毙。所以决定发奋图强，毕竟再不学点什么就晚了，这也算是我最后的机会。虽然和大家一样是参加考核的，但是毕竟大二的老东西，稍微有点基础，所以写个笔记打个样，希望能给后来者一点点小小的帮助。先说一句，本人是蒟蒻，如果本文档出现任何错误或者写的不清楚的地方，请指出并且狠狠拷打我。但是小蒟蒻也有一颗成为大佬的心，写这篇其实主要目的之一是希望能帮到后人，还有一点就是激励自己能更新下去（）

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








































# 生成式AI认识：

随便放张图先

![[Pasted image 20240910221050.png]]