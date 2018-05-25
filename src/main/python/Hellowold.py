#!/usr/bin/env python3 - 在windows下可以不写

print ("Hello, Python!") #print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""

#------------------------------------------------------------------
#Python 中的变量不需要声明。每个变量在使用前都必须赋值
#两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "shawn" 分配给变量 c
a, b, c = 1, 2, "shawn"
#print("a:" + str(a))#1
#print("b:" + str(b))#2
#print("c:" + c)#shawn
aa = bb = 1 #三个变量被分配到相同的内存空间上
#print("aa:" + str(aa))#1
#print("bb:" + str(bb))#1
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

#深入模块 - 模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。
    # 这些代码只有在第一次被导入时才会被执行
#__name__属性 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，
    # 模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行
    # 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入
# Filename: using_name.py
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
#python using_name.py - 程序自身在运行
#import using_name - 我来自另一模块
#dir() # 得到一个当前模块中定义的属性列表
#__all__ = ["echo", "surround", "reverse"] 这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块





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

import math
#math模块为浮点运算提供了对底层C函数库的访问
print (math.cos(math.pi / 4)) #0.7071067811865476
print (math.log(1024, 2))#10.0

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
print (random.choice(['apple', 'pear', 'banana']))
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
print (random.sample(range(100), 10))#[21, 6, 32, 25, 68, 48, 94, 18, 22, 97]
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
print("str5: ", str5[:4])              #Shaw
if( "h" in str5) :#大小写严格
    print("h 在变量 str5 中")#h 在变量 str5 中
else :
    print("h 不在变量 str5 中")
if( "H" not in str5) :
    print("H 不在变量 str5 中")#H 不在变量 str5 中
else :
    print("H 在变量 str5 中")
# 字符串格式化符号:
# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址
print ("名称 %s 年龄 %d" % ('小明', 10))
print("abc首字母大写".capitalize())#Abc首字母大写
print ("指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格:", "shawn".center(8, '*'))#*shawn**
#str.count 字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
str1="www.shawnc.com"
print ("str1.count('w') : ", str1.count('w'))#4
print ("str1.count('c', 0, 10) : ", str1.count('c',0,10))#1
#使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回
str1 = "全春林";
str_utf8 = str1.encode("UTF-8")
str_gbk = str1.encode("GBK")
print("UTF-8 编码：", str_utf8)#b'\xe5\x85\xa8\xe6\x98\xa5\xe6\x9e\x97'
print("GBK 编码：", str_gbk)#b'\xc8\xab\xb4\xba\xc1\xd6'
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))#全春林
print("GBK 解码：", str_gbk.decode('GBK','strict'))#全春林
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
str1='Shawn aaa!'
print (str1.endswith('!'))#True
print (str1.endswith('!',8))#True
print (str1.endswith('aaa'))#False
print (str1.endswith('w', 0, 4))#True
#反之
# startswith(str, beg=0,end=len(string))
# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
str1 = "this is\tstring"
print ("原始字符串: " + str1)
print ("替换 \\t 符号: " +  str1.expandtabs())
print ("使用16个空格替换 \\t 符号: " +  str1.expandtabs(16))
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
str1 = "Shawn example!"
print (str1.find("exam"))#6
print (str1.find("exam", 5))#6
print (str1.find("exam", 10))#-1
# 类似于 find()函数，不过是从右边开始查找.
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))#5
print (str1.rfind(str2, 0, 10))#5
print (str1.rfind(str2, 10, 0))#-1
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
print (str1.index("exam"))#-1
print (str1.index("exam", 5))
#print (str1.index("exam", 12))#    print (str1.index("exam", 12)) ValueError: substring not found
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))#5
#print (str1.rindex(str2,10))#    print (str1.rindex(str2,10)) ValueError: substring not found
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
print ("shawn33 ".isalnum())#False
print ("shawn33".isalnum())#True
print ("www.shawn.com".isalnum())#False
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
print ("shawn33".isalpha())#False
print ("shawn".isalpha())#True
print ("www.shawn.com".isalpha())#False
# 如果字符串只包含数字则返回 True 否则返回 False..
print ("123456".isdigit())#True
print ("www.shawn.com".isdigit())#False
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
print ("www.shawn.com".islower())#True
print ("www.Shawn.com".islower())#False
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
print ("shawn33".isnumeric())#False
print ("23443434".isnumeric())#True
# 如果字符串中只包含空白，则返回 True，否则返回 False.
print ("       ".isspace())#True
print ("   d    ".isspace())#False
# 如果字符串是标题化的(见 title())则返回 True，否则返回 False,所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False
print ("This Is String Example...Wow!!!".istitle())#True
print ("This is string example....wow!!!".istitle())#False
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
print ("THIS IS STRING EXAMPLE....WOW!!!".isupper())#True
print ("THIS is string example....wow!!!".isupper())#False
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print ("-".join( seq ))#r-u-n-o-o-b
print ("".join( seq ))#Shawn
# 返回字符串长度
print(len("shawn33"))#7
# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
str1 = "shawn example....wow!!!"
print (str1.ljust(50, '*'))#shawn example....wow!!!***************************
#反之
# rjust(width,[, fillchar])
# 转换字符串中所有大写字符为小写.
print( "shawn EXAMPLE....WOW!!!".lower() )#shawn example....wow!!!
# 转换字符串中的小写字母为大写
# upper()
# 将字符串中大写转换为小写，小写转换为大写
# swapcase()
# 截掉字符串左边的空格或指定字符。
print( "     this is string example....wow!!!     ".lstrip() );#this is string example....wow!!!
print( "88888888this is string example....wow!!!8888888".lstrip('8') );#this is string example....wow!!!8888888
#反之
# rstrip()
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
str1 = "this is string example....wow!!!"
intab = "aeiou"#这个字符串种匹配的字母 换
outtab = "12345"#这里相同index的字符
trantab = str1.maketrans(intab, outtab)
print (str1.translate(trantab))#th3s 3s str3ng 2x1mpl2....w4w!!!
# 返回字符串 str 中最大的字母。
print ("shawn231: " + max("shawn231"))#w
# 返回字符串 str 中最小的字母。
print ("shawn231: " + min("shawn231"))#1
# 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
print ("shawn example....wow!!!".replace("example", "eeeee"))#shawn eeeee....wow!!!
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
str1 = "this is string example....wow!!!"
print (str1.split( ))#['this', 'is', 'string', 'example....wow!!!']
print (str1.split('i',1))#['th', 's is string example....wow!!!']
print (str1.split('w'))#['this is string example....', 'o', '!!!']
# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# splitlines([keepends])
# 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# title()
# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
str1 = "this is wow!!!"
print ("str.zfill : ",str1.zfill(40))#str.zfill :  00000000000000000000000000this is wow!!!
print ("str.zfill : ",str1.zfill(50))#str.zfill :  000000000000000000000000000000000000this is wow!!!
print ('12'.zfill(5)) #00012
print ('-3.14'.zfill(7))#-003.14
# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false
print ("shawn33".isdecimal())#False
print ("23443434".isdecimal())#True



