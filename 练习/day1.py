# a = 'string@d'
# print(a)
# print('dhdkhskd')

# int_a = 1
# float_a = 1.1
# complex_a = 2j

# print(type(int_a))
# print(type(float_a))
# print(type(complex_a))

# list_a = [2, 1, 3, "a", "b"]
# # print(list_a[0])
# # print(list_a[1])
# print(list_a[0:3])

# 分支结构
# a = 2
# if a == 0:
#     print('a=0')
# else:
#     print("a!=0")

# 多重分支
# a = 1
# if a == 1:
#     print("a=1")
# elif a== 2:
#     print("a=2")
# else:
#     print("a!=1,2")

"""
分段函数求值
     3x - 5 (x>1)
f(x) = x + 2 (-1 <= x <= 1)
     5x + 3 (x < -1)
"""

# 分支结构
# x = 2
# if x > 1:
#     y = 3*x - 5
#     print("y的值是{}".format(y))
# else:
#     if x >= 1:
#         y = x + 2
#     else:
#         y = 5*x + 3
#     print("y的值是{}".format(y))

# 多重分支

# x = -2
# if x > 1:
#     y = 3*x - 5
# elif -1 <= x <= 1:
#     y = x + 2
# else:
#     y = 5*x + 3
# print(y)

# 循环结构(for in 循环）

"""
1.计算1-100求和
2.加入分支结构实现1-100之间的偶数求和
3.使用python 实现1-100之间的偶数求和
"""
# result = 0
# for i in range(101):
#     result = result + i
# print(result)

# result = 0
# for i in range(101):
#     if i % 2 == 0:
#         result = result + i
# print(result)

# result = 0
# for i in range(2, 101, 2):
#     if i % 2 == 0:
#         result = result + i
# print(result)

# while 循环 搭配break(跳出整个循环,continue（跳出当前循环） 使用
# for i in range(1, 10):
#     if i == 4:
#         continue
#     print(i)

