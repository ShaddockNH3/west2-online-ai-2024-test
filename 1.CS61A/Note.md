# CS61A

## 学习建议

CS61A这门课适合有一定基础的人听，不然很劝退，国外教材经典地和国内教材不一样，而且质量也差的比较多，比方说Java经典入门教程MIT 6.092，人家MIT设置的14个小时学完java，从基本语法到面向对象，课程+lab，国内可能得用一整年的时间（说的就是你，fzu！）。

本人从8月末开始准备考核，先花了五天的时间速通了一下python的语法，做完了原来考核的题目（除了正则表达式），后面就去稍微看了点爬虫和numpy库，由于数模比赛耽搁了一周多的时间，现在重新上github上看，发现考核内容较先前改变了不少，比如我上学期稍微看了点的神课cs61a，只不过上学期因为摆大烂没坚持下来（蒟蒻的证明），希望写这个文档之后能坚持下去吧（）

lab00，lab01，hw01，hw02，hog，用的是24spring，因为后面没有页面备份了，所以其他改用23spring

如果看到什么作业链接下载的话就算了，有时间我会检查一下我的笔记然后删掉一些不正确的东西
## 关于如何unlock或者检测作业

windows端在终端运行时使用`python ok --q question_name -u --local`，而非伯努利提供的`python3 ok --q question_name -u`

同理，在进行检测作业的时候也得改成`python ok --q question_name --local`

注意：
- python3改为python
- 由于我们无法使用伯努利账号，所以增加--local是必要的
- 由于是local测试，所以你写的代码不一定完全正确，但是通过了所有测试点

## 学习资料
- https://www.bilibili.com/video/BV1GK411Q7qp/?vd_source=0272bb7dd0d8d9302c55fc082442b9e3 （2022Fall）
- 课本链接：https://composingprograms.netlify.app/
- lab
- chatgpt
## 注意

直接听lecture就行了，其他的有兴趣可以听，有基础的也可以直接啃书，不过难度比较大就是了。只需要注意L1从35min开始听，前面的是国内外课程特有的成绩计算环节（对于初听国外网课的人来说......不敢跳过啊！）

本人有点基础，上学期听了几个lc，开学第一周速通了一下python语法，所以就直接上课本和lab了。

## 虚拟环境

spring2023需要使用python3.9，所以打开终端到那个文件夹，然后输入以下指令（使用conda）

```
conda create -p ./myenv python=3.9
```

然后激活：

```
conda activate ./myenv
```

检验

```
python --version
```

然后就ok了










## 第一章：使用函数构建抽象

到了后面，就开始有点难了，先看课本再说。

### 1.开始

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

### 1.2 编程要素

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

### 1.3 定义新的函数

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
### 1.4 设计函数

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

### 1.5 控制

终于到了if，else和while了，~~先上个体育课先~~，前面其实有很多东西讲的 不是很清楚，我的评价是还是自己理解的不够深

看了一遍1.5，感觉对于有基础的来说没啥好讲的，接着就是灾难一般的1.6


### 1.6 高阶函数

#### 1.6.1 作为参数的函数

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


#### 1.6.2 作为通用方法的函数

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

#### 1.6.3 嵌套定义

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
#### 1.6.4 作为返回值的函数

按照课本里的例子可以理解成复合函数，也就是说函数也可以作为返回值，比如说课本里的那个例子，我现在想要定义一个$h(x)=g(f(x))$，那么可以由如下代码实现

```
def compose(f,g):  
    def h(x):  
        return g(f(x))  
    return h  
  
def g(x):  
    return x+1  
  
def f(x):  
    return x*x  
  
H=compose(f,g)  
  
print(H(4))
```

输出：

```
17
```

来手动验证一下，输入4的时候确实输出的是17

#### 1.6.5 牛顿法

牛顿法是一种求函数$f(x)$的零点的方法，常用于求难解方程或者不可解方程的零点，这是一个数学方法，下面一整段都可以跳过暂时先不必理解。

先在$f(x)$"随便"取一个点$x_n$，然后在该点处一阶泰勒展开如下：

$f(x) \approx f(x_n) + f'(x_n) \cdot (x - x_n)$

令之为0：

$f(x_{x+1}) = f(x_n) + f'(x_n) \cdot (x_{n+1} - x_n)=0$   

反解出 $x_{n+1}$：

$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

然后将$x_{n+1}$继续带入$f(x)$中，继续求解，直到$f(x_n)$接近0或者等于0