#---------------------------------Tuple（元组）-列表类似，不同在于 写在小括号(),不能修改
#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表
print ('Tuple（元组）')
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print (x,)	1 2 3	迭代
testTuple1 = ( 'abcd', 786 , 2.23, 'shawn`s', 70.2  )
testTuple2 = (123, 'shawn`s')
testTuple3 = "a", "b", "c", "d"
print (type(testTuple3))#<class 'tuple'>
print (testTuple3)#('a', 'b', 'c', 'd')
print (testTuple3[-2])#c
print (testTuple3[2:])#('c', 'd')
print (testTuple1[0])          # abcd
print (testTuple1[1:3])        # (786, 2.23)
print (testTuple1[2:])         # (2.23, 'shawn`s', 70.2)
print (testTuple2 * 2)          # (123, 'shawn`s', 123, 'shawn`s')
print (testTuple1 + testTuple2) # 连接元组 - ('abcd', 786, 2.23, 'shawn`s', 70.2, 123, 'shawn`s')
testTuple4 = ()    # 空元组
testTuple5 = (20,) # 一个元素，需要在元素后添加逗号,不加的话会认为就是整形20 不认成元组
print (testTuple4)#()
print (testTuple5)#(20,)
del testTuple5;#无法指定删除元素不过 可以删除整个元组
#print (testTuple5)# NameError: name 'testTuple5' is not defined
testTuple6 = "3", "1", "4", "5"
print (max(testTuple6))#5
testTuple7 = 3, 1, 4, 5
print (min(testTuple7))#1
list1= ['Google', 'Taobao', 'Shawn', 'Baidu']
tuple1 = tuple(list1)#将列表转换为元组
print (tuple1)#('Google', 'Taobao', 'Shawn', 'Baidu')
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)
print (u)#((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))



