str=list(input().split())
num=[]
for items in str:
    if items.isdigit():
        num.append(int(items))
print(sorted(num))
