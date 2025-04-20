HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    def helper(i,sum):
        if i==n+1:
            return sum
        return helper(i+1,sum+term(i))
    return helper(1,0)



def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
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



def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    def f(n):
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r

    if row<column:
        return 0
    return f(row)//(f(row-column)*f(column))



def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
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