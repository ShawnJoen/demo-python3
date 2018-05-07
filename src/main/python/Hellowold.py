#!/usr/bin/env python3 - 在windows下可以不写

print ("Hello, Python!") #print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""

#标准数据类型 - Python3 中有六个标准的数据类型：
#---------------------------------Number（数字）- int(Python3的int,表示为长整型没有Long)、float、bool、complex(复数)
# 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
# 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
# 数学函数
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y) - x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)	返回数字x的平方根。

# 三角函数
# acos(x)	返回x的反余弦弧度值。
# asin(x)	返回x的反正弦弧度值。
# atan(x)	返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	返回的x弧度的正弦值。
# tan(x)	返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	将角度转换为弧度

# 数学常量
# pi	数学常量 pi（圆周率，一般以π来表示）
# e	数学常量 e，e即自然常数（自然常数）。

#数据类型是不允许改变
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
print("除法，得到一个浮点数: " + str(2 /4)) #0.5  整数除法中，除法（/）总是返回一个浮点数
print("除法，得到一个整数: " + str(2 // 4)) #0 想得到整数的结果使用运算符 //

#数学运算中*代表乘法，**为指数运算
#>>> 2*4 = 8
#>>> 2**4 = 16
#>>> 5 ** 2  # 5 的平方 = 25
#>>> 2 ** 7  # 2的7次方 = 128

varNumber1 = 1
varNumber2 = 10 #对象将被创建
del varNumber1, varNumber2 #删除数字对象的引用
#可以使用十六进制和八进制来代表整数
number = 0xA0F # 十六进制
print('十六进制数值:' + str(number))#2575
number=0o37 # 八进制
print('八进制:' + str(number))#31

#随机数函数
import random
print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Shawn' 返回一个随机字符 : ", random.choice('Shawn'))
print (" 从 1-100 中选取一个奇数 randrange(1,100, 2) : ", random.randrange(1, 100, 2))
print ("从 0-99 选取一个随机数 randrange(100) : ", random.randrange(100))
print ("[0,1)范围内 random() : ", random.random()) #0.3848253248722716
#seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数
random.seed()
print ("使用默认种子生成随机数：", random.random())
random.seed(10)
print ("使用整数种子生成随机数：", random.random())
random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())
#shuffle() 方法将序列的所有元素随机排序
list = [20, 16, 10, 5];
random.shuffle(list)
print ("随机排序列表 : ",  list)
random.shuffle(list)
print ("随机排序列表 : ",  list)
print ("uniform(5, 10) 的随机浮点数 : ",  random.uniform(5, 10))#8.32548129941273
print ("uniform(7, 14) 的随机浮点数 : ",  random.uniform(7, 14))#11.50216637642797
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

num1 = 1;
num2 = 2;
#sum = float(num1) + float(num2)
#print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))#数字 1 和 2 相加结果为： 3.0
#print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))#两数之和为 6.0







#---------------------------------平方根
#--适用于正数
#num3 = float(input('请输入一个数字： '))#10.2
#num3_sqrt = num3 ** 0.5
#print(' %0.3f 的平方根为 %0.3f'%(num3, num3_sqrt))#10.200 的平方根为 3.194
#--适用于正数和负数
import cmath
#num4 = float(input("请输入一个数字: "))#-10.2
#num4_sqrt = cmath.sqrt(num4)
#print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num4 ,num4_sqrt.real,num4_sqrt.imag))#-10.2 的平方根为 0.000+3.194j

#---------------------------------RegEXPression 正则表达式
import re
# .	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d	匹配一个数字字符。等价于 [0-9]。
# \D	匹配一个非数字字符。等价于 [^0-9]。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。

# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

#从字符串的起始位置匹配一个模式
#re.match(pattern 正则表达式, string 匹配的字符串, flags=0)
print(re.match('www', 'www.shawn.com').span())  #(0, 3)
print(re.match('com', 'www.shawn.com'))         #None
print(re.match('.*com', 'www.shawn.com'))       #<_sre.SRE_Match object; span=(0, 13), match='www.shawn.com'>

#扫描整个字符串并返回第一个成功的匹配
print(re.search('www', 'www.shawn.com').span())  # (0, 3)
print(re.search('com', 'www.shawn.com').span())  # (10, 13)
print(re.search('XXX', 'www.shawn.com'))  # None

line1 = "Cats are smarter than dogs"
matchObj1 = re.match( r'(.*) are (.*?) .*', line1, re.M|re.I)
if matchObj1:
    print ("matchObj1.group() : ", matchObj1.group())   #Cats are smarter than dogs
    print ("matchObj1.group(1) : ", matchObj1.group(1)) #Cats
    print ("matchObj1.group(2) : ", matchObj1.group(2)) #smarter
else:
    print ("No match!!")

searchObj1 = re.search( r'(.*) are (.*?) .*', line1, re.M|re.I)
if searchObj1:
    print ("searchObj.group() : ", searchObj1.group())  #Cats are smarter than dogs
    print ("searchObj.group(1) : ", searchObj1.group(1))#Cats
    print ("searchObj.group(2) : ", searchObj1.group(2))#smarter
else:
    print ("Nothing found!!")

#替换字符串中的匹配项
#re.sub(pattern, repl, string, count=0  模式匹配后替换的最大次数，默认 0 表示替换所有的匹配)
phone = "2004-959-559 # 这是一个电话号码"
num5 = re.sub(r'#.*$', "", phone) #删除注释
print ("电话号码 : ", num5) #2004-959-559
num6 = re.sub(r'\D', "", phone) # 移除非数字的内容
print ("电话号码 : ", num6) #2004959559

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2) #将匹配的数字乘于 2
s1 = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s1)) #A46G8HFD1134

#编译正则表达式
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print (m) #None
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print (m) #None
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print (m) #<_sre.SRE_Match object; span=(3, 5), match='12'>

#字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
#findall(string[, pos[, endpos]])
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('shawn 123 google 456')
result2 = pattern.findall('s77hawn123google456', 0, 10)
result3 = pattern.findall('shawngoogle456', 0, 10)
print(result1)#['123', '456']
print(result2)#['77', '123']
print(result3)#[]

#和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
#re.finditer(pattern, string, flags=0)
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )#输出每数字组

#split 方法按照能够匹配的子串将字符串分割后返回列表
#re.split(pattern, string[, maxsplit=0 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数 , flags=0])
print(re.split('\W+', 'shawn, shawn, shawn.'))#['shawn', 'shawn', 'shawn', '']
print(re.split('\W+', ' shawn, shawn, shawn.', 1) )#['', 'shawn, shawn, shawn.'] 分隔一次
print(re.split('a*', 'hello world'))#['hello world'] 找不到匹配的字符串, 不会对其作出分割

#---------------------------------

#---------------------------------

#---------------------------------

#---------------------------------