print ('-----------Tuple End----------')
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
print (testSet2 - testSet3) #在 testSet2 中的字母，但不在 testSet3 中
#{'b', 'r', 'd'}
print (testSet2 | testSet3)#在 testSet2 或 testSet3 中的字母
#{'l', 'm', 'r', 'd', 'z', 'a', 'c', 'b'}
#a & b #在 a 和 b 中都有的字母
#a ^ b  #在 a 或 b 中的字母，但不同时在 a 和 b 中
print ({x for x in 'abracadabra' if x not in 'abc'}) #{'d', 'r'}


print ('-----------Sets End----------')
#---------------------------------List（列表） 可变数据
print ('List（列表）')
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
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
print (testList1[-2])#shawn`s
print (testList1[1:])#[999, 13, 14, 15, 'shawn`s', 70.2]
testList1[2:4] = []
print (testList1) #['abcd', 999, 15, 'shawn`s', 70.2]
#List内置方法 append()、pop()
del testList1[2]
#del testList1[2:3]
print (testList1)#['abcd', 999, 'shawn`s', 70.2]
print (max([2,4,1,23]))#23
print (min([2,4,1,23]))#1
#嵌套列表
print ([testList1, testList2])#[['abcd', 999, 'shawn`s', 70.2], [123, 'shawn`s']]
# 在列表末尾添加新的对象
list1 = ['Google', 'Shawn', 'Taobao']
list1.append('Baidu')
print ("列表末尾添加新的对象 更新后的列表 : ", list1)#['Google', 'Shawn', 'Taobao', 'Baidu']
# 统计某个元素在列表中出现的次数
aList = [123, 'Google', 'Shawn', 'Taobao', 123];
print ("123 元素个数 : ", aList.count(123))#2
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1 = ['Google', 'Shawn', 'Taobao']
list2 = [22,44,11] # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print ("列表末尾一次性追加另一个序列中的多个值 扩展后的列表：", list1)#['Google', 'Shawn', 'Taobao', 22, 44, 11]
# 从列表中找出某个值第一个匹配项的索引位置
# list.index(obj)
# 将对象插入列表
list1 = ['Google', 'Shawn', 'Taobao']
list1.insert(1, 'Baidu')
print ('对象插入列表 : ', list1)#['Google', 'Baidu', 'Shawn', 'Taobao']
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1 = ['Google', 'Baidu', 'Taobao']
print ("pop : ", list1.pop())#Taobao
print ("移除列表中的一个元素 : ", list1)#['Google', 'Baidu']
# 移除列表中某个值的第一个匹配项
list1 = ['Google', 'Baidu', 'Taobao', 'Baidu']
list1.remove('Baidu')
print ("移除列表中某个值的第一个匹配项 : ", list1)#['Google', 'Taobao', 'Baidu']
# 反向列表中元素
# list.reverse()
# 对原列表进行排序
# list.sort([func])
# 清空列表
list1 = ['Google', 'Baidu']
list1.clear()
print ("列表清空后 : ", list1)#[]
# 复制列表
list1 = ['Google', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)#['Google', 'Baidu']

#列表当做堆栈使用 - 最先进入的元素最后一个被释放（后进先出）
stack = [3, 4, 5]
stack.append(6)
stack.pop()
#列表当作队列使用 - 第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.popleft()
#列表推导式
vec = [2, 4, 6]
#[3*x for x in vec] # [6, 12, 18]
#[[x, x**2] for x in vec] # [[2, 4], [4, 16], [6, 36]]
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
#[weapon.strip() for weapon in freshfruit] # ['banana', 'loganberry', 'passion fruit']
#[3*x for x in vec if x > 3] # [12, 18]
#[3*x for x in vec if x < 2] # []
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print ([x*y for x in vec1 for y in vec2]) # [8, 6, -18, 16, 12, -36, 24, 18, -54]
print ([vec1[i]*vec2[i] for i in range(len(vec1))]) # [8, 12, -54]
#嵌套列表解析
matrix = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
[9, 10, 11, 12],
]
print (matrix)#[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print ([[row[i] for row in matrix] for i in range(4)])#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print (transposed)#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] 等同上面的

