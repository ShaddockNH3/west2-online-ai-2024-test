dic={'a': 3, 'b': 2, 'c': 1}
l1=[]
l2=[]
for key in dic:
    l1.append(key)
    l2.append(dic[key])
dic1={}
for i in range(0, len(l1)):
    dic1[l2[i]]=l1[i]
print(dic1)


for key, value in sorted(dic.items(), key=lambda item: item[1]):
    print(f"{key}:{value}")
