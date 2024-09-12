'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("和：",end='')
print(sum(A^B))
'''

'''
str=list(input())
dic={}
for char in str:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1
for key,value in sorted(dic.items()):
    print(f"{key}:{value}")
'''

str=list(map(int,input().split()))
str=list(set(str))
print(sorted(str))