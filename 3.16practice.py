#数字
"""整数 int 浮点数float 复数 complex"""
import math
import random
a=1.0
print(a)
print(int(a))
print(n:=54//2)
print(7/2)
#数学函数
print(abs(-2))
print(math.ceil(4.1))
x=3
y=4
print(math.fabs(-10))#fabs以浮点数返回数字的绝对值
print(math.floor(4.9))#返回数字的下舍整数
print(pow(2,3))
print(math.sqrt(8))

#随机数函数
a=[2,1,3,5]
print(random.choice(range(10)))
print(random.random())
print(random.uniform(1,5))


#字符串
var1="Hello World!"
var2="Runoob"
print(var2[1:5])
print(var1[:6]+"Runoob!")#截取是从1开始

print("Hello \t World!")
if 'H' in var1:
    print("var1包括H")
print("我叫%s今年%d岁!" % ('小明',10))

"""字符串常用函数及用法"""
a="llo hello hello string"
print(str.capitalize(a))#把字符串的第一位变成大写
print(a.center(8,"-"))#将a居中,其余用-补充
sub="he"
print(a.count(sub))#计算子字符串出现的次数
print(a.find(sub))#查找子字符串第一次出现的位置
dit="1234"
print(dit.isdigit())#检查字符串是不是都是数字
op="ABS"
print(op.lower())
ll=("r","c","L")
print('-'.join(ll))#插入指定元素到指定字符序列中
string="aBCdeFG"
print(string.swapcase())#小写变大写,小写变大写



#列表
list=['red','green','blue','yellow','white','black']
print(list[0])#正索引 0到5
print(list[-1:])#负索引 -1到-6

print(list[:4])#从0开始
print(list[1:])

"""列表的函数方法"""
print(len(list)) #计算列表的函数
print(max(list))#计算列表的最大值
print(min(list))#计算列表的最小值

list.append("csgo")
print(list)
print(list.count("csgo"))
print(list.index("csgo"))
list.insert(3,"fbw")


#元组
tup1=('Google','Runoob',1997,2000)
type(tup1)

#字典
tinydict={'Name':'Runoob','Age':'7','Class':'First'}
print(tinydict['Name'])
tinydict['Name']='Peter'
print(tinydict['Name'])

#集合
set1={1,3,4,6,7}
set2=set(set1)