print ('-----------List End----------')
#---------------------------------Dictionary（字典） 可变数据 - 字典当中的元素是通过键来存取,无序的对象集合
#字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合, 键(key)必须是唯一
print ('Dictionary（字典）')
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
del dictionary2['name'] # 删除键 'Name'
print (dictionary2)#{'code': 2, 'site': 'qcl108.dothome.co.kr'}
#dictionary2.clear()     # 清空字典
#print (dictionary2)#{}
#del dictionary2         # 删除字典
#print (dictionary2)#NameError: name 'dictionary2' is not defined
print (	len({'Name': 'Shawn', 'Age': 7, 'Class': 'First'}))#3
print (	type({'Name': 'Shawn', 'Age': 7, 'Class': 'First'}))#<class 'dict'>
print ("新复制的字典为 : ",dictionary2.copy())#新复制的字典为 :  {'code': 2, 'site': 'qcl108.dothome.co.kr'}
#fromkeys()方法
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  dict)#新的字典为 : {'name': None, 'age': None, 'sex': None}
dict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  dict)#新的字典为 : {'name': 10, 'age': 10, 'sex': 10}
#get() 方法
dict = {'Name': 'Shawn', 'Age': 27}
print ("Age 值为 : %s" %  dict.get('Age'))#Age 值为 : 27
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))#Sex 值为 : NA 无key的话使用默认值
#in 操作符
dict = {'Name': 'Shawn', 'Age': 7}
if  'Age' in dict:
    print("键 Age 存在") #Age 存在
else :
    print("键 Age 不存在")
# items() 方法以列表返回可遍历的(键, 值) 元组数组
dict = {'Name': 'Shawn', 'Age': 7}
print ("Value : %s" %  dict.items())#Value : dict_items([('Name', 'Shawn'), ('Age', 7)])
# keys() 方法以列表返回一个字典所有的键
dict = {'Name': 'Shawn', 'Age': 7}
print ("字典所有的键为 : %s" %  dict.keys())#dict_keys(['Name', 'Age'])
#setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
dict = {'Name': 'Shawn', 'Age': 7}
print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))#Age 键的值为 : 7
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))#Sex 键的值为 : None
print ("新字典为：", dict)#新字典为： {'Name': 'Shawn', 'Age': 7, 'Sex': None}
#update() 方法
dict = {'Name': 'Shawn', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print ("更新字典 dict : ", dict)#更新字典 dict :  {'Name': 'Shawn', 'Age': 7, 'Sex': 'female'}
# values() 方法以列表返回字典中的所有值
dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print ("字典所有值为 : ",  dict.values())#dict_values(['female', 7, 'Zara'])
#pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
site = {'name': 'Shawn', 'alexa': 10000, 'url': 'www.Shawn.com'}
pop_obj = site.pop('alexa')
print (pop_obj)#10000
print (site)#{'name': 'Shawn', 'url': 'www.Shawn.com'}
#popitem() 方法随机返回并删除字典中的一对键和值(一般删除末尾对)。
#如果字典已经为空，却调用了此方法，就报出KeyError异常
site= {'name': 'Shawn', 'alexa': 10000, 'url': 'www.Shawn.com'}
pop_obj = site.popitem()
print(pop_obj)#('url', 'www.Shawn.com')
print(site)#{'name': 'Shawn', 'alexa': 10000}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
#gallahad the pure
#robin the brave
# 序列中遍历时，索引位置和对应值可以使用 enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
#0 tic
#1 tac
#2 toe
# 同时遍历两个或更多的序列，可以使用 zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#What is your name?  It is lancelot.
#What is your quest?  It is the holy grail.
#What is your favorite color?  It is blue.
# 反向遍历一个序列，首先指定这个序列，然后调用 reversed()
for i in reversed(range(1, 10, 2)):
    print(i)
# 9
# 7
# 5
# 3
# 1
#按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f,end=",")#apple,banana,orange,pear,
print()
print ('-----------Dictionary End----------')
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
#print(re.sub('(?P<value>\d+)', double, s1)) #A46G8HFD1134

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

#---------------------------------if, while, 迭代器
var1 = 100
if var1:#true
    print ("1 - if 表达式条件为 true")#
    print (var1)#100
var2 = 0
if var2:#false
    print ("2 - if 表达式条件为 true")
    print (var2)
#while 循环
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
#flag = 1
#while (flag): print ('-shawn-')
#while 循环使用 else 语句
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")
#for 语句
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print (x)
#遍历数字序列
for i in range(5):
    print(i)
#range指定区间的值
for i in range(5,9) :
    print(i)
#指定数字开始并指定不同的增量
for i in range(0, 10, 3) :
    print(i, end=",")#0,3,6,9,
for i in range(-10, -100, -30) :
    print(i, end=",")#-10,-40,-70,
a = ['Google', 'Baidu', 'Shawn', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])#
# 1 Baidu
# 2 Shawn
# 3 Taobao
# 4 QQ
# pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句
#while True:
#    pass  # 等待键盘中断 (Ctrl+C)
for letter in 'Shawn':
    if letter == 'a':
        pass
        print ('执行 pass 块')
    print ('当前字母 :', letter)
