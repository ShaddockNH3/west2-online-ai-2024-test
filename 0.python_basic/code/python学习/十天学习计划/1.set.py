
'''
set名为集合，和数学上的集合类似，其拥有无序性，唯一性和可变性三个特点。
无序性，集合内的元素没有固定的顺序，不能通过索引访问元素
唯一性 ，集合中的每个元素都是唯一的，重复的元素在加入集合时会自动被去重
可变性，集合可以动态地添加或删除元素
'''

'''
# 使用大括号创建集合
my_set = {1, 2, 3, 4}

# 使用 set() 函数创建集合
another_set = set([1, 2, 3, 4])

my_set.add(5)  # 添加元素 5

my_set.remove(3)  # 删除元素 3，如果元素不存在，会报错
my_set.discard(3)  # 删除元素 3，如果元素不存在，不会报错

集合运算：

并集（union）：set1 | set2 或 set1.union(set2)
交集（intersection）：set1 & set2 或 set1.intersection(set2)
差集（difference）：set1 - set2 或 set1.difference(set2)
对称差集（symmetric difference）：set1 ^ set2 或 set1.symmetric_difference(set2)
'''

my_book=set(input().split())
fr_book=set(input().split())

sorted_my_book=sorted(my_book&fr_book)
sorted_fr_book=sorted(my_book^fr_book)

for book in my_book:
    print(book,end=" ")
print()
for book in fr_book:
    print(book,end=" ")