$f(x)$=0可以解出$f(x) = f(x_n) + f'(x_n) \cdot (x - x_n)$的一个根，这个根就是$x_{n+1}$，但是由于我们用泰勒公式去一阶线性拟合，拟合地效果相对来说不是很好，所以接着把$x_{n+1}$带入，算出一个更接近地值：$x_{n+2}$

如此迭代过后，算出来的零点就很精确了

根据以上定义可以实现的python代码如下：

```
def nt(f,df,x):  
    while f(x)>0.00001 or f(x)==0:  
        x=x-f(x)/df(x)  
    return x  
  
def f(x):  
    return x*x-2*x  
  
def df(x):  
    return 2*x-2  
  
print(nt(f,df,4))
```

输出：

```
2.0000000004656613
```

这里实现导数的方法比较笨，自己手算的（）

现在可以根据这个方法来算n次方根，比如说我想求数m的n次方根，那么也就是求解方程$x^{n}-m=0$，引入牛顿法：

```
def nt(f,df,x):  
    while f(x,5,64)>0.00001 or f(x,5,64)==0:  
        x=x-f(x,5,64)/df(x,5)  
    return x  
  
'''  
64的五次方根
'''  
  
def f(x,n,m):  
    return pow(x,n)-m  
  
def df(x,n):  
    return n*pow(x,n-1)  
  
print(nt(f,df,4))#猜测为根为4
```

输出：

```
2.297396715534247
```

事实上这个误差还是定的太大了，可以再定地精确很多

#### 1.6.6 柯里化

简单来说，柯里化就是把f(x,y)转换成g(x)(y)的形式，其结果本质上是一样的，但是又有很大的区别，柯里化的意思是说，可以逐步接收参数，也可以固定x，从而不必每次都输入x

简单举个例子，比如说二元函数$f(x,y)=x+y$，与二元函数$g(x)(y)=x+y$，当我在计算前者的时候，必须逐个输入，如$f(1,1),f(1,2)$等等，而在使用后者时，我可以这么做，令$h(y)=g(1)(y)=1+y$，此后我调用$h(x)$，实际上就是在调用$g(1)(y)=1+y$

这种思想可以理解为闭包，$h(x)$把我们前者输入的1给“记住了”，从而在后续调用时可以不必再输入

~~先去疯狂星期四一下~~

~~其实最后吃的煎包~~

再回来看实现，不妨用这个例子：$f(x,y)=x^2+y^2$

```
def func(x):  
    def h(y):  
        return x*x+y*y;  
    return h  
  
H=func(2)(3)  
h1=func(2)  
h2=func(3)  
  
print(H)  
print(h1(3))  
print(h2(3))
```

输出：

```
13
13
18
```

下面的意思就是说我们可以使用柯里化来简化我们的代码，比如说我想实现很多次的while循环，每次都是从a到b，但是每次都输入while后面跟着一大串的东西很麻烦，那么可以进行如下化简（不使用map的版本）：

```
def example_while(a,b,f):  
    while a <= b:  
        a += 1  
        f()  
    return 0  
  
def f():  
    print("I hate study")  
  
example_while(1,3,f)
```

输出：

```
I hate study
I hate study
I hate study
```

~~很好，英语语法错了~~

这样子我每次进行某种操作的时候就没必要再写while循环了，而是直接`example_while(a,b,f)`，干进去就ok了

==这里留下一个小小的疑问，如果直接这样的话，该怎么使用a和b的值呢？回头再来想想==

==下面举得柯里化例子先掠过==


#### 1.6.7 lambda表达式

还没先看课本，就我自己对lambda表达式的理解，其实这部分就是为了简化代码用的，只在某个局部内使用地很平常的代码，没必要污染全局环境，甚至连函数内环境都不需要污染很多（仅个人理解）

根据课本提供的lambda表达式的理解，感觉这里可以理解为什么python是解释性语言？

```
lambda              x         :              f(g(x))
"A function that    takes x   and returns    f(g(x))"
```

简单写一个 lambda表达式，就不用课本那个了：

```
s=lambda x:x*x  
print(s(12))
```

输出：

```
144
```

接下来课本给的这个例子：

```
compose1 = lambda f,g: lambda x: f(g(x))
```

如果不看`lambda f,g:`这部分的话，后面代码的意思是说，x进行f(g(x))的操作后返回，其实也就是返回f(g(x))，简化为：

```
compose1 = lambda f,g: f(g(x))
```

