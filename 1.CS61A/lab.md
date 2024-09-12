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

### lab01

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


### lab02

上lab02