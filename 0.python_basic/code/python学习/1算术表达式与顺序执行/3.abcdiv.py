#首先是与上一题一样的思路
str_a,str_b,str_c=input().split()
a=int(str_a)
b=int(str_b)
c=int(str_c)
print((a+b)//c)

#然后是利用map，但是没有像上一题那么简洁，只是简化了转换的过程
a,b,c=map(int,input().split())
print((a+b)//c)

#chatgpt引入了lambda函数和*解包，可以使代码更简洁
'''
首先是解包，解包是*，用于解开迭代器中的数据赋予给函数当参数使用
而lambda函数是一个临时的匿名函数
代码如下：
'''
print((lambda a,b,c:(a+b)//c)(*map(int,input().split())))
'''
虽然lambda简化了代码但是增加了可读性，需要注意一下
然后就是向下取整的问题，题目应该是傻逼要求
'''
print((lambda a,b,c:int((a+b)/c))(*map(int,input().split())))