所以这段代码的意思其实是分别指定f和g函数，然后进行f(g(x))操作，然后返回这个函数，上文中的这个是一个作用：

```
def compose(f,g):  
    def h(x):  
        return g(f(x))  
    return h  
  
def g(x):  
    return x+1  
  
def f(x):  
    return x*x  
  
H=compose(f,g)  
  
print(H(4))
```

我其实很不喜欢用lambda，因为这样的函数往往不是很清晰，虽然写的很简单，跟numpy库似的，代码写的跟鬼画符一样，但是不可否认其高效性。

#### 1.6.8 抽象和一等函数

这里说的抽象就是说，我们作为程序员可以自己定义把某个功能扔进某个函数，比如说我现在要写一个函数，按照顺序大小购买所有的物品，我可以把排序和购买两个操作全部扔进一个函数里，也可以把他们拆成三个函数，由大函数调用两个小函数，可以自己裁决

而一等函数的意思就是说，在python里，一等函数的地位完全是和普通的数据是一样的，可以直接绑定成数，可以乱七八糟地进行传递

#### 1.6.9 函数装饰器

首先函数装饰器是干啥的，其实就是可以让你在调用某个函数的时候进行一些额外的操作，比如说记录时间等等，可以用如下代码实现：

```
def trace(fn):  
    def wrapped(x):  
        print("Haha")  
        return fn(x)  
    return wrapped  
  
@trace  
def square(x):  
    return x*x  
  
print(square(4))  
  
'''  
@的意思就是说，在执行square的时候square其实并不是被绑定到下面return x*x上，而是被绑定到trace返回的wrapped函数上  
'''
```

==对于专家的额外内容，先掠过==

==对于专家的额外内容：装饰器符号 `@` 也可以后跟一个调用表达式。跟在 `@` 后面的表达式会先被解析（就像上面的 'trace' 名称一样），然后是 `def` 语句，最后将装饰器表达式的运算结果应用到新定义的函数上，并将其结果绑定到 `def` 语句中的名称上。==

### 1.7 递归

#### 1.7综述

听说cs61a最难的东西之一就是递归了，好好看眼

有稍微看了数据结构的就知道，其实递归就是一种经典的分而治之或者减而知之的策略。举一个很简单的例子，我们已经知道了下面一个数列的递推式：

$a_1=1$
$a_n=a_{n-1}+1$

有高中基础的同学肯定一下就能说出他的通项公式，但是我是一个笨蛋，不知道怎么求他的通项公式，一下子能想到的方法肯定是：

$a_{n-1}=a_{n-2}+1$

如此这样一直下去，最后肯定能得到$a_1$，最后反过来再推导上去，就能解出$a_n$是多少了

不妨将代码实现如下：

```
def a(n):  
    if n == 1:  
        return 1  
    else:  
        return a(n - 1) + 1  
  
print(a(13))
```

当n=1时的情况，我们称之为平凡情况，也就是递归基

递归就可以理解成数组中的递推式，不妨根据上面的情景，实现以下斐波那契数列：

$f(n)=f(n-1)+f(n-2)$

平凡情况就是$f(1)=1,f(2)=1$

下面代码实现：

```
def fib(n):  
    if n==1 or n==2:  
        return 1  
    return fib(n-1)+fib(n-2)  
  
print(fib(8))
```

输出：

```
21
```

可以验证一下斐波那契数列第8项是不是21：

$${1,1,2,3,5,8,13,21}$$

接下来就是最经典的汉诺塔问题，汉诺塔问题如下：

有三根柱子，分别为 A、B、C，柱子 A 上叠放着 n 个直径各不相同的圆盘，圆盘的直径由下到上依次减小。要求将所有圆盘从柱子 A 移动到柱子 C，遵循以下规则：

1. 每次只能移动一个圆盘。
2. 圆盘只能放在另一个柱子上。
3. 在移动过程中，任何时刻都不能将较大的圆盘放在较小的圆盘上。

现在请你告诉我，汉诺塔总共被移动了几次

这个问题如果不用递归解释的话，比较麻烦，如果用递归解释的话，那就很快：

我们要解决一个问题规模为n的问题（从A柱移动到C柱子，B为辅助柱），那么我们先求解一个问题规模为n-1的问题（将A柱上除了最后一个盘子移动到B柱上，借助C为辅助柱），然后把A柱子上最后一个n移动到C柱子上，最后我们还是要求解一个问题规模为n-1的问题（把B柱上剩下n-1个柱子移动到C柱上，借助A为辅助柱子）

