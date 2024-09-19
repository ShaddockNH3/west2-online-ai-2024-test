### hw1

就不磨磨唧唧了，直接写完全部ok检查

看完课本1.5就能写了

```
from operator import add, sub  
  
def a_plus_abs_b(a, b):  
    if b < 0:  
        f = sub  
    else:  
        f = add  
    #这里一下没反应过来，python可以动态绑定  
    return f(a, b)  
  
def a_plus_abs_b_syntax_check():  
    return i*i+j*j+k*k-max(i,j,k)*max(i,j,k)  
  
def two_of_three_syntax_check():  
    """Check that your two_of_three code consists of nothing but a return statement.  
  
    >>> # You aren't expected to understand the code of this test.    >>> import inspect, ast    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]    ['Expr', 'Return']    """    # You don't need to edit this function. It's just here to check your work.  
  
def largest_factor(n):  
    i=1  
    max=1  
    while i<n:  
        if n%i==0:  
            if max<i:  
                max=i  
        i+=1  
    return max  
  
def hailstone(n):  
    cnt=0  
    while n!=1:  
        print(n)  
        if n%2==0:  
            n//=2  
        else:  
            n=n*3+1  
        cnt+=1  
    print(1)  
    return cnt+1
```


### hw02

和先前一样，直接开写

```
from operator import add, mul  
  
square = lambda x: x * x  
  
identity = lambda x: x  
  
triple = lambda x: 3 * x  
  
increment = lambda x: x + 1  
  
  
HW_SOURCE_FILE=__file__  
  
'''  
首先这里可以调用以上函数，粉笔是平方，返回本身，三倍，以及自增，先记住  
  
'''  
  
def product(n, term):  
    i,sum=1,1  
    while i<=n:  
        i,sum=i+1,sum*term(i)  
    return sum  
  
def accumulate(fuse, start, n, term):  
    i=1  
    while i<=n:  
        start,i=fuse(start,term(i)),i+1  
    return start  
  
  
def summation_using_accumulate(n, term):  
    return accumulate(add,0,n,term)  
  
  
def product_using_accumulate(n, term):  
    return accumulate(mul,1,n,term)  
  
  
def make_repeater(f, n):  
    def h(first):  
        if f==identity:  
            return first  
        elif f==increment:  
            return add(n,first)  
        elif f==triple:  
            return mul(pow(3,n),first)  
        else:  
            i=1  
            while i<=n:  
                i,first=i+1,square(first)  
            return first  
    return h
```

最后一题实现有点沙雕，有时间看看怎么解更好点

### hw03（23spring）

```
def num_eights(n):  
    if n==0:  
        return 0  
    if n%10==8:  
        return 1+num_eights(n//10)  
    return num_eights(n//10)
```

递归解8

迭代版本如下：

```
def pingpong(n):  
    i=1  
    cnt=0  
    tip=True  
    while i<=n:  
        if tip:  
            cnt += 1  
        else:  
            cnt -= 1  
        if (num_eights(i) >0 or i%8==0) and tip:  
            tip=False  
        elif (num_eights(i) >0 or i%8==0) and not tip:  
            tip=True  
        i+=1  
    return cnt
```

那么如何将之转换为递归呢？

由于是从后往前推导，所以无法第一时间知道到底是+1还是-1。不妨将问题和课本那样拆解：

为了求PingPong(n)，我们得将问题拆解成PingPong(n-1) + or - 1，这里的+或者-的判断得是一个区间，区间前后即是num_eights(n) >0 or i%8的前一个和后一个。也就是说，我们可以先递归地把区间给求出来！

但是题目里禁止赋值，所以使用列表的想法破灭

不过可以注意到，情况分成两类，一个是+一个是-，所以感觉可以写成互递归，两个会是怎样的？

然后发现上面都是在做无用功，因为我的迭代版本太复杂了，根据答案精简了一下我的迭代版本：

```
def pingpong(n):  
    i=1  
    cnt=1  
    tip=1  
    while i<n:  
        if num_eights(i) >0 or i%8==0:  
            tip=-tip  
        cnt+=tip  
        i+=1  
    return cnt
```

通过提示，我们知道，迭代的信息有三个，索引，值和方向，所以需要写一个辅助函数，将这些信息传入递归中，从而确保索引，值，方向的正确性

其实我到最后还是没有理解为什么要这样做，最后照着答案写了一下：

```
def pingpong(n):  
    def help(i,cnt,tip):  
        if i==n:  
            return cnt  
        if num_eights(i) >0 or i%8==0:  
            return help(i + 1, cnt - tip, -tip)  
        else:  
            return help(i+1,cnt+tip,tip)  
    return help(1,1,1)
```

然后，我突然意识到，这里的递归并不是我此前理解的递归。此前理解的递归是类似于斐波那契数列那样的递归，将问题分而治之，不必了解问题具体到底是怎么解决的，从上至下

