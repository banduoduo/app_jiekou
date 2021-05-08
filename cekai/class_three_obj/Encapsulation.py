#封装
class Airplan:
    name = ""
    color = ""

    def set_color(self, color):
        self.color = color
        print(f"飞机的颜色是：{self.color}")

    def set_name(self, name):
        self.name = name
        print(f"飞机的名字是：{self.name}")


# air1 = Airplan()
# air1.set_name("第一家飞机")
# air1.set_color("红色")

#继承
#民用机
class MYplay(Airplan):
    zhongliang = ""
    def zhong(self,num):
        print(f"飞机的重量是{num}")

my = MYplay()
my.set_color("绿色")
my.set_name("民用机")
my.zhong(100000)


"""
class Tv:
    hunantv = ""
    zhejiang = ""

    def key_one(self,top1):
        self.hunantv = top1
        print("湖南台")

    def key_two(self,top2):
        self.zhejiang = top2
        print("浙江卫视")


tv1 = Tv()
tv1.key_one("湖南台")
tv1.key_two("浙江卫视")
"""