#迭代器 - 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")#1 2 3 4
print()
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# while True:
#     try:
#         print (next(it), end=",")#1,2,3,4,
#     except StopIteration:
#         sys.exit()
# yield 的函数被称为生成器（generator）
# 生成器是一个返回迭代器的函数
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
# 返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
# def fibonacci(n): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print (next(f), end=" ")#0 1 1 2 3 5 8 13 21 34 55
#     except StopIteration:
#         sys.exit()
#---------------------------------def 函数
#可更改(mutable)与不可更改(immutable)对象
#strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象
#传递参数是没有类型 仅仅是一个对象的引用（一个指针）
#不可变类型 - 类似 c++ 的值传递 - 值传递的只是a的值fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身
#可变类型：类似 c++ 的引用传递 - 如列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
#传递参数 严格讲应该是 传不可变对象和传可变对象
#变量作用域
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），
#     再找不到就会去全局找，再者去内建中找
#只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
        # 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域
def area(width, height):
    return width * height
def print_welcome(name):
    print("Welcome", name)
a =  area(2,4);
print(a)#8
print_welcome("Shawn")#Welcome Shawn
#传不可变对象实例
def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print( b ) # 结果是 2
#传可变对象实例
def changeme( mylist ):
    mylist.append([1,2,3,4])
    print ("函数内取值: ", mylist)
    return
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )#[10, 20, 30, [1, 2, 3, 4]]
print ("函数外取值: ", mylist)#[10, 20, 30, [1, 2, 3, 4]]
#关键字参数 - 允许函数调用时参数的顺序与声明时不一致
def printinfo( name, age ):
    "打印任何传入的字符串"
    print ("名字: ", name)#shawn
    print ("年龄: ", age)#33
    return
#调用printinfo函数
printinfo( age=33, name="shawn" )
#默认参数
def printinfo( name, age = 33 ):
    print ("名字: ", name)
    print ("年龄: ", age)
    return
printinfo( name="shawn" )
#不定长参数 - 和上述2种参数不同，声明时不会命名
def printinfo( arg1, *vartuple ):
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var,end=", ")
    return
# 调用printinfo 函数
printinfo( 10 )#10
printinfo( 70, 60, 50 )#70  60, 50,
print ()
#lambda 匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print ("相加后的值为 : ", sum( 10, 20 ))#相加后的值为 :  30
#return语句 - 退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
#global 和 nonlocal关键字 - 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)#1
    num = 123#在这里修改了全局的num了
    print(num)#123
fun1()
print(num)#123
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)#100
outer()#100
# a = 10
# def test():
#     a = a + 1 #这样不使用关键字global,nonlocal 会报错#
#     print(a)#UnboundLocalError: local variable 'a' referenced before assignment
# test()
#---------------------------------输入和输出
print (str('Hello Shawn'))#Hello Shawn - 用户易读的表达形式
print (repr('Hello Shawn'))#'Hello Shawn' - 解释器易读的表达形式
print (str(1/7))#0.14285714285714285
#读和写文件 - open(filename, mode)
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
f = open("./foo.txt", "w")
print (f.write( "Shawn\n123" ))#6 - 返回写入的字符数
f.close()# 关闭打开的文件
f = open("./foo.txt", "r")
str = f.read()
print(str)#Shawn
f.close()
f = open("./foo.txt", "r")
str = f.readline()#f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
print(str)#Shawn
f.close()
f = open("./foo.txt", "r")#f.readlines() 将返回该文件中包含的所有行
str = f.readlines()#如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割
print(str)#['Shawn\n', '123']
f.close()
f = open("./foo.txt", "r")
for line in f:
    print(line, end='')#Shawn
f.close()
print ()
#f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
# f.seek() 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符
#pickle 模块 - 实现了基本的数据序列和反序列化
import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')
#pickle.dump(obj, file, [,protocol])
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)#从文件中创建上一次程序保存的对象
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()
import pprint
#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)#pickle 这个对象, 就能对 file 以读取的形式
pprint.pprint(data1)
data2 = pickle.load(pkl_file)#pickle 这个对象, 就能对 file 以读取的形式
pprint.pprint(data2)#
pkl_file.close()
#{'a': [1, 2.0, 3, (4+6j)], 'b': ('string', 'Unicode string'), 'c': None}
#[1, 2, 3, <Recursion on list with id=78805992>]

