n=int(input())
def fib(n):
    a,b=0,1
    cnt=2
    while(cnt<=n):
        a,b=b,a+b
        cnt+=1
    return b
print(fib(n))