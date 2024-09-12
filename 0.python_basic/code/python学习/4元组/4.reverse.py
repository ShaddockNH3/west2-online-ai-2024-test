n=int(input())
l=list(map(int,input().split()))
r_l=l[::-1]
for num in r_l:
    print(num,end=' ')