my_martix=[[1 for j in range(10)]for i in range(5)]
transposed_my_martix=[[my_martix[j][i] for j in range(len(my_martix))]for i in range(len(my_martix[0]))]
print(transposed_my_martix)
'''
生成数组并转置
以下是使用zip解包的方法
'''
transposed_my_martix=list(map(list,zip(*my_martix)))
print(transposed_my_martix)
