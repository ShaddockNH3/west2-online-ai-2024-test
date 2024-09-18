### lab00（24spring）

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

### lab01（24spring）

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



### lab02(23spring)

#### Q1: WWPD: The True Will Prevail

忘记放终端上的东西了，需要注意的是，这里考察的是对and，or和not的理解。

a and b，如果a为假则返回False，如果a为真b为真则返回b，如果a，b均为假则返回False

a or b，如果a为真则返回a，如果a为假b为真则返回b，如果均为假则返回False

#### Q2: WWPD: Lambda the Free

```
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 1
(cases remaining: 7)

Q: Which of the following statements describes a difference between a def statement and a lambda expression?
Choose the number of the correct choice:
0) A def statement can only have one line in its body.
1) A lambda expression cannot have more than two parameters.
2) A lambda expression does not automatically bind the function object that it returns to an intrinsic name.
3) A lambda expression cannot return another function.
? 2
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 2
(cases remaining: 6)

Q: How many parameters does the following lambda expression have?
lambda a, b: c + d
Choose the number of the correct choice:
0) Not enough information
1) two
2) three
3) one
? 1
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 3
(cases remaining: 5)

Q: When is the return expression of a lambda expression executed?
Choose the number of the correct choice:
0) When the lambda expression is evaluated.
1) When you pass the lambda expression into another function.
2) When the function returned by the lambda expression is called.
3) When you assign the lambda expression to a name.
? 2
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 1
(cases remaining: 4)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
>>> lambda x: x  # A lambda expression with one parameter x
? Function
-- OK! --

>>> a = lambda x: x  # Assigning a lambda function to the name a
>>> a(5)
? 5
-- OK! --

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
? Funcion
-- Not quite. Try again! --

? Function
-- Not quite. Try again! --

? 3
-- OK! --

>>> b = lambda x, y: lambda: x + y # Lambdas can return other lambdas!
>>> c = b(88, 43)
>>> c
? Function
-- OK! --

>>> c()
? 131
-- OK! --

>>> d = lambda f: f(4)  # They can have functions as arguments as well
>>> def square(x):
...     return x * x
>>> d(square)
? Function
-- Not quite. Try again! --

? 16
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 2
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> #
>>> # Pay attention to the scope of variables
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
? Function
-- Not quite. Try again! --

? 4
-- OK! --

>>> f = lambda z: x + z
>>> f(3)
? Function
-- Not quite. Try again! --

? Error
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 3
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> x = None # remember to review the rules of WWPD given above!
>>> x
? Nothing
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 4
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # Try drawing an environment diagram if you get stuck!
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
? Error
-- OK! --

>>> higher_order_lambda(g)(2)
? 4
-- OK! --

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
? 3
-- OK! --

>>> print_lambda = lambda z: print(z) # When is the return expression of a lambda expression executed?
>>> print_lambda
? Function
-- OK! --

>>> one_thousand = print_lambda(1000)
? 1000
-- OK! --

>>> one_thousand # What did the call to print_lambda return?
? Function
-- Not quite. Try again! --

? Nothing
-- OK! --

---------------------------------------------------------------------
OK! All cases for Lambda the Free unlocked.

Cannot backup when running ok with --local.
```

还是需要注意lambda语句的语法和其定义，尤其需要记住在python里，函数的地位和普通的变量是一样的，可以任意绑定

#### Q3: WWPD: Higher Order Functions

```
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Higher Order Functions > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
? beets
-- OK! --

>>> chocolate
? Function
-- OK! --

>>> chocolate()
(line 1)? sweets
(line 2)? 'cake'
-- OK! --

>>> more_chocolate, more_cake = chocolate(), cake
? sweets
-- OK! --

>>> more_chocolate
? 'cake'
-- OK! --

>>> # Reminder: cake, more_cake, and chocolate were defined/assigned in the code above!
>>> # It might be helpful to refer to their definitions on the assignment website so you don't have to scroll as much!
>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
? chocolate
-- Not quite. Try again! --

? Function
-- OK! --

>>> snake(10, 20)()
(line 1)? sweets
(line 2)? 'cake'
-- OK! --

>>> cake = 'cake'
>>> snake(10, 20)
? 30
-- OK! --

---------------------------------------------------------------------
OK! All cases for Higher Order Functions unlocked.

Cannot backup when running ok with --local.
```

