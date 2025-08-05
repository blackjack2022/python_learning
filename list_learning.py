import random

con = ['jack', 10, [100, 99]]
print(f'index 0={con[0]}')
# 负向索引：负向单索引是指在正向单索引的基础上添加一个负号“-”，所表达的含义是从右向左的方向获取元素，可以用[-n]表示，例如：
print(f'index 1={con[-2]}')
print(f'index 2:0={con[2][0]}')

'''
切片索引指的是按照固定的步长，连续取出多个元素，
可以用**[start : end : step]**表示。start指索取元素的起始位置；end指索取元素的终止位置（注意，end位置的元素是取不到的！）
；step指索取元素的步长，默认为1，表示逐个取出一连串的列表元素；切片，你可以把它理解成高中所学的值域范围，属于
'''
list2 = ['江苏', '安徽', '浙江', '上海', '山东', '山西', '湖南', '湖北']
# 取出”浙江“至”山西“四个元素
print(list2[2:6])
# 取出“安徽”、“上海”、“山西”三个元素
print(type(list2[1:6:2]))
# 取出倒数第二个和第三个元素
print(list2[-3:-1])
# 取出最后三个元素
print(list2[-3:])

list3 = ["1", "1", "2"]
'''
多个相同元素，remove方法删除从左到右第一个对应值元素
'''
list3.remove('1')
print(list3)

items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)
'''
列表生成表达式
'''
items2 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items2)

'''
嵌套列表生成表达式
[exp for iter_var_A in iterable_A for iter_var_B in iterable_B]
每迭代iterable_A中的一个元素，就把ierable_B中的所有元素都迭代一遍。

相当于这样的过程：

L = []
for iter_var_A in iterable_A:
    for iter_var_B in iterable_B:
        L.append(exp)
'''
L1 = ['香蕉', '苹果', '橙子']
L2 = ['可乐', '牛奶']
L3 = ['1', '2', '3']
# 不使用列表生成式实现
list7 = []
for x in L1:
    for y in L2:
        list7.append((x, y))
print(list7)
# 使用列表生成式实现
list8 = [(x, y, z) for x in L1 for y in L2 for z in L3 if (z != '1')]
print(list8)

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)