递推式表示如下：

T(n)=T(n-1)+1+T(n-1)

很快地就可以发现，刚刚那么一个复杂的问题就转换成了上面那个式子，很容易用高中的方法求解出T(n)的通项公式，这里继续用递归求解，代码如下：

```
def hannuo(n):  
    if n==1:  
        return 1  
    return hannuo(n-1)+1+hannuo(n-1)  
  
print(hannuo(3))
```

输出：

```
7
```

从上面可以看出来，我们根本就不需要知道内部汉诺塔在求解的时候内部到底时怎么实现的，就这么求出来了

如果我们要知道内部是如何实现的，只需要简单地写出一个函数：

`hannuo('原本的柱子','目标柱子','辅助柱子')`

从上面的分析可以知道，我们是要解决一个问题，从A柱子移动到C柱子，然后后面两个n-1的问题分别是A移动到B，B移动到C，所以可以直接写代码如下：

```
def hanoi(n, source, target, auxiliary):  
    if n == 1:  
        print(source,"->",target)  
        return  
  
    hanoi(n - 1, source, auxiliary, target)  
    print(source, "->", target)  
    hanoi(n - 1, auxiliary, target, source)  
  
hanoi(3, 'A', 'C', 'B')
```

输出：

```
A -> C
A -> B
C -> B
A -> C
B -> A
B -> C
A -> C
```

~~上面写这些是因为这也是我最近才理解的东西，其实最后一个也不是很理解~~

然后看课本，和上述一样，先处理平凡情况：

```
def sum_digit(n):  
    if n<10:  
        return n  
    else:  
        n,last_num=n//10,n%10  
        return sum_digit(n)+last_num  
  
print(sum_digit(1234))
```

注意到，在递归实例中创建了很多局部帧，也就是说递归需要的空间很大，在此按下不表，日后再谈

#### 1.7.1 递归函数剖析

其实就是上面说的

#### 1.7.2 互递归

有种说不上来的感觉，但是写个代码先：

```
def is_even(n):  
    if n==0:  
        return True  
    else:  
        return is_odd(n-1)  
  
def is_odd(n):  
    if n==0:  
        return False  
    else:  
        return is_even(n-1)  
  
print(is_even(9))  
print(is_odd(9))
```

输出：

```
False
True
```

#### 1.7.3 递归打印

没看懂在讲啥（）

#### 1.7.4 树递归

最具体的例子就是斐波那契，虽然简单但是浪费很多空间，一般这种都可以用 动态规划来解决

#### 1.7.5 分割数

典型采用分而治之的求解方法，如果我想求n个数的分割方法，分割出来的最大数为m，那么记在这个问题为C(n,m)，然后定义递归基

每当，m需要从其本身到0，n也是，考虑遍历的情况，

C(n-1,m)和C(n,m-1)，直到m和n分别到0为止。

所以可以C(n,m)=C(n-1,m)和C(n,m-1)，定义递归基之后，便可求解。

### 第一章总结一下

函数的高级使用方法很不熟练，然后递归思想还得再多去理解以下
## 第二章、使用数据构建抽象

### 2.1 引言

主要引入了一下python的数据类型，可以使用type来进行检查

### 2.2 数据抽象

第一大段话的意思感觉就是我们可以定义一些新的数据类型，但是不必知道他们的具体实现方式，和面向对象的思想差不多

第一小节就有点面向对象的意思在里面了，和大一下cpp的蛮多作业差不多，定义一个分数类，然后计算分数类。

由于原始的python中并没有”分数“这个概念，所以这里的”分数“是我们自己定义出来的，也可以说是自己抽象出来的，可以实现分数的加减乘除运算

接下来就引入了“对”的概念，也就是列表，list，与c/cpp中的数组/向量类似。

list可以进行拆包操作，也可以进行寻秩访问

下面其实就是应用函数来表示list的方法？

### 2.3 序列

#### 2.3.1 列表

```
'''  
list的基本使用  
'''  
  
d=[1,2,3,4]  
print(d)  
print(len(d))  
d=[-1,0]+d*2  
print(d)  
#二维列表  
d=[[2,3],[1,4]]  
print(d[0])
```

#### 2.3.2 遍历

```
for <name> in <expression>:
    <suite>
```

expression可以是迭代器

- 序列解包

```
>>> same_count = 0
>>> for x, y in pairs:
        if x == y:
            same_count = same_count + 1
>>> same_count
2
```