"""
猜数字游戏
1.计算机出一个1-100之间的随机数由人来猜
2.计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

# import random
#
# computer_number = random.randint(1, 100)
# # print(computer_number)
# while True:（不停循环）
#     person_number = int(input("请输入一个数字"))
#     if person_number > computer_number:
#         print("小一点")
#     elif person_number < computer_number:
#         print("大一点")
#     elif person_number == computer_number:
#         print("猜对了")
#         break
# 定义函数
# def method(a, b=[]):
#     b.append(a)
#     return b
#
#
# print(method(1))
# print(method(2))

# ** a(字典传参，传k值）
# * a （元祖传参）
# lambda 函数

# list_banduo=[1, 5,2, 3]
# list_banduo.append(1) 增加数字在末尾
# list_banduo.insert(0, 2) 增加数字在任意位置
# list_banduo.remove(1) 删除
# list_banduo.pop(2) 删除（标签）
# y = list_banduo.pop(2)
# print(y)
# list_banduo.sort(reverse=True) 正序排，在reverse是倒叙
# list_banduo.reverse() 倒叙排，从后往前
# print(list_banduo)

"""
列表推导式
如果我们想生成一个平方列表，比如【1，4，9....】，使用for循环怎么写，使用列表生成式又应该怎么写呢
"""
# list_square = []
# for i in range(1, 4):
#     list_square.append(i**2)
#
# print(list_square)
#
# list_square2 = [i**2 for i in range(1, 4)]
# print("list_square2", list_square2)
#
# list_square3 = [i**2 for i in range(1, 4) if i != 1]
# print(list_square3)

# list_square4 = [i*j for i in range(1, 4) for j in range(1, 4)]
# print(list_square4)

# 元组定义
# tuple_banduo = (1, 2, 3)
# tuple_banduo2 = 1, 2, 3
#
# print("tuple_banduo",tuple_banduo)
# print(type(tuple_banduo))
#
# print("tuple_banduo2",tuple_banduo2)
# print(type(tuple_banduo2))

# # 元组的不可变特性
# a = [1, 2, 3]
# tuple_banduo = (1, 2, a)
# print(id(tuple_banduo[2]))
# tuple_banduo[2][0] = "a"
# print(id(tuple_banduo[2]))
# print(tuple_banduo)

# 元组内置函数
# count （从元组中计算出总共有多少个相同的元素）
# index(索引)
# 集合
# 集合的内置函数
# a = {1, 2, 3}
# b = {1, 4, 5}
# print(a.union(b)) 并集
# print(a.intersection(b)) 交集
# print(a.difference(b))
# print({i for i in "jkbdakbdlaih"})

# 去重
# c = "ddddddvfgh"
# print(set(c))

# 字典

# dict_bando = {"a":2,"b":3,"c":4,"d":5}
# dict_banduo2 = dict(a=1,b=2)
# print(dict_bando.keys())
# print(dict_banduo2.values())

# print(dict_bando.pop("a"))
# print(dict_bando)
# print(dict_bando.popitem()) // 返回被删除的键值对
# print(dict_bando) // 删除掉上面执行的键值对后，还剩余的元素

# fromkeys
# a = {}
# b = a.fromkeys((1, 3, 4), "a")
# print(b)
# 字典推导式
# print({i: i*2 for i in range(1, 4)})

# 数字型
# 字符型
# 布尔型
# 格式化输出
# str ="my age is %d"%20
# print(str)
# format()方法
# name1 = "tom"
# name2 = "jane"
# print('two boy are {} and {}'.format(name1, name2))

# 打开文件的读取方式
# 方法一
# f = open('绝对路径', 'rt')
# print(f.read())
# print(f.reaable())
# print(f.readline())
# print(f.readlines())

# 方法二（最好这种）
# with open('绝对路径', 'rt') as f:
#     print(f.read())
#     while True:
#         line = f.readline()
#         if line:
#             print(line)
#         else:
#             break

# json 格式转换 dumps 方法
# import json
#
# info = [{
#     "name": "Tom",
#     "gender": "male",
#     'other': None
# }, {
#     "name": "Jack",
#     "gender": "male",
#     'other': None
# }]
# # dumps:将python中的字典转换为字符串
# data = json.dumps(info, sort_keys=True, indent=4)
# print(data)
# print(type(data))

# json 格式转换 dump 方法

# import json
#
# info = [{
#     "name": "Tom",
#     "gender": "male",
#     'other': None
# }, {
#     "name": "Jack",
#     "gender": "male",
#     'other': None
# }]
# print("读取json文件")
# json.dump(info, open("绝对路径.json", "w"))


# json 格式转换 loads 方法 将字符串转换json
# import json
#
# str = '''
#  [{
#     "name": "Tom",
#     "gender": "male"
# }, {
#     "name": "Jack",
#     "gender": "male"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(type(data))
# print(data)


# load
# import json
#
# js0bj = json.load(open("绝对路径.json", 'r'))
# print(js0bj)
# print(type(js0bj))
# print(js0bj[0]['itemId'])

# try:
#     num1 = int(input("请输入一个除数"))
#     num2 = int(input("请输入一个被除数"))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("除数不能为0")
# except ValueError:
#     print("输入需要是数值型整数")
# except:
#     print("这是一个能用型异常")
# else:
#     print("这个程序不是异常")
# finally:
#     print("无论发没发生异常，都执行")

# import os        # os 方法

# os.remove("testdir2")
# print(os.listdir("./"))
# os.removedirs("testdir")   #删除

# print(os.getcwd())        # 查看完整路径


# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#    f = open("b/tet.txt", "w")
#    f.write("hello,os using")
#    f.close()


# time.asctime()  #国外的时间格式
# time.time() #时间戳
# time.sleep()    # 等待
# time.localtime()       #时间戳转成元组
# time.strftime()  # 将当前的时间戳转换为带格式的时间

# print(time.asctime())
# print(time.time())
# print(time.sleep())
# print(time.localtime())
# print(time.strftime("%Y年%m月%d日  %H:%M:%S"))

# 获取两天前的时间
# now_timestamp = time.time()
# two_day_before = now_timestamp - 60 * 60 * 24 * 2
# time_tuple = time.localtime(two_day_before)
# print(time.strftime("%Y年%m月%d日  %H:%M:%S", time_tuple))

# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.read())

# import math
#
# print(math.ceil(6.4))           #值的上限
# print(math.floor(4.4))          # 值的下限
# print(math.sqrt(36))             # 平方根

# python 多线程
# import logging
# from time import sleep, ctime
#
# logging.basicConfig(level=logging.INFO)
#
#
# def loop0():
#     logging.info(("start loop0 at" + ctime()))
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
#
# def loop1():
#     logging.info(("start loop0 at" + ctime()))
#     sleep(2)
#     logging.info("end loop0 at " + ctime())

#
# def main():
#     logging.info("star all at " + ctime())
#     _thread.start_new_thread(loop0, ())
#     _thread.start_new_thread(loop1, ())
#     sleep(6)
#     logging.info("end all at " + ctime())
#
#
# if __name__ == '__main__':
#     main()

