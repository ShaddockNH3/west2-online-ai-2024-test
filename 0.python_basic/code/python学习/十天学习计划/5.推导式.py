haha=0

'''
range(start, stop, step)
start（起始值）：序列的开始值，默认为0。
stop（终止值）：序列的结束值（不包括这个值哦）。
step（步长）：两个数之间的差值，默认为1。


列表推导式、集合推导式、字典推导式
[表达式 for 元素 in 可迭代对象 if 条件]

'''
'''
mylist=[x*x for x in range(10) if x%2==0]
print(mylist)

myset={x*x for x in range(10) if x%2!=0}
print(myset)

mydic={x:x*x for x in range(10)}
print(mydic)

mydic={x:x*x for x in myset}
print(mydic)

mydic={x:y for x in myset for y in mylist}
print(mydic)


mymartix=[[0 for j in range(2)] for i in range (2)]
print(mymartix)

myset_plus=[myset,[x+1 for x in myset],[x+2 for x in myset]]

mymartix=[[myset_plus[i] for j in range(3)] for i in range(3)]
print(mymartix)

'''

my_martix=[[i+j/2 for j in range(10)]for i in range(10)]
for row in my_martix:
    print(row)
for col in my_martix:
    print(col)
#突然发现，第二种打印方式就是矩阵的转置！

transposed_my_martix=[[my_martix[j][i]for j in range (len(my_martix))]for i in range (len(my_martix[0]))]
print(transposed_my_martix)