copy一下

range函数，range(start,end,step)，步长默认为1

范围通常出现在 `for` 循环头部中的表达式，以指定 `<suite>` 应执行的次数。一个惯用的使用方式是：如果 `<name>` 没有在 `<suite>` 中被使用到，则用下划线字符 "_" 作为 `<name>`。


#### 2.3.3 序列处理

到了比较重点的地方，列表推导式了！

这是一个比较高级的使用方法

```
[<map expression> for <name> in <sequence expression> if <filter expression>]
```

比如迅速填充从1，100中的所有偶数：

```
l=[x for x in range(1,101) if x%2==0]  
print(l)  
```

迅速填充从1，100中所有偶数并且square一下
```
l=[x**2 for x in range(1,101) if x%2==0]  
print(l)
```

- 聚合

首先什么是完美数，完美数就是一个一个正整数，等于它所有 **真因数**（即除了它本身之外的所有正因数）之和

可以写一个discover函数先来找出一个数的真因数，可以直接用列表推导式来写，然后利用这个列表推导式作为判断条件，计算sum后来输出真因数p

```
def discover(n):  
    l=[x for x in range (2,n) if n%x==0]  
    return [1]+l  
  
p=[n for n in range(1,1000) if n==sum(discover(n))]  
  
print(p)
```

下面这个例子讲的是如何利用类似discover的函数，来求解在给定面积的情况下具有整数边长的矩形的最小周长，可以通过列表推导式进行遍历

```
def discover(n):  
    l=[x for x in range (2,n) if n%x==0]  
    return [1]+l  
  
def width(a,h):  
    assert a%h==0  
    return a//h  
  
def per(w,h):  
    return 2*(w+h)  
  
def min_per(a):  
    hei=discover(a)#求解初所有能把a整除的数  
    p=[per(width(a,h),h)for h in hei]#求解所有周长并取最小  
    return min(p)
```

接下里是**高阶函数**

首先就是一种函数，能对一个序列中的所有数都进行某种函数的处理之后，再返回某个序列，也可以对这个序列进行某种筛选后再返回筛选后的序列

下面reduce函数的意思就是说，可以定义一个函数，先对序列中的所有数进行处理后，然后再总体处理，简单来说就是先处理，然后聚合

然后下面的例子暂时都跳过，后面会将`map`和`filter`。看一眼内置的reduce长啥样：

`reduce(fn, s, initial)`，initial，也就是初始参数，默认为1

#### 2.3.4 序列抽象

- 成员资格

```
who in list
who not in list
```

- 切片

超级高级的用法，切片

l[first,end,step]

step也可以是负数，表示反方向切片

#### 2.3.5

没啥好讲的（）或许吧，回头再看看

#### 2.3.6 树

？怎么就开始讲树了？

所以还是比较适合稍微学了点数据结构的来啃cs61a（）

然后树这里一下子没看懂，先看一遍课（L12）

```
>>> def tree(root_label, branches=[]):
        for branch in branches:
            assert is_tree(branch), '分支必须是树'
        return [root_label] + list(branches)

>>> def label(tree):
        return tree[0]

>>> def branches(tree):
        return tree[1:]
```

上述代码是在构造树，这里没有构造树的实例，待会儿下面举个例子。桑树代码其实也算是一种在递归定义树，树的根节点，然后根节点下面有一个树存储的值，后续是这个结点的子树。

举个例子先：

```
def tree(root_label,branches=[]):  
    for branch in branches:  
        assert is_tree(branch)  
    return [root_label]+list(branches)  
  
def label(tree):  
    return tree[0]  
  
def branches(tree):  
    return tree[1:]  
  
def is_tree(tree):  
    if type(tree)!=list or len(tree)<1:  
        return False  
    #如果树不为列表或者长度小于1，肯定就不是树  
    for branch in branches(tree):  
        if not is_tree(branch):  
            return False  
    #递归进入所有树，从而进行判断  
    return True  
  
def is_leaf(tree):  
    return not branches(tree)  
  
t=tree(1,[tree(2,[]),  
  
                            tree(3,[tree(7,[]),  
                                                        tree(8,[])]),  
  
                            tree(4,[tree(5,[]),  
                                                        tree(6,[])])])  
  
print(t)  
print(label(t))  
print(branches(t))  
print(label(t[1]))  
print(branches(t[1]))  
print(is_leaf(t[1]))  
print(len(t))
```


越看越天才，太牛了，这个构造