#---------------------------------错误和异常
print ("错误和异常")
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         #break #有break语句时无出错误会终结脚本, 或无加时循环执行try
#     except ValueError: #抓取值错误Error 如果一个异常没有与任何的except匹配，将会传递给上层的try中
#         print("Oops!  That was no valid number.  Try again   ")
#         pass
#     except (RuntimeError, TypeError, NameError):#可以同时处理多个异常
#         pass
#     except: #最后一个except子句可以忽略异常的名称 - 打印一个错误信息
#         print("Unexpected error:", sys.exc_info()[0])#Unexpected error: <class 'ValueError'>
#         raise

for arg in [1]:
    try:
        f = open('./foo.txt', 'r')
    except IOError:
        print('cannot open', arg)
    else: # 必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行
        print(arg, 'has', len(f.readlines()), 'lines')#1 has 2 lines
        f.close()

def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
#简单抛出一个异常 raise
#raise NameError('HiThere') #raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("--division by zero!")
    else:
        print("--result is", result)
    finally:#有没有发生异常，finally 子句都会执行
        print("--executing finally clause")
divide(2, 1)#--result is 2.0
#--executing finally clause
divide(2, 0)#--division by zero!
#--executing finally clause
#关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
#执行完毕后 内部会关闭文件
with open("foo.txt") as f:
    for line in f:
        print(line, end="")
#Shawn
#123
#---------------------------------面向对象 Class
#self代表类的实例，而非类
#普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
#self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self
#__private_attrs：两个下划线开头，声明该属性为私有
#__private_method：两个下划线开头，声明该方法为私有方法
# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __div__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w): #构造方法
        self.name = n
        self.age = a
        self.__weight = w
    def func(shawn): #self 不是 python 关键字，可以换成 shawn
        print(shawn)#<__main__.Test object at 0x0529F870> 类的实例
        print(shawn.__class__)#<class '__main__.Test'> 指向类
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))#shawn 说: 我 33 岁。
t = people('shawn',33, 80)
t.func()
t.speak()

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))#ken 说: 我 10 岁了，我在读 3 年级
s = student('ken',10, 60, 3)
s.speak()
super(student,s).speak()#ken 说: 我 10 岁。 - 直接调用student的父级people的speak(用子类对象调用父类已被覆盖的方法)

#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
    def __foo(self):          # 私有方法
        print('这是私有方法')

    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
#我叫 Tim，我是一个演说家，我演讲的主题是 Python
test.foo()
#这是公共方法
#这是私有方法

#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):#和 JAVA Class中 toString()方法是 相同的功能
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,other):#运算符重载
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

#---------------------------------操作系统接口
import os
#返回当前的工作目录
print (os.getcwd())#D:\xampp\htdocs\java\shawn\demo-python3\src\main\python
#执行系统命令 mkdir
#print (os.system('mkdir new_folder'))#1
#修改当前的工作目录
#print (os.chdir('D:/xampp/htdocs/java/shawn/demo-python3/src/main/python/new_folder'))#None
#返回当前的工作目录re.
#print (os.system('mkdir new_folder2'))#0
import glob #lob模块提供了一个函数用于从目录通配符搜索中生成文件列表
print (glob.glob('*.py'))#['Hellowold.py']
#命令行参数
print(sys.argv)#['D:/xampp/htdocs/java/shawn/demo-python3/src/main/python/Hellowold.py']
#sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息
sys.stderr.write('Warning, log file not found starting a new one\n')
#Warning, log file not found starting a new one
#脚本的定向终止
#sys.exit()
#访问 互联网 以及处理网络通信协议
#从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib

#数据压缩
import zlib
s = b'witch which has which witches wrist watch'
print (len(s))#41
t = zlib.compress(s)
print (len(t))#37
print (zlib.decompress(t))#b'witch which has which witches wrist watch'
print (zlib.crc32(s))#226805979

#---------------------------------多线程
#常用的两个模块为 thread(已被废弃) 重命名为_thread, threading(推荐使用)
#_thread 模块中的start_new_thread()函数来产生新线程
    # function - 线程函数。
    # args - 传递给线程函数的参数,他必须是个tuple类型。
    # kwargs - 可选参数
import _thread
import time
# 为线程定义一个函数
# def print_time( threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
# try: # 创建两个线程
#     _thread.start_new_thread( print_time, ("Thread-1", 1, ) )
#     _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
# except:
#     print ("Error: 无法启动线程")
# while 1:
#     pass
#Thread类提供了以下方法:
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

