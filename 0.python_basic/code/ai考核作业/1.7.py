class Good:
    def __init__(self,num,name,price,all,leave):
        self.__num=num
        self.__name=name
        self.__price=price
        self.__all=all
        self.__leave=leave

    def display(self):
        print(self.__num,self.__name,self.__price,self.__all,self.__leave)

    def income(self):
        income_goods=(self.__all-self.__leave)*self.__price
        print(income_goods)

    def setdata(self,num,name,price,all,leave):
        self.__num = num
        self.__name = name
        self.__price = price
        self.__all = all
        self.__leave = leave

g=Good(114514,"nasty",114514,114514,114)
g.income()
g.display()
g.setdata(10086,"中国移动",10086,10086,100)
g.income()
g.display()



