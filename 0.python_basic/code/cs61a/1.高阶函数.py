
def sum_test(n,term):
    total=0
    for i in range(1,n+1):
        total+=term(i)
    return total

def square_x(x):
    return x*x

def tri_x(x):
    return x**3

def pi_x(x):
    return 3.14

'''
如果我想输入的话可以通过两种途径，第一种就是if else
第二种：
eval函数，可以将输入的字符串解释为函数并且返回该函数
'''

n,func=input().split()
n=int(n)
func=eval(func)
print(sum_test(n,func))
