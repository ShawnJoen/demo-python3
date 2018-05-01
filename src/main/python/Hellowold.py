#!/usr/bin/env python3 - 在windows下可以不写

print ("Hello, Python!") #print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""

#标准数据类型 - Python3 中有六个标准的数据类型：
#---------------------------------Number（数字）- int(Python3的int,表示为长整型没有Long)、float、bool、complex(复数)
aNumber, bNumber, cNumber, dNumber = 20, 5.5, True, 4+3j
print(type(aNumber), type(bNumber), type(cNumber), type(dNumber))#判断数据类型
# -- <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
if (type(aNumber) == int) :
    print("type(aNumber) == int -> True") #v
else :
    print("type(aNumber) == int -> False")
print(isinstance(dNumber, int))#False - 判断数据类型
#区别就是:
    #type()不会认为子类是一种父类类型
    #isinstance()会认为子类是一种父类类型
print("除法，得到一个浮点数: " + str(2 /4)) #0.5
print("除法，得到一个整数: " + str(2 // 4)) #0

#---------------------------------String（字符串）
#单行注释,多行:'''内容'''或"""内容"""， 还有多行字符串 也可以用三引号('''或""")指定
str1 = '字符串1'; str2 = "字符串2"
str3 = str1 + \
       str2 #使用反斜杠(\)来实现多行语句
print ("字符串多行: " + str3)
#反斜杠可以用来转义，使用r可以让反斜杠不发生转义
str4 = r"message1 \n message2" + "\n message3"
print ("字符串 r 反斜杠不发生转义" + str4)
str5='Shawn`s'
print("str5: " + str5[0:-1])           # Shawn`
print("str5: " + str5[0])              # S
print("str5: " + str5[2:5])            # awn
print("str5: " + str5[2:])             # awn`s
print("str5: " + str5 * 2)             # Shawn`sShawn`s
print("str5: " + str5[1], str5[-2])    #h ` ,和其他语言不同 向一个索引位置赋值，比如str5[0] = 'm'会导致错误

#---------------------------------Tuple（元组）-列表类似，不同在于 写在小括号(),不能修改
#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表
testTuple1 = ( 'abcd', 786 , 2.23, 'shawn`s', 70.2  )
testTuple2 = (123, 'shawn`s')
print (testTuple1[0])          # abcd
print (testTuple1[1:3])        # (786, 2.23)
print (testTuple1[2:])         # (2.23, 'shawn`s', 70.2)
print (testTuple2 * 2)          # (123, 'shawn`s', 123, 'shawn`s')
print (testTuple1 + testTuple2) # 连接元组 - ('abcd', 786, 2.23, 'shawn`s', 70.2, 123, 'shawn`s')
testTuple3 = ()    # 空元组
testTuple4 = (20,) # 一个元素，需要在元素后添加逗号,不加的话会认为就是整形20 不认成元组
print (testTuple3)#()
print (testTuple4)#(20,)
#---------------------------------Sets（集合）- 无序不重复元素的序列
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
testSet1 = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'} #重复的元素被自动去掉
print(testSet1)   #{'Tom', 'Jim', 'Mary', 'Rose', 'Jack'}
# 成员测试
if('Rose' in testSet1) :
    print('Rose 在集合中') #v
else :
    print('Rose 不在集合中')
# set可以进行集合运算
testSet2 = set('abracadabra')
testSet3 = set('alacazam')
print(testSet2)#{'b', 'd', 'r', 'a', 'c'}
print(testSet2 - testSet3)     # a和b的差集 - {'d', 'r', 'b'}
print(testSet2 | testSet3)     # a和b的并集 - {'b', 'l', 'd', 'r', 'a', 'm', 'c', 'z'}
print(testSet2 & testSet3)     # a和b的交集 - {'a', 'c'}
print(testSet2 ^ testSet3)     # a和b中不同时存在的元素 - {'m', 'b', 'l', 'd', 'z', 'r'}

#---------------------------------List（列表） 可变数据
testList1 = [ 'abcd', 786 , 2.23, 'shawn`s', 70.2]
testList2 = [123, 'shawn`s']
print (testList1[0])         # 输出列表第一个元素
print (testList1[1:3])       # [786, 2.23]
print (testList1[2:])        # [2.23, 'shawn`s', 70.2]
print (testList2 * 2)        # [123, 'shawn`s', 123, 'shawn`s']
print (testList1 + testList2) # 连接列表 ['abcd', 786, 2.23, 'shawn`s', 70.2, 123, 'shawn`s']
testList1[1] = 999 #list类型可变
print (testList1) #['abcd', 999, 2.23, 'shawn`s', 70.2]
testList1[2:3] = [13, 14, 15]
print (testList1) #['abcd', 999, 13, 14, 15, 'shawn`s', 70.2]
testList1[2:4] = []
print (testList1) #['abcd', 999, 15, 'shawn`s', 70.2]
#List内置方法 append()、pop()

#---------------------------------Dictionary（字典） 可变数据 - 字典当中的元素是通过键来存取,无序的对象集合
#字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合, 键(key)必须是唯一
dictionary1 = {}
dictionary1['one'] = "值1"
dictionary1[2]     = "值2"
dictionary2 = {'name': 'shawn`s', 'code':2, 'site': 'qcl108.dothome.co.kr'}
print (dictionary1['one'])   #值1
print (dictionary1[2])       #值2
print (dictionary2)          #{'name': 'shawn`s', 'code': 2, 'site': 'qcl108.dothome.co.kr'}
print (dictionary2.keys())   #dict_keys(['name', 'code', 'site'])
print (dictionary2.values()) #dict_values(['shawn`s', 2, 'qcl108.dothome.co.kr'])
dictionary1 = dict([('age',29), ('gender','male')])#键值对序列中构建字典
print (dictionary1)#{'age': 29, 'gender': 'male'}
dictionary1 = dict(age=29, gender='male')
print (dictionary1)#{'age': 29, 'gender': 'male'}
dictionary3 = {x: x**2 for x in (2, 4, 6)}
print (dictionary3)#{2: 4, 4: 16, 6: 36}
#数据类型转换

#---------------------------------
#Python 中的变量不需要声明。每个变量在使用前都必须赋值
#两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "shawn" 分配给变量 c
a, b, c = 1, 2, "shawn"
print("a:" + str(a))#1
print("b:" + str(b))#2
print("c:" + c)#shawn
aa = bb = 1 #三个变量被分配到相同的内存空间上
print("aa:" + str(aa))#1
print("bb:" + str(bb))#1
del aa, c
#print("c:" + c)#NameError: name 'c' is not defined 删除后调用此变量会出Error中断程序解释

#str6 = input("请输入: ") #等待用户输入
#print("输入的内容为: " + str6)
import sys #导入整个模块
print ('\n python 路径为',sys.path)
from sys import * #模块中的全部函数
#from sys import argv,path  #导入特定的成员
print ('\n python 路径为',path)
help(max) #help() 函数可以打印输出一个函数的文档