需要对嵌套定义和柯里化很了解。

#### Q4: Composite Identity Function

上代码了：

```
def composite_identity(f, g):  
    def h(x):  
        h1=composer(f,g)  
        h2=composer(g,f)  
        if h1(x)-h2(x)==0:  
            return True  
        else:  
            return False  
    return h
```

这里我自己写出来感觉都有点懵，回头再来看看，还是感觉理解地不够深

#### Q5: Count van Count

```
def count_cond(condition):  
    def f(n):  
        i,cnt=1,0  
        while i<=n:  
            if condition(n,i):  
                cnt+=1  
            i+=1  
        return cnt  
    return f
```

在写出来这个之后，我大概懂题目的意思了，其实就是写一个通用模板

#### Q7: Multiple

```
def multiple(a, b):    
    while b != 0:  
        a, b = b, a % b  
    return a1//a*b1
```

欧几里得法

#### Q8: I Heard You Liked Functions...

不，我不喜欢

```
def h(n):  
    def f(x):  
        result=x  
        i=1  
        while i<=n:  
            if i%3==1:  
                result=f1(result)  
            elif i%3==2:  
                result=f2(result)  
            else:  
                result=f3(result)  
            i+=1  
        return result  
    return f  
return h
```

得定义三层，这里我每次都会忘记一个东西，事实上最内层的有时候应该传的是值，而不是函数。如果传的是函数的话，那么最后应该还得h(n)(m)才对

其实还是有点没搞懂这里是什么意思就是了，还得再看看

### lab03

#### q1

```
def ordered_digits(x):  
    l=x%10  
    x=x//10  
    tip=True  
    while x/10!=0:  
        if(l<x%10):  
            tip=False  
            break        l=x%10  
        x//=10  
    return tip
```


#### q2

```
def get_k_run_starter(n, k):  
    i = 0  
    final = None  
    while i<=k:  
        while n>10 and (n%10>(n//10)%10):  
            n//=10  
        final = n%10  
        i = i+1  
        n = n//10  
    return final
```

注意从后往前数就行了

#### q3

```
def make_repeater(func, n):  
    def h(first):  
        if func==identity:  
            return first  
        elif func==increment:  
            return add(n,first)  
        elif func==triple:  
            return mul(pow(3,n),first)  
        else:  
            i=1  
            while i<=n:  
                i,first=i+1,square(first)  
            return first  
    return h
```

抄一下hw2的代码

#### q4先掠过，有点怪怪的感觉



### lab4(23spring)

#### q1

```
=====================================================================
Assignment: Lab 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Squared Virahanka Fibonacci > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def virfib_sq(n):
...     print(n)
...     if n <= 1:
...         return n
...     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
>>> r0 = virfib_sq(0)
? 0
-- OK! --

>>> r1 = virfib_sq(1)
? 1
-- OK! --

>>> r2 = virfib_sq(2)
(line 1)? 2
(line 2)? 1
(line 3)? 0
-- OK! --

>>> r3 = virfib_sq(3)
(line 1)? 4
-- Not quite. Try again! --

(line 1)? 2
-- Not quite. Try again! --

(line 1)? 3
(line 2)? 2
(line 3)? 1
(line 4)? 0
(line 5)? 1
-- OK! --

>>> r3
? 16
-- Not quite. Try again! --

? 9
-- Not quite. Try again! --

? 25
-- Not quite. Try again! --

? 2
-- Not quite. Try again! --

? 1
-- Not quite. Try again! --

? 4
-- OK! --

>>> (r1 + r2) ** 2
? 1
-- Not quite. Try again! --

? 4
-- OK! --

>>> r4 = virfib_sq(4)
(line 1)? 3
-- Not quite. Try again! --

(line 1)? 4
(line 2)? 3
(line 3)? 2
(line 4)? 1
(line 5)? 0
(line 6)? 1
(line 7)? 1
-- Not quite. Try again! --

(line 1)? 4
(line 2)? 3
(line 3)? 2
(line 4)? 1
(line 5)? 0
(line 6)? 1
(line 7)? 2
(line 8)? 1
(line 9)? 0
-- OK! --

>>> r4
? 25
-- OK! --

---------------------------------------------------------------------
OK! All cases for Squared Virahanka Fibonacci unlocked.

Cannot backup when running ok with --local.
```

