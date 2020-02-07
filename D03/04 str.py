# 对字符串下面这两部分操作：形成的都是一个新的字符串，与原来的字符串没有关系。
# 第一部分：索引切片步长
# 字符串是有序的
# 按照索引取值，取出来的都是一个字符，形成的字符串
# s1 = 'python1期骑士计划'
# s2 = s1[0]
# print(s2, type(s2))
# s3 = s1[2]
# s4 = s1[4]
# s5 = s1[-1]
# # 按切片取值，顾头不顾尾
# s6 = s1[0:5]
# s61 = s1[:5]
# print(s6,s61)
# print(s1[1:7])
# s7 = s1[6:-1]
# s71 = s1[6:]
# s72 = s1[6:-2]
# print(s7, s71 , s72)

# 按照切片+步长
# s8 = s1[:5:2]
# s9 = s1[1::2]
# print(s8,s9)
# 如果想倒叙取值，加一个反向步长
# s10 = s1[-1:-5:-1]
# print(s10)


# 第二部分：字符串的常用方法。
# capitalize() 首字母大写 ***
# name = 'oldBOy'
# print(name.capitalize())
#
# center 字符串剧中前后填充自定义的字符 **
# print(name.center(20,'*')) #*******oldBOy*******

# upper lower 全大写 全小写 *****
# print(name.upper())
# print(name.lower())
# 应用举例：
# username = input('请输入用户名')
# code = 'ASfer'
# your_code = input('请输入验证码：').upper()
# if username == 'alex' and your_code== code:
#     print('账号密码及验证码输入正确')
#
# startswith  endswith 判断是否以  为开头 结尾     ****
# print(name.startswith("o"))
# print(name.startswith("ol"))
# print(name.startswith("oldBOy"))
# print(name.startswith("B",3))#B是否是从索引位置3开头的
# print(name.startswith("ld",1,5))#ld是否是从所以位置1-5（不含5）的一段开头
#
# print(name.endswith("o"))
#
# swapcase() 大小写转化 **
# print(name.swapcase())

# s1 = 'alex wusir*taibai6nvshen'
# #title 非字母隔开的每个部分的首字母大写 **
# print(s1.title())
#
# find 通过元素找索引, 找到第一个就返回，没有此元素则返回-1 *****
# print(name.find('B')) #3
# print(name.find('ld')) #1
# print(name.find('w')) #-1
# print(name.find('d',1,-1)) #2
# print(name.index('q')) #报错
#
# index 通过元素找索引, 找到第一个就返回，没有此元素则报错 *****
#
#
# name = '\t    oldboy\n'
# strip 默认去除字符串前后的空格，换行符，制表符 *****
# name1 = '*alex**'
# name2 = 'weralexqwe'
# print(name.strip())
# print(name1.strip('*')) # alex
# print(name2.strip('ewr')) # alexq 可以指定字符去除，直到没有任意字符为止
# lstrip()  rstrip() 只去除左侧 右侧的空白或指定字符
# 举例
# username = input('请输入用户名：').strip()
# if username = 'alex':
#     print('登陆成功')
#
# s1 = 'alex wusir taibai'
# # split #将字符串分割成列表
# l1 = s1.split() #默认按照空格分割
# print(l1) #['alex', 'wusir', 'taibai']
# s2 = 'alex，wusir，taibai' #中文，
# print(s2.split('，')) #['alex', 'wusir', 'taibai']
# s3 = '，alex，wusir，taibai'
# print(s3.split('，')) #['', 'alex', 'wusir', 'taibai']
# s4 = ' alex wusir taibai'
# print(s4.split()) #['alex', 'wusir', 'taibai'] 算是个bug，注意下
# print(s4.split(' ')) #['', 'alex', 'wusir', 'taibai']
# s5= 'alexlwle'
# print(s5.split('l',1)) #['a', 'exlwle'] 可设置分割次数
#
# #join 自定制连接符，将可迭代对象中的元素连接起来    *****
# str1 = 'alex'
# s2= '*'.join(str1)
# print(s2) #a*l*e*x
#
# str2 = 'alex 是创始人，alex很nb，alex...'
# #replace 替换 *****
# s3 = str2.replace('alex','SB',1) #替换次数可设置
# print(s3) #SB 是创始人，alex很nb，alex..

# #格式化输出：format
# s1 = '我叫{}，今年{}，性别{}'
# #三种方式
# s2 = '我叫{}，今年{}，性别{}'.format('taibai','28','male')
# print(s2) #我叫taibai，今年28，性别male
# s3 = '我叫{2}，今年{0}，性别{1},我依然叫{2}'.format('28','male','taibai')
# print(s3) #我叫taibai，今年28，性别male,我依然叫taibai
# s3 = '我叫{name}，今年{age}，性别{gender},我依然叫{name}'.format(age='28',gender='male',name='taibai')
# print(s3) #我叫taibai，今年28，性别male,我依然叫taibai

# #is系列
# name= 'taibai123'
# name1= 'a123'
# print(name.isalnum()) #数字或字母组成
# print(name1.isdigit()) #判断全部是有整数组成
# print(name.isalpha()) #全部由字母组成
#
# #公共方法
# name = 'alexaaaa'
# print(name.count('a')) # 5  有切片
# print(len(name)) # 8 字符个数，注意区别于索引下标
#
# s1 = 'fdjsafjsdkla'












