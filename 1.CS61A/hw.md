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