而在这个问题里，由于tip是不确定的，必须得从1开始向上构造，在不能使用赋值等操作的前提下，在递归这里引入了函数的再定义！

也就是说，这次我们是从下往上构造，递归基是最上面的位子！

而最开始的值传递则由“闭包”忠诚地完成，从而构造了一个自下而上的递归！

查询了一下资料发现，递归有两种策略，一种策略是自顶向下的递归，将问题分而治之，递归向下；而另一种递归则是自底向上的递归，也叫做构造性递归，通过逐步构造，每一层都依赖于前一层的结果，允许我们在没有赋值语句的前提下，仍然一步步求解。

换句话说，比如我们要求一个数列的前n项和，

$a_n=n*n-n+1,a_1=1$

自顶向下的递归可以这么写：

```
def f(x):  
    return x*x-x+1  
  
def sum_f(n):  
    if n==1:  
        return 1  
    return sum_f(n-1)+f(n)
```

因为我们可以得出如下分而治之的结果：

$S_{n}=S_{n-1}+a_n$

如果想正过来求$S_n$，很容易想到直接$a_1$开始加到$a_n$，先写出迭代版本：

```
def sum_f_die(n):  
    i=1  
    sum=0  
    while i<=n:  
        sum+=f(i)  
        i+=1  
    return sum
```

可以注意到，这里我们需要记录两个信息，一个是索引i，一个是sum，也就是和

```
def sum_f_(n):  
    def help(i,sum):  
        if i==n:  
            return sum  
        return help(i+1,sum+f(i+1))  
    return help(i=1,sum=f(1))
```

最终输出：

```
def f(x):  
    return x*x-x+1  
  
def sum_f(n):  
    if n==1:  
        return 1  
    return sum_f(n-1)+f(n)  
  
def sum_f_die(n):  
    i=1  
    sum=0  
    while i<=n:  
        sum+=f(i)  
        i+=1  
    return sum  
  
def sum_f_(n):  
    def help(i,sum):  
        if i==n:  
            return sum  
        return help(i+1,sum+f(i+1))  
    return help(i=1,sum=f(1))  
  
print(sum_f(100))  
print(sum_f_die(100))  
print(sum_f_(100))
```

输出：

```
333400
333400
333400
```

接下来也是一道递归，由于我在看课本的时候没去看分割数，现在在这里看一下


```
def count_coins(change):  
    def cnt(n,m):  
        if n==0:  
            return 1  
        elif n<0 or m is None:  
            return 0  
        else:  
            return cnt(n-m,m)+cnt(n,next_smaller_coin(m))  
    return cnt(change,25)
```

递归基的处理不是很熟练，其他都是对的，就是根据课本上的那个的变种


### hw4(23spring)

q2

```
def planet(mass):  
    """Construct a planet of some mass."""  
    assert mass > 0  
    return ['planet',mass]  
  
  
def mass(w):  
    """Select the mass of a planet."""  
    assert is_planet(w), 'must call mass on a planet'  
    return w[1]
```

就这两行

q3

```
def balanced(m):  
    if is_planet(m):  
        return True  
    if total_weight(left(m))*length(left(m))!=total_weight(right(m))*length(right(m)):  
        return False  
    return balanced(left(m)) and balanced(right(m))
```

本来以为做不出来的，没想到仔细分析了一下竟然做出来了！

q4

思路和这个差不多：

```
def tree(tree_label,branches=[]):  
    return [tree_label]+list(branches)  
  
def label(tree):  
    return tree[0]  
  
def branch(tree):  
    return tree[1:]  
  
def is_leaf(tree):  
    return not branch(tree)  
  
def print_tree(tree,i=0):  
    if is_leaf(tree):  
        print(' '*i+str(label(tree)))  
    else:  
        print(' '*i+str(label(tree)))  
        for b in branch(tree):  
            print_tree(b,i+2)  
  
  
t=tree(1,[tree(4,[tree(5)]),tree(9)])  
  
print_tree(t)
```

所以现在其实是要想办法构造出来一棵树，然后return这棵树就行了

研究了很久都没研究懂，看了答案也没看懂，今天先这样，回头再来研究一下

答案对列表推导式的应用很熟练，而我这里却很生疏。现在知道一整个属于一个树的构造，那么现在应该如何把这棵树给构建出来，很麻烦。

m相当于树结构的什么，想一下，m相当于树结构的root，而a相当于什么，a相当于树结构的branch，p相当于什么，p相当于树的叶子

再整理一下，m里面有什么？m里面是一个‘mobile’，left和right。这里的left和right代表的是什么？代表的是两个arm

然后是arm，arm里面有啥？‘arm’，长度，p/m。如果是p的话，那就是叶子节点，如果是m的话，那就再构造一棵树

然后就是至关重要的end函数，我之前一直都没有注意过这个函数。end函数接受arm，返回arm上挂着的到底是p还是m

所以我们现在应当构造branch，然后再构造root，最后相加。

