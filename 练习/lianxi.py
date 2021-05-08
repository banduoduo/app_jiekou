"""
请输入1-7的数字
"""

# day = int(input("请输入1-7的数字"))
# if day == 1:
#     print("今天是星期一")
# elif day == 2:
#     print("今天是星期二")
# elif day == 3:
#     print("今天是星期三")
# elif day == 4:
#     print("今天是星期四")
# elif day == 5:
#     print("今天是星期五")
# elif day == 6:
#     print("今天是星期六")
# elif day == 7:
#     print("今天是星期七")
# else:
#     print("您输入的数字有误")

"""
登录验证
"""
# username = 'admin'
# password = 'admin123'
# username_input = input("请输入用户名")
# password_input = input("请输入密码")
# if username == username_input and password == password_input:
#     print("登陆成功")
# else:
#     print("登录失败")
"""
计算1-100之间的和
"""
# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print("1-100之间的和是{}".format(sum))

"""
1-100之间能被二整除的数
"""

# num1 = 1
# while num1 <= 100:
#     if num1 % 2 == 0:
#         print("{}能被2整除".format(num1))
#     num1 += 1
#     if num1 % 2 != 0:
#         continue

"""
猜数字，有五次机会，猜对了，输出你猜对了，用完五次几会就输出你的机会用完了
"""

# import random
#
# random_num = random.randint(1, 10)
# tru_num = 5
# while tru_num > 0:
#     num = int(input("请输入你要猜的数字"))
#     if num == random_num:
#         print("你猜对了")
#         break
#     tru_num -= 1
#     if tru_num == 0:
#         print("你的机会用完了")

"""
打印九九乘法表
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={} ".format(j, i, i * j), end='')
    print()

# def speak(name, voice):
#     print("{}发出了{}".format(name, voice))
#
#
# speak("小猫", "miaomiao")
# speak("小羊","moumou")

# def compare(num1, num2):
#     if num1 > num2:
#         print("num1>num2")
#     elif num1 < num2:
#         print("num1<num2")
#     else:
#         print("num1=num2")
#
#
# compare(6, 6)

# def cheng(a,b):
#     print(a*b)
#
#
# cheng(2, 2)

# def sum_cheng(a, b):
#     return a * b, a + b
#
#
# num1, num2 = sum_cheng(9, 2)
# print(num1)
# print(num2)

"""
递归函数
"""

# def digui(n):
#     print(n)
#     if n == 10:
#         return
#     digui(n + 1)
#
#
# digui(1)

"""
猜数字游戏
1.计算机出一个1-100之间的随机数由人来猜
2.计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

# import random
#
# computer_random = random.randint(1, 100)
# print(computer_random)
# while True:
#     person_num = int(input("请输入你要猜的数字"))
#     if person_num == computer_random:
#         print("你猜对了")
#         break
#     elif person_num > computer_random:
#         print("小一点")
#     elif person_num < computer_random:
#         print("大一点")

# num = 2
# print("我有%d个苹果" % num)

# name = "haha"
# age = 23
# print("我叫%s,我今年%d了" % (name, age))
# susername = "banduobanduo"
# print(susername.capitalize())
# print(susername.count('a'))
# print(susername.endswith('o'))
# print(susername.startswith('b'))
# print(susername.index('n'))
# print(susername.isalnum())
# print(susername.isalpha())
# print(susername.isdigit())
# print(susername.islower())
# print(susername.isupper())
# print(susername.lower())
# print(susername.upper())
# print(susername.split('o'))
# print(susername.replace('ban', 'pan'))

# list_a = ['china', 'us', 'ug']
# print(list_a[1])
# for a in list_a[0]:
#     print(a)
# print(len(list_a))
# for i in range(len(list_a)):
#     print(list_a[i])

# list_a[2] = 're'
# print(list_a)

# del list_a[2]
# print(list_a)

# list_b = ['a', 'b', 'c']
# list_b.append('d')
# print(list_b)
# list_b.clear()
# print(list_b)
# list_b.copy()
# print(list_b)
# list_b.index('a')
# print(list_b)

# tuple_a = ("a", "b", "v")
# tuple_b = ('d', "e", "f")
# print(tuple_a)
# for i in tuple_a:
#     print(i)
# print(tuple_a+tuple_b)
# del tuple_a

# tuple_num = (1, 3, 5, 7, 44, 55)
# print(max(tuple_num))
# print(min(tuple_num))
# print(list(tuple_num))

# dict_a = {'a': 66, 'b': 63, 'c': 44}
# print(dict_a['a'])
# dict_a['d'] = 99
# print(dict_a)
# print(len(dict_a))
# print(str(dict_a))
# a ='a' in dict_a
# print(a)
# d = 'd'in dict_a
# print(d)
# e = 'e' not in dict_a
# print(e)

# for i in dict_a.items():
#     print(i)

# for i, j in dict_a.items():
#     print(i, '-----', j)

# keys()
# info = {"语文": 80, "数学": 90, "英语": 100}
# print(info.keys())

# print(info.values())
# print(info.pop("语文"))
"""
实现功能是购物车的功能，程序运行之后，让购物车输入水果的编号，然后将购物车内的水果的数量增加
"""
# iterm = {1: "苹果", 2: "香蕉", 3: "芒果"}
# iterm_keys = list(iterm)
# shopcar = {"苹果": 0, "香蕉": 0, "芒果": 0}
# while True:
#     print("当前的购物车内有：", str(shopcar))
#     num = int(input("请选择您要做什么？购物>1,退出程序>2"))
#     if num == 1:
#         while True:
#             print(str(iterm))
#             choose_num = int(input("请您选择要购买的商品号码："))
#             if choose_num not in iterm_keys:
#                 print("当前无此产品，请重新输入：")
#                 continue
#             else:
#                 shopcar[iterm[choose_num]] += 1
#                 num = int(input("请选择：继续购物>1,退出>2"))
#                 if num == 1:
#                     continue
#                 else:
#                     break
#     elif num == 2:
#         print("退出程序")
#         break
#     else:
#         print("您输入的数字有误，请重新输入")
#         break

