l=list(map(int,input().split()))
h=int(input())+30
cnt=0
for num in l:# 新学到的，for num in l，遍历数组
    if num<=h:
        cnt+=1
print(cnt)