有一个很重要的点，其实就是这里的m之类的东西都不算是根什么的，但是m里面的left和right的数值其实分别就是这个位子出去的两个重量。

gpt了一下，突然发现其实我还是没有理解这里递归的本质，只是在按照自己的想法瞎搞

首先我搞错了一点，这里其实并不是什么m代表啥，a代表啥，p代表啥的意思。

其次这是一个经典减而置之的问题，将原本的问题拆分为：

求解根结点的重量+两个分支的重量

递归基是碰到叶子节点，也就是planet的时候返回，其原本的重量，而其余的就是递归地求出这个根的所有重量，然后求和，就是这个节点的重量。

所以我的思路一开始就有问题。

然后没有很好地利用end函数和递归的思想，这里end函数返回的是判断arm上是p/m，应该很自然地想到，当返回p的时候，直接返回mass，其实就是递归基，当还是m的时候，递归求解即可

所以还是理解错题目的意思了，一直想着怎么用total_weight的解法，反而忽略了上面的问题。随后代码也是照抄的答案，标记一下回来再看看。

```
def totals_tree(m):  
    if is_planet(m):  
        return tree(mass(m))  
    else:  
        branch=[totals_tree(end(f(m))) for f in [left,right]]  
        return tree(sum([label(b) for b in branch]), branch)
```

然后我是感觉total_weight是能解的，感觉待会再去设计一下，思路应该和上面的差不多，利用end函数进行递归，只不过return的时候应该不一样。

也和我想的一样，只需要改一点就行了，但是突然感觉，如果这样求解的话，是不是没必要用上面那个列表推导式？

```
def totals_tree(m):  
    if is_planet(m):  
        return tree(mass(m))  
    else:  
        branch=[totals_tree(end(f(m))) for f in [left,right]]  
        return tree(total_weight(m), branch)
```

果然可以。

这里的branch函数感觉也可以用上面的total_weight来进行化简，或者说让列表推导式没那么看不懂

答案branch那行的意思是，f是left和right，f(m)其实就是递归下去，求解m的左分支和右分支

这里真的回头再思考一下，至少以我目前的能力是没办法想出else下面那行的句子的，return感觉花点心思应该可以。

==cy==

q5

```
def replace_loki_at_leaf(t, lokis_replacement):  
    if is_leaf(t) and label(t)=='loki':  
        return tree(lokis_replacement)  
    else:  
        bs=[replace_loki_at_leaf(b,lokis_replacement) for b in branches(t)]  
        return tree(label(t),bs)
```

这题也是半想半看答案的，经过了上面的洗礼，大概知道得结合列表推导式和递归来写这题。

写到这里，突然想起来一个很重要的事情，把tree的实现再自己手搓一遍：

```
def tree(tree_label,branches=[]):  
    return [tree_label]+list(branches)  
  
def label(tree):  
    return tree[0]  
  
def branch(tree):  
    return tree[1:]  
  
def is_tree(tree):  
    if type(tree)!=list or len(tree)<1:  
        return False  
    else:  
        for b in branch(tree):  
            if not is_tree(b):  
                return False  
    return True  
def is_leaf(tree):  
    return not branch(tree)
```

在检查是不是树的时候，也用到了相似的方式，递归进去遍历所有的树

然后这两题的列表推导式，其实都是在重复干两个事情：

1. 创建树的branch
2. 把树根和branch拼在一起形成一棵新树

再整理一下。

q6

```
def has_path(t, word):  
	assert len(word) > 0, 'no path for empty word.'  
    if t[0]!=word[0]:  
        return False  
    elif(len(word)==1):  
        return True  
    for b in branches(t):  
        if has_path(b,word[1:]):  
            return True  
    return False
```

和答案写的一样，简单来说还是减而置之，一下没想明白的点在于for循环，其实这个是遍历这个节点所对应的所有的路线，只要一条路走通立刻返回True

q7

```
=====================================================================
Assignment: Homework 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
interval > Suite 1 > Case 1
(cases remaining: 2)

>>> import hw04
>>> from hw04 import *
>>> str_interval(interval(-1, 2))
? "-1 to 2"
-- OK! --

>>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
? [3,10]
-- Not quite. Try again! --

? "[3,10]"
-- Not quite. Try again! --

? "3 to 10"
-- OK! --

---------------------------------------------------------------------
interval > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for interval unlocked.

Cannot backup when running ok with --local.
```

代码：

```
def lower_bound(x):  
    """Return the lower bound of interval x."""  
    return x[0]  
  
  
def upper_bound(x):  
    """Return the upper bound of interval x."""  
    return x[1]
```

没啥好说的

下面的问题后面都写了，当时搞numpy库的版本搞了好久，这里就不放了。

总的来说，作业的上半部分在教你搞树，下半部分在引入面向对象的东西，尽可能使用他接口提供的东西。

还是感觉写的怪怪的，有种说不上来的感觉。q9再看看。

### hw5


