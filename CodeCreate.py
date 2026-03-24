"""
功能：生成强密码
- 选择长度
- 选择是否包含数字/符号/大小写
- 生成多个密码
- 保存到文件
"""


import random
import string

def simple_password(length,letters,digits,punctuation):
    """生成包含数字、大小写字母、符号的强密码"""
    chars=""

    if letters == 1:
        chars += string.ascii_letters  # 大小写字母
    if digits == 1:
        chars += string.digits          # 数字
    if punctuation == 1:
        chars += string.punctuation     # 符号
    if not chars:
        return "至少选择一种字符类型"
    return ''.join(random.choice(chars) for _ in range(length))


title="密码生成器"
print(title.center(50))
while True:
    print("1.选择你的密码长度")
    length=int(input())
    print("2.密码是否包含数字/符号/大小写")
    letters=int(input("是否需要大小写0/1 "))
    digits=int(input("是否需要数字0/1 "))
    punctuation=int(input("是否需要符号0/1 "))

    print("3.需要几个密码")
    count=int(input())
    for i in range(count):
        print(simple_password(length,letters,digits,punctuation))
    print("是否还需要生成y/n")
    judge=input()
    if judge=='n':
        break




    