#### q2

```
def summation(n, term):  
    assert n >= 1  
    def helper(i,sum):  
        if i==n+1:  
            return sum  
        return helper(i+1,sum+term(i))  
    return helper(1,0)
```


不难，使用自下而上的递归

q3

```
def paths(m, n):  
    def sovle(i,j):  
        if i==m and j==n:  
            return 1  
        elif i<m and j==n:  
            return sovle(i+1,j)  
        elif i==m and j<n:  
            return sovle(i,j+1)  
        else:  
            return sovle(i+1,j)+sovle(i,j+1)  
    return sovle(1,1)
```

q4

```
=====================================================================
Assignment: Lab 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Lists > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> s = [7//3, 5, [4, 0, 1], 2]
>>> s[0]
? 2
-- OK! --

>>> s[2]
? [4,0,1]
-- OK! --

>>> s[-1]
? 2
-- OK! --

>>> len(s)
? 4
-- OK! --

>>> 4 in s
? 2
-- Not quite. Try again! --

? None
-- Not quite. Try again! --

? Fasle
-- Not quite. Try again! --

? False
-- OK! --

>>> 4 in s[2]
? True
-- OK! --

>>> s + [3 + 2, 9]
? [2,5,[4,0,1],2,5,9]
-- OK! --

>>> s[2] * 2
? [4,0,1,4,0,1]
-- OK! --

>>> x = [1, 2, 3, 4]
>>> x[1:3]
? [2,3,4]
-- Not quite. Try again! --

? [1,2,3]
-- Not quite. Try again! --

? [2,3]
-- OK! --

>>> x[:2]
? [1,2]
-- OK! --

>>> x[1:]
? [1,2,3,4]
-- Not quite. Try again! --

? [2,3,4]
-- OK! --

>>> x[-2:3]
? False
-- Not quite. Try again! --

? [3]
-- OK! --

>>> x[-2:4]
? [3,4]
-- OK! --

>>> x[0:4:2]
? [1,3]
-- OK! --

>>> x[::-1]
? [4,3,2,1]
-- OK! --

---------------------------------------------------------------------
OK! All cases for Lists unlocked.

Cannot backup when running ok with --local.
```

q5

(用阶乘逃课了)


```
def pascal(row, column):  
    def f(n):  
        r = 1  
        for i in range(1, n + 1):  
            r *= i  
        return r  
  
    if row<column:  
        return 0  
    return f(row)//(f(row-column)*f(column))
```


q6

让我们写递归解法，我记得之前写过迭代解法

```
def double_eights(n):    
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

上面是之前写过的迭代解法，接下来看看递归

```
def double_eights(n):  
    def helper(n,num,dir):  
        if n==0:  
            return False  
        elif n%10==8 and dir:  
            return True  
        elif n%10==8:  
            return helper(n//10,n%10,True)  
        else:  
            return helper(n//10,n%10,False)  
    num = n % 10  
    if num == 8:  
        a = True  
    else:  
        a = False  
    n //= 10  
    return helper(n,num,a)
```

其实是差不多的

### lab5（23spring）

