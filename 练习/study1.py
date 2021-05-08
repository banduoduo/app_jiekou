# int_a = 1
# float_a = 1.5
# complex_a = 10j
# print(int_a)
# print(float_a)
# print(complex_a)
# print(type(int_a))
# print(type(float_a))
# print(type(complex_a))

# list_a = [1, 2, 3]
# print(list_a)
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
"""
分段函数求值
     3x - 5 (x>1)
f(x) = x + 2 (-1 <= x <= 1)
     5x + 3 (x < -1)
"""
# 分支结构 if else
# x = -5
# if x > 1:
#     y = 3 * x - 5
#     print("y的值是{}".format(y))
# else:
#     if x >= 1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
#     print("y的值是{}".format(y))

# 多重分支 if elif elif/else

"""
分段函数求值
     3x - 5 (x>1)
f(x) = x + 2 (-1 <= x <= 1)
     5x + 3 (x < -1)
"""
# x = -2
# if x > 1:
#     y = 3 * x - 5
# elif -1 <= x <= 1:
#     y = x + 2
# elif x < -1:
#     y = 5 * x + 3
# print("y的值是{}".format(y))

"""
1.计算1-100求和
2.加入分支结构实现1-100之间的偶数求和
3.使用python 实现1-100之间的偶数求和
"""
# result = 0
# for i in range(101):
#     result = result + i
# print(result)

# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print("1-100之间的和是{}".format(sum))

# result = 0
# for i in range(101):
#     if i % 2 == 0:
#         result = result + i
# print(result)

# result = 0
# for i in range(2, 101, 2): //第一位2代表从1开始计算，第二位2代表只要偶数的值
#     if i % 2 == 0:
#         result = result + i
# print(result)

# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)

# for i in range(1, 10):
#     if i == 3:
#         break
#     print(i)

"""
猜数字游戏
1.计算机出一个1-100之间的随机数由人来猜
2.计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

# import random
#
# computer_number = random.randint(1, 100)
# print(computer_number)
# while True:
#     person_number = int(input("请输入一个数字"))
#     if computer_number > person_number:
#         print("大一点哟")
#     elif computer_number < person_number:
#         print("小一点哟")
#     elif computer_number == person_number:
#         print("猜对了")
#         break

# 定义函数
# def app(a):
#     print(a)
#
#
# app(1)

# def method(a, b=[]):
#     b.append(a)
#     return b
#
#
# print(method(2))
# print(method(3))

# list_a = [1, 2, 3, 4]
# list_a.append(11)
# list_a.insert(0, 9)
# list_a.pop(2)
# list_a.remove(4)
# print(list_a)

"""
列表推导式
如果我们想生成一个平方列表，比如【1，4，9....】，使用for循环怎么写，使用列表生成式又应该怎么写呢
"""
# square_list = []
# for i in range(1, 4):
#     square_list.append(i**2)
# print(square_list)
# square_list2 = []
# for i in range(1, 4):
#     square_list2.append(i**2)
# print(square_list2)

# square2_list = [i**2 for i in range(1, 4)]
# print(square2_list)

"""
列表推导式
如果我们想生成一个平方列表，比如【1，4，9....】，使用for循环怎么写，使用列表生成式又应该怎么写呢
"""
# list_i = []
# for i in range(1, 4):
#     list_i.append(i ** 2)
# print(list_i)

# list_i= [i ** 2 for i in range(1, 4)]
# print(list_i)

# yuanzu
# tuple_b = [1, 2, 3]
# tuple_c = 1, 2, 3
# print(tuple_b)
# print(type(tuple_b))
# print(tuple_c)
# print(type(tuple_b))
#
# a = [3, 4, 5]
# tuple_a = (1, 2, 3, a)
# tuple_a[3][0] = "a"
# print(tuple_a)


# a = [1, 2, 3]
# tuple_banduo = (1, 2, a)
#
# tuple_banduo[2][0] = "a"
#
# print(tuple_banduo)


# with open('绝对路径', 'rt') as f:
#     print(f.read())
#     while True:
#         line = f.readline()
#         if line:
#             print(line)
#         else:
#             break

# with open('jueduiluj''rt')as a:
#     print(a.read())
#     while True:
#         line = a.readline()
#         if line:
#             print(line)
#         else:
#             break

# str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
# print(str.split())
# print(str.split('', 1))

# txt = "Google#Runoob#Taobao#Facebook"
# x = txt.split("#", 1)
# print(x)

# string = "www_gziscas_com_cn"
# str = string.split('_')
# print(str)

# string = "www_gziscas_com_cn"
# str = (string.split('_', 2)[0])
# print(str)

# string = "www_gziscas_com_cn"
# u1, u2, u3 = string.split('_', 2)
# print(u1)
# print(u2)
# print(u3)
