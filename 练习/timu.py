"""
编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。
"""

l = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))

print(','.join(l))

"""
问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
则输出为:40320
"""


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


print('请输入一个数字：')
x = int(input())
print(fact(x))
