#字符串的切分，替换与反向切分
print("请输入一个字符串，我将把里面的oi替换为fzu，并且进行倒叙输出")
str=input()
arr_fzu=str.split("oi")#按照oi进行切分
str_fzu="fzu".join(arr_fzu)#把fzu替换进原先的切分点
reverse_fzu=str_fzu[::-1]#反向切分
print(reverse_fzu)
