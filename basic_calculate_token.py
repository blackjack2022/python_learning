import math
# 幂
print(2 ** 3)

"""
赋值运算符和复合赋值运算符

Version: 1.0
Author: 骆昊
"""
a = 10
b = 3
a += b  # 相当于：a = a + b
a *= a + 2  # 相当于：a = a * (a + 2)
print(a)  # 大家算一下这里会输出什么
"""
赋值运算构成的表达式本身不产生任何值，也就是说，如果你把一个赋值表达式放到print函数中试图输出表达式的值，将会产生语法错误。
为了解决这个问题，Python 3.8 中引入了一个新的赋值运算符:=，我们称之为海象运算符，大家可以猜一猜它为什么叫这个名字。
海象运算符也是将运算符右侧的值赋值给左边的变量，与赋值运算符不同的是，运算符右侧的值也是整个表达式的值，看看下面的代码大家就明白了。
"""
print(a := 2)

# 格式化输出
name = 'jack'
age = 10
print("name=%s, age=%d " % (name, age))
print(f'name={name},age={age:3d}')

'''
这里其实还有一种格式化输出的方式，是 Python 3.8 中增加的新特性，大家直接看下面的代码就明白了。
说明：假如变量a的值是9.87，那么字符串f'{a = }'的值是a = 9.87；而字符串f'{a = :.1f}'的值是a = 9.9。
这种格式化输出的方式会同时输出变量名和变量值。
'''


radius = float(5.5)  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
print(f'{area = :.2f}')  # 输出：area = 95.03
