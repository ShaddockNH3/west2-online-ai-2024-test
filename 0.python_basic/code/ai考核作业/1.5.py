dic={}
print("现在请你输入若干个键值对，每个键值对之间由换行符分开，键值之间由空格隔开")
print("如果你想结束，请输入q")
while True:
    kv=input()
    if kv=="q":
        break
    k,v=kv.split()
    k=int(k)
    if(k%2!=0):
        dic[k]=v
print(dic)

