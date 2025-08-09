'''

创建集合
在 Python 中，创建集合可以使用{}字面量语法，{}中需要至少有一个元素，因为没有元素的{}并不是空集合而是一个空字典，
字典类型我们会在下一节课中为大家介绍。当然，也可以使用 Python 内置函数set来创建一个集合，
准确的说set并不是一个函数，而是创建集合对象的构造器，这个知识点会在后面讲解面向对象编程的地方为大家介绍。
我们可以使用set函数创建一个空集合，也可以用它将其他序列转换成集合，
例如：set('hello')会得到一个包含了4个字符的集合（重复的字符l只会在集合中出现一次）。
除了这两种方式，还可以使用生成式语法来创建集合，就像我们之前用生成式语法创建列表那样。

'''
set1 = {1, 2, 3, 3, 3, 3}
print(set1)

set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)

set3 = set('hello')
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)  # {2, 4, 6}
print(set1.intersection(set2))  # {2, 4, 6}

# 并集
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)  # {1, 3, 5, 7}
print(set1.difference(set2))  # {1, 3, 5, 7}

# 对称差
print(set1 ^ set2)  # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}
