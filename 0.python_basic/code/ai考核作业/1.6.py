def how_much():
    mylist=list(map(int,input().split()))
    dic={}
    for num in mylist:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    for key,value in sorted(dic.items()):
        print(f"{key} : {value}times")

how_much()