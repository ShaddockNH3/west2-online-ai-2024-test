'''
宝可梦游戏
分析和题目里给的一样 ，先写一个Pokemon的基类，然后写一个属性类继承一下
先说一下宝可梦的共性，有Hp,有属性，有攻击力，有防御力，有闪避，有技能
Hp，攻击力，防御力，闪避率是固定的，直接在父类写就行了
属性和技能由于每个宝可梦不一样，所以需要在父类写虚函数，然后在子类重写
由于每个宝可梦需要修改其他宝可梦的数值，所以可以设定为公有继承
这里思路错了，应该是先属性类也写一个类，然后再由具体的宝可梦继承，浪费了100多行代码（
'''

from abc import  ABC,abstractmethod#可以像cpp那样子写类
import random

class Pokemon:
    def __init__(self,hp,attack,defence,dodge):
        self.hp=hp
        self.attack=attack
        self.defence=defence
        self.dodge=dodge

    def restraint(self):  # 克制关系
        pass

    def restrained(self):  # 被克制关系
        pass

    def No_restraint(self): #无克制关系
        pass

    def if_restraint(self): #判断是否克制，如果克制返回1，无克制返回0，被克制返回-1
        pass

    def is_dodge(self):#是否躲闪成功
        pass


class Water_Pokemon(Pokemon):#水属性宝可梦
    def __init__(self,hp,attack,defence,dodge):#继承
        Pokemon.__init__(self,hp,attack,defence,dodge)

class Fire_Pokemon(Pokemon):
    def __init__(self,hp,attack,defence,dodge):
        Pokemon.__init__(self,hp,attack,defence,dodge)

class Grass_Pokemon(Pokemon):#草属性宝可梦
    def __init__(self,hp,attack,defence,dodge):
        Pokemon.__init__(self,hp,attack,defence,dodge)

    def Attribute_passive(self):#属性被动
        self.hp=self.hp*1.1  #每回合回复 10% 最大HP值

class Eletri_Pokemon(Pokemon):
    def __init__(self,hp,attack,defence,dodge):
        Pokemon.__init__(self,hp,attack,defence,dodge)

    def Attribute_passive(self):#是否再发动一次技能
        pass

class Pokemon_PikaChu(Eletri_Pokemon):
    def __init__(self):
        Eletri_Pokemon.__init__(self,hp=80,attack=35,defence=5,dodge=0.3)

def choose_Pokemon_team():
    print("请选择3个宝可梦用于组成你的队伍：")
    print("1.皮卡丘(电属性) 2.妙蛙种子(草属性) 3.杰尼龟(水属性) 4.小火龙(火属性)")
    print("输入数字选择你的3个宝可梦,中间用空格隔开:",end=" ")
    pokemon1,pokemon2,pokemon3=int(input())
    pokemon4,pokemon5,pokemon6=int(input())#电脑的暂时也用输入代替,记得改
    '''
    这里实现宝可梦类的创建，记得创建
    '''
    print("请选择你的宝可梦:")
    print("")#这里通过上面的实现具体是什么
    print("输入数字选择你的宝可梦:",end=" ")
    num=int(input())
    print("你选择了",end=" ")
    print()#实现数字的转换



def a_turn():
    pass

def take_turn_for_one():
    who=0
    while True:
        if who==0:
            pass
        else:
            pass
        if My_Pokemon_hp<=0 or Computer_Pokemon_hp<=0:#尚未实现
            break
    if My_Pokemon_hp>0:
        return True
    else:
        return False

def begin():
    pass

begin()


