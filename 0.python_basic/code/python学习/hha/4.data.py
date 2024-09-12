f1=open("data1.txt")
f2=open("data2.txt", 'a')
data=f1.readline(3)
f2.write(data)
data=input()
f2.write(data)
f1.close()
f2.close()






#readline和readlines的区别在于前者最多只能读一行，后者不是，后者是有多少个字符
#比如说是13个字符，我输入1也是一行，12也是一行，但是14就是两行