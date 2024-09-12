#简单的拆分方法,
str=input()
a_str,b_str=str.split()
'''
上述代码必须一一对应，如果没有对应的话会报错。
这种实现方法叫拆包，同样的，其也可以应用于数组上面
'''
a=int(a_str)
b=int(b_str)
print(a+b)

#使用map的方法
'''
可迭代对象：列表，数组
map的基本语法：map(function, iterable)
function是应用到每个元素上的函数，
iterable是对应的迭代对象
最终返回一个迭代器

另外，sum函数，sum(...)是对迭代器内的东西求值
sum(iterable, start=0)
start为初始值，可选要不要写，0为默认
'''

print(sum(map(int,input().split())))
'''
思路其实就是和上面差不多
'''