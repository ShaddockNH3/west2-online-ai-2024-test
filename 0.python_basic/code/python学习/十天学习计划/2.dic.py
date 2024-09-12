

sales_data = {
    "2024-08-01": 150.75,
    "2024-08-02": 200.50,
    "2024-08-03": 175.20,
    "2024-08-04": 220.30,
    "2024-08-05": 160.10,
    "2024-08-06": 180.00,
    "2024-08-07": 210.00
}

print(sum(sales_data.values()))
print(sum(sales_data.values())/len(sales_data))
print(max(sales_data.values()))
print(min(sales_data.values()))
for key in sales_data:
    if sales_data[key]>(sum(sales_data.values())/len(sales_data)):
        print(key," ")
for items in sales_data.items():
    print(items)


del sales_data["2024-08-01"]
print(sales_data)
sales_data["2024-08-01"]=123
print(sales_data)



'''
def how_much():
    mylist=list(map(int,input().split()))
    dic={}
    for num in mylist:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    sorted(dic)
    print(dic)

how_much()

像上面这提就比较具有代表性！
'''