#关于注释
'''
三个单引号
这是外部的多行注释
#嵌套注释
'''
"""
三个双引号
这是外部的多行注释
#可以嵌套注释
"""

#运算符
"""算术运算符"""
a=10
b=21
print(b//a)#取整除.往小的方向去整数
print(b%a)#取模.返回除法的余数

"""比较运算符"""
"""赋值运算符"""
#海象运算符
if(n:=10)>5:
    print(n)
""""先将n赋值为10,在于5比较"""

#逻辑运算符
a=10
b=20
if(a and b):
    print("a和b都是true")
if(a or b):
    print("a和b有一个ture")
if(not a):
    print("a为ture返回false")

#成员运算符
list=[1,2,3,4,5]
if(a in list):
    print("a在列表List")
else:
    print("a不在list")

#身份运算符
a=20
b=20
if(a is b):
    print("a与b有相同标识")

#运算符优先级
a=20
b=10
c=15
d=5
e=0
