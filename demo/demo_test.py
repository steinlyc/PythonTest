# class stu(object):
#     age = 1
#     b=2

#     def __init__(self, age):
#         age = age
#         print(b)

# student = stu(2)

# print(stu.age)
# print(student.age)

# class Dic():
#     def __init__(self):
#         global dic
#         dic = {"a": ("A", 1), " b": ("B", 2)}

# aa = Dic()
# print(aa)
# print(dic)
# a = 1

# class Stu(object):
#     def __init__(self, name):
#         self.name = name

#     def p3(self):
#         print("a" + self.name)

#     @classmethod
#     def p1(cls):
#         print(stu1.name)

#     @staticmethod
#     def p2():
#         print(stu1.name)
#         print(a)

# stu1 = Stu("haha")
# stu1.p1()
# stu1.p2()
# Stu.p1()
# Stu.p2()
# stu1.p3()
# Stu.p3(stu1)

# class test(object):
#     def __init__(self, name):
#         self.name = name

# num1 = test("haha")
# print(num1.name)

# from enum import Enum

# class Vip(Enum):
#     Yellow = 1
#     Red = 2
#     Black = 3
#     Blue = 3
# a=2
# r = a == Vip.Yellow
# print(r)
# print(type(Vip(3)))

# def main():
#     sum = 0
#     def step(num):
#         nonlocal sum
#         temp = sum + num
#         sum = temp
#         return temp

#     return step

# start = main()
# print(start.__closure__)
# print(start(1))
# print(start(3))
# print(start(4))
# print(start(7))

# from functools import reduce

# step = [(0, 1), (2, 4), (-2, -1), (1, 2)]

# r = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), step, (0, 0))

# print(r)

# #引入函数
# from functools import reduce

# #初始位置
# start = (0, 0)

# #经过的位置
# steps = [(1, 3), (2, -2), (-2, 3)]

# #计算结果
# r = reduce(
#     lambda current_pos, new_step: list(map(lambda x, y: x + y, current_pos, new_step)), steps, start)

# #结果坐标位置
# print(r)

# import re

# temp = ['a', 'A', 'b', 'B', 'd', 'D']
# r = filter(lambda x: True if re.findall('[a-z]', x) else False, temp)
# print(list(r))

# temp=[1,2,2,3,3,4,5,6,6,6,7,8]

# f=set(temp)
# print(list(f))

# a = []
# if not a:
#     print(bool(a))
#     print(not a)

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# temp = EC.title_contains('9999')
# temp2 = EC.title_contains('百度')

# print(temp(driver))
# print(temp2(driver))

# temp = {
#     'name':'lyc',
#     'age':12
# }

# print('名字是{name},年龄是{age}'.format(**temp))

# print('名字是{0},年龄是{1}'.format(*temp))

# print(f'名字是{temp["name"]},年龄是{temp["age"]}')

# print("浅拷贝：")
# import copy
# b=[1,2,3,4,5]
# print("id b:",id(b))
# h=copy.copy(b)
# print("id h",id(h))
# print(h)
# h.append(6)
# b.append(7)
# print(h)
# print("id h",id(h))
# print(b)   #浅拷贝新的列表h改变了，原来的b没变。
 
# b[1]='n'   #列表元素改变后，新的列表也没变
# print(h)
 
# ('id b:', 140165805110552)
# ('id h', 140165805110480)
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6]
# ('id h', 140165805110480)
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6]
# import time

# def test(fnc):
#     def getTime(*args,**kwargs):
#         print(time.time())
#         fnc(*args,**kwargs)
#     return getTime

# def run(*args,**kwargs):
#     print(*args,kwargs)

# run('a','b','c',a=1,b=2)

# class Test(object):
#     name='lily'
    
#     @staticmethod
#     def run(cls):
#         print(cls.name)

# Test.run(Test)