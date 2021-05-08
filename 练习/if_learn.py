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
#     print("今天是星期日")
# else:
#     print("输入的数字有误")

# 登录验证

# username = "admin"
# password = "admin123"
# username_input = input("请输入你的用户名")
# password_input = input("请输入你的密码")
# if username_input == username and password_input == password:
#     print("登陆成功")
# else:
#     print("登录失败")
# 计算1-100之间的和
# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print("1-100之间的和是{}".format(sum))

# num1 = 1
# while num1 <= 100:
#     if num1 % 2 == 0:
#         print("{}能被2整除".format(num1))
#     num1 += 1
#     if num1 % 2 != 0:
#         continue


# import random
#
# random_num = random.randint(1, 10)
# try_num = 5
# while try_num > 0:
#     num = int(input("请输入你的数字："))
#     if random_num == num:
#         print("你猜对了")
#         break
#     try_num -= 1
#     if try_num == 0:
#         print("你的机会用完了")


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}*{}={} ".format(j, i, i*j),end='')
#     print()


# def speak(name, voice):
#     print("{}发出了{}".format(name, voice))
#
#
# speak("小猫", "喵喵")
# speak("小狗", "旺旺")

# def compare(num1, num2):
#     if num1 > num2:
#         print("num1>num2")
#     elif num1 == num2:
#         print("num1=num2")
#     else:
#         print("num1<num2")
#
#
# compare(6, 6)


# def sum_and_cheng(a, b):
#     return a + b, a * b
#
#
# num1, num2 = sum_and_cheng(-10,20)
# print(num1)
# print(num2)
# def speak():
#     return "miaomiaomiao"
#
#
# a = speak()
# print(a)

# 递归函数
# def digui(n):
#     print(n)
#     if n == 10:
#         return
#     digui(n + 1)
#
#
# digui(1)

# x = 50

# def fun():
#     global x
#     print("x is", x)
#     x = 20
#     print("change x to", x)
#
#
# fun()
# print("x is still", x)

# var1 = "Hello"
# var2 = "world"
# print(var1 + var2)
#
# print(var1*2)

# 格式化
# num = 2
# print("我有 %d 个苹果" % num)
# username = "banduo"
# age = 20
# print("我的名字叫 %s 我今年 %d 岁了" % (username,age))

# capitalize 首字母大写
# username = "banduobanduo"
# username.capitalize()
# print(username.capitalize())

# count 相同字符的个数
# username = "banduobanduo"
# username.count("b")
# print(username.count("b"))
# endwith 是否以什么结尾
# startwith 是否以什么开头
# index 获取指定字符串的的位置
# isalnum 以纯数字或者英文数字组合，纯数字为true，有特殊字符就是false
# isalpha 必须是因为字母
# isdigit 纯数字
# islower 小写
# isupper 大写
# upper 转成大写
# lower 转小写
# split 分割
# replace 替换

# 数组 [0]是下标
# list_a = ["a","b","c"]
# print(list_a[0])
# for list_a in list_a[0]:
#     print(list_a)

# len() 获取数组的长度，数量
# for i in range(len(list_a)):
#     print(list_a[i])

# 数据替换
# list_a = ["a","b","c"]
# list_a[1]="d"
# print(list_a)
# del list_a[1] 删除元素

# 数组的常用方法
"""
append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.

"""
# a_list = ["a", "b", "c"]
# a_list.append("d")
# print(a_list)

# 元组 定义一个元组要加,
# tuple_a = ("a", "b", "c")
# # print(tuple_a)
# for i in tuple_a:
#     print(i)

# 元组操作
# 元组相加用+
# 删除元组 del tuple_a 只能删除整个元组

# 元组的内置函数
# max
# min
# list(tuple)

# tuple_a = (1, 3, 5, 7, 80)
# print(max(tuple_a))
# print(list(tuple_a))

# 字典 dict{} key:value,多个值用，隔开
# info = {"语文": 80, "数学": 90, "英语": 100}
# print(info["语文"])
# 添加数据
# info = {"语文": 80, "数学": 90, "英语": 100}
# info["物理"] = 70
# print(info)

# 字典的常用函数
# len(info) 长度
# str(info) 字符串
# in not in
# info = {"语文": 80, "数学": 90, "英语": 100}
# print("语文" in info)
# items() 遍历字典
# info = {"语文": 80, "数学": 90, "英语": 100}
# for i in info.items():
#     print(i)

# 获取两个变量
# info = {"语文": 80, "数学": 90, "英语": 100}
# for i,j in info.items():
#     print(i, "------", j)

# keys()
# info = {"语文": 80, "数学": 90, "英语": 100}
# print(info.keys())

# values()

# info = {"语文": 80, "数学": 90, "英语": 100}
# print(info.values())
# pop(Key) 删除键值对，返回这个key的value
# info = {"语文": 80, "数学": 90, "英语": 100}
# print(info.pop("语文"))

# 实现功能是购物车的功能，程勋运行之后，让购物车输入水果的编号，然后将购物车内的水果的数量增加
# iterms = {1: "苹果", 2: "香蕉", 3: "芒果"}
# iterms_keys = list(iterms.keys())
# shopcar = {"苹果": 0, "香蕉": 0, "芒果": 0}
# while True:
#     print("当前的购物车内：", str(shopcar))
#     num = int(input("请选择你要做什么？购物>1,退出程序>2:"))
#     if num == 1:
#         while True:
#             print(str(iterms))
#             choose_num = int(input("请选择您要购买的商品号码："))
#             if choose_num not in iterms_keys:
#                 print("当前无此商品，请重新选择：")
#                 continue
#             else:
#                 shopcar[iterms[choose_num]] += 1
#                 num = int(input("请选择：继续购物>1,退出>2："))
#                 if num == 1:
#                     continue
#                 else:
#                     break
#     elif num == 2:
#         print("程序已退出")
#         break
#     else:
#         print("输入错误，请重新选择")
#         break


# 集合的定义方法：
# a = set() 空集合
# a = {'a', 'b'} 有数据时的集合

# 将字符串转成集合 set（）
# 将数组转成集合 set（list）
# a - b 集合a中包含，而集合b 不包含的元素
# a | b 取并集
# a & b 取交集
# a ^b 不同时包含于a 和 b的元素

# 集合的办法
# add() 添加
# update() 添加，有就不添加，没有才添加
# remove() 已出单个元素
# claer() 清楚所有元素
# len() 长度
# intersection() 取交集
# unicon() 取并集


# slice 切片
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# c = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
# print(a[0:1:1])

# 下标=索引
# a[0:1:1]
# a[0:1]
# a[0:5:2]
# a[1]
# a[:9]
# a[1:]
# a[1::2]
# a[::-1]
# a[-1:-6:-1]
# 多个切片一起
# a[0:6][::-1]
# a[0:6][::2]