#线程模块
#threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
#threading.currentThread(): 返回当前的线程变量
#threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程
#threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果
#使用 threading 模块创建线程
#我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程
# import threading
# import time
# exitFlag = 0
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()#等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
# thread2.join()#
# print ("退出主线程")
# 开始线程：Thread-1
# 开始线程：Thread-2
# Thread-1: Mon May 21 22:42:25 2018
# Thread-2: Mon May 21 22:42:26 2018
# Thread-1: Mon May 21 22:42:26 2018
# Thread-1: Mon May 21 22:42:27 2018
# Thread-1: Mon May 21 22:42:28 2018
# Thread-2: Mon May 21 22:42:28 2018
# Thread-1: Mon May 21 22:42:29 2018
# 退出线程：Thread-1
# Thread-2: Mon May 21 22:42:30 2018
# Thread-2: Mon May 21 22:42:32 2018
# Thread-2: Mon May 21 22:42:34 2018
# 退出线程：Thread-2
# 退出主线程

#线程同步
# Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步
#将其操作放到 acquire 和 release 方法之间
# import threading
# import time
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开启线程： " + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # 释放锁，开启下一个线程
#         threadLock.release()
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
# threadLock = threading.Lock()
# threads = []
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")
# 开启线程： Thread-1
# 开启线程： Thread-2
# Thread-1: Mon May 21 22:57:32 2018
# Thread-1: Mon May 21 22:57:33 2018
# Thread-1: Mon May 21 22:57:34 2018
# Thread-2: Mon May 21 22:57:36 2018
# Thread-2: Mon May 21 22:57:38 2018
# Thread-2: Mon May 21 22:57:40 2018
# 退出主线程

#线程优先级队列（ Queue）
#线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，
# 和优先级队列 PriorityQueue
# 这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
# Queue 模块中的常用方法:
    # Queue.qsize() 返回队列的大小
    # Queue.empty() 如果队列为空，返回True,反之False
    # Queue.full() 如果队列满了，返回True,反之False
    # Queue.full 与 maxsize 大小对应
    # Queue.get([block[, timeout]])获取队列，timeout等待时间
    # Queue.get_nowait() 相当Queue.get(False)
    # Queue.put(item) 写入队列，timeout等待时间
    # Queue.put_nowait(item) 相当Queue.put(item, False)
    # Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    # Queue.join() 实际上意味着等到队列为空，再执行别的操作
# import queue
# import threading
# import time
# exitFlag = 0
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print ("退出线程：" + self.name)
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
# # 等待队列清空
# while not workQueue.empty():
#     pass
# # 通知线程是时候退出
# exitFlag = 1
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")
# 开启线程：Thread-1
# 开启线程：Thread-2
# 开启线程：Thread-3
# Thread-2 processing One
# Thread-1 processing Two
# Thread-3 processing Three
# Thread-1 processing Four
# Thread-3 processing Five
# 退出线程：Thread-2
# 退出线程：Thread-3
# 退出线程：Thread-1
# 退出主线程

#---------------------------------XML解析
#有三种方法解析XML，SAX，DOM，以及ElementTree
#标准库包含SAX解析器 SAX (simple API for XML )
#sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler
# startDocument()方法 文档启动的时候调用。
# endDocument()方法 解析器到达文档结尾时调用。
# startElement(name, attrs)方法 遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
# endElement(name)方法 遇到XML结束标签时调用。

# xml.sax.make_parser( [parser_list] ) 创建一个新的解析器对象并返回
# 参数说明: parser_list - 可选参数，解析器列表

# xml.sax.parse( xmlfile, contenthandler[, errorhandler]) 创建一个 SAX 解析器并解析xml文档
# 参数说明:
# xmlfile - xml文件名
# contenthandler - 必须是一个ContentHandler的对象
# errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象

# xml.sax.parseString(xmlstring, contenthandler[, errorhandler])创建一个XML解析器并解析xml字符串
# 参数说明:
# xmlstring - xml字符串
# contenthandler - 必须是一个ContentHandler的对象
# errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
import xml.sax
class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print ("*****Movie*****")
            title = attributes["title"]
            print ("Title:", title)
    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print ("Type:", self.type)
        elif self.CurrentData == "format":
            print ("Format:", self.format)
        elif self.CurrentData == "year":
            print ("Year:", self.year)
        self.CurrentData = ""
    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
