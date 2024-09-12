### hw1

就不磨磨唧唧了，直接写完全部ok检查

看完课本1.5就能写了

```
from operator import add, sub  
  
def a_plus_abs_b(a, b):  
    """Return a+abs(b), but without calling abs.  
  
    >>> a_plus_abs_b(2, 3)    5    >>> a_plus_abs_b(2, -3)    5    >>> a_plus_abs_b(-1, 4)    3    >>> a_plus_abs_b(-1, -4)    3    """    if b < 0:  
        f = sub  
    else:  
        f = add  
    #这里一下没反应过来，python可以动态绑定  
    return f(a, b)  
  
def a_plus_abs_b_syntax_check():  
    """Check that you didn't change the return statement of a_plus_abs_b.  
  
    >>> # You aren't expected to understand the code of this test.    >>> import inspect, re    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)    ['return f(a, b)']    """    # You don't need to edit this function. It's just here to check your work.  
  
def two_of_three(i, j, k):  
    """Return m*m + n*n, where m and n are the two smallest members of the  
    positive numbers i, j, and k.  
    >>> two_of_three(1, 2, 3)    5    >>> two_of_three(5, 3, 1)    10    >>> two_of_three(10, 2, 8)    68    >>> two_of_three(5, 5, 5)    50    """    return i*i+j*j+k*k-max(i,j,k)*max(i,j,k)  
  
def two_of_three_syntax_check():  
    """Check that your two_of_three code consists of nothing but a return statement.  
  
    >>> # You aren't expected to understand the code of this test.    >>> import inspect, ast    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]    ['Expr', 'Return']    """    # You don't need to edit this function. It's just here to check your work.  
  
def largest_factor(n):  
    """Return the largest factor of n that is smaller than n.  
  
    >>> largest_factor(15) # factors are 1, 3, 5    5    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40    40    >>> largest_factor(13) # factor is 1 since 13 is prime    1    """    i=1  
    max=1  
    while i<n:  
        if n%i==0:  
            if max<i:  
                max=i  
        i+=1  
    return max  
  
def hailstone(n):  
    """Print the hailstone sequence starting at n and return its  
    length.  
    >>> a = hailstone(10)    10    5    16    8    4    2    1    >>> a    7    >>> b = hailstone(1)    1    >>> b    1    """    cnt=0  
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
    """Return the product of the first n terms in a sequence.  
  
    n: a positive integer    term:  a function that takes one argument to produce the term  
    >>> product(3, identity)  # 1 * 2 * 3    6    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5    120    >>> product(3, square)    # 1^2 * 2^2 * 3^2    36    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2    14400    >>> product(3, increment) # (1+1) * (2+1) * (3+1)    24    >>> product(3, triple)    # 1*3 * 2*3 * 3*3    162    """    i,sum=1,1  
    while i<=n:  
        i,sum=i+1,sum*term(i)  
    return sum  
  
def accumulate(fuse, start, n, term):  
    """Return the result of fusing together the first n terms in a sequence   
    and start.  The terms to be fused are term(1), term(2), ..., term(n).   
    The function fuse is a two-argument commutative & associative function.  
  
    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5    15    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5    26    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)    11    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2    25    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2    72    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)    19    """    i=1  
    while i<=n:  
        start,i=fuse(start,term(i)),i+1  
    return start  
  
  
def summation_using_accumulate(n, term):  
    """Returns the sum: term(1) + ... + term(n), using accumulate.  
  
    >>> summation_using_accumulate(5, square)    55    >>> summation_using_accumulate(5, triple)    45    >>> # This test checks that the body of the function is just a return statement.    >>> import inspect, ast    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]    ['Expr', 'Return']    """    return accumulate(add,0,n,term)  
  
  
def product_using_accumulate(n, term):  
    """Returns the product: term(1) * ... * term(n), using accumulate.  
  
    >>> product_using_accumulate(4, square)    576    >>> product_using_accumulate(6, triple)    524880    >>> # This test checks that the body of the function is just a return statement.    >>> import inspect, ast    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]    ['Expr', 'Return']    """    return accumulate(mul,1,n,term)  
  
  
def make_repeater(f, n):  
    """Returns the function that computes the nth application of f.  
  
    >>> add_three = make_repeater(increment, 3)    >>> add_three(5)    8    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1    243    >>> make_repeater(square, 2)(5) # square(square(5))    625    >>> make_repeater(square, 3)(5) # square(square(square(5)))    390625    """    def h(first):  
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

### hw03