if ( __name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler( Handler )
    parser.parse("movies.xml")
# *****Movie*****
# Title: Enemy Behind
# Type: War, Thriller
# Format: DVD
# Year: 2003
# *****Movie*****
# Title: Transformers
# Type: Anime, Science Fiction
# Format: DVD
# Year: 1989
# *****Movie*****
# Title: Trigun
# Type: Anime, Action
# Format: DVD
# *****Movie*****
# Title: Ishtar
# Type: Comedy
# Format: VHS
print ("xml.dom解析xml")
#xml.dom解析xml
from xml.dom.minidom import parse
import xml.dom.minidom
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print ("Root element : %s" % collection.getAttribute("shelf"))
# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")
# 打印每部电影的详细信息
for movie in movies:
    print ("*****Movie*****")
    if movie.hasAttribute("title"):
        print ("Title: %s" % movie.getAttribute("title"))
    type = movie.getElementsByTagName('type')[0]
    print ("Type: %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print ("Format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print ("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print ("Description: %s" % description.childNodes[0].data)
# Root element : New Arrivals
# *****Movie*****
# Title: Enemy Behind
# Type: War, Thriller
# Format: DVD
# Rating: PG
# Description: Talk about a US-Japan war
# *****Movie*****
# Title: Transformers
# Type: Anime, Science Fiction
# Format: DVD
# Rating: R
# Description: A schientific fiction
# *****Movie*****
# Title: Trigun
# Type: Anime, Action
# Format: DVD
# Rating: PG
# Description: Vash the Stampede!
# *****Movie*****
# Title: Ishtar
# Type: Comedy
# Format: VHS
# Rating: PG
# Description: Viewable boredom
#---------------------------------JSON 数据解析
# json.dumps(): 对数据进行编码
# json.loads(): 对数据进行解码
# Python  编码为 JSON 类型转换对应表：
# Python	                                JSON
# dict	                                    object
# list, tuple	                            array
# str	                                    string
# int, float, int- & float-derived Enums	number
# True	                                    true
# False	                                    false
# None	                                    null
# JSON 解码为 Python 类型转换对应表：
# JSON	            Python
# object	        dict
# array	            list
# string	        str
# number (int)	    int
# number (real)	    float
# true	            True
# false	            False
# null	            None

import json
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Shawn',
    'url' : 'http://www.Shawn.com'
}
json_str = json.dumps(data)#对数据进行编码
print ("Python 原始数据：", repr(data))
#Python 原始数据： {'no': 1, 'name': 'Shawn', 'url': 'http://www.Shawn.com'}
print ("JSON 对象：", json_str)
#JSON 对象： {"no": 1, "name": "Shawn", "url": "http://www.Shawn.com"}

# Python 字典类型转换为 JSON 对象
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])#data2['name']:  Shawn
print ("data2['url']: ", data2['url'])#data2['url']:  http://www.Shawn.com
#从文件解析 -  json.dump() 和 json.load() 来编码和解码JSON数据
# 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)
# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)

#---------------------------------日期和时间

from datetime import date
now = date.today()
print (now)#2018-05-20
print (now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
#05-20-18. 20 May 2018 is a Sunday on the 20 day of May.
birthday = date(1964, 7, 31)
print (birthday) #1964-07-31
age = now - birthday
print (age) #19651 days, 0:00:00
print (age.days) #19651

import time
ticks = time.time()
print ("当前时间戳为:", ticks)#当前时间戳为: 1527171285.2309587

#获取当前时间
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
#本地时间为 : time.struct_time(tm_year=2018, tm_mon=5, tm_mday=24, tm_hour=22, tm_min=30, tm_sec=23,
    # tm_wday=3, tm_yday=144, tm_isdst=0)
# 属性	    值
# tm_year	    2008
# tm_mon	    1 到 12
# tm_mday	    1 到 31
# tm_hour	    0 到 23
# tm_min	    0 到 59
# tm_sec	    0 到 61 (60或61 是闰秒)
# tm_wday	    0到6 (0是周一)
# tm_yday	    一年中的第几天，1 到 366
# tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1

#最简单的获取可读的时间模式的函数是asctime()
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)#本地时间为 : Thu May 24 22:32:36 2018

#格式化日期
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#2018-05-24 22:33:26
# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))#Thu May 24 22:33:26 2018
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))#1459175064.0

#python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

#获取某月日历
import calendar
cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)
# January 2016
# Mo Tu We Th Fr Sa Su
# 1  2  3
# 4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31


#---------------------------------

