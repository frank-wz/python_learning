# count = 1
# while count < 4:
#     print(count)
#     count += 1
#     if count ==3:break
# else:
#     print(666)

'''
7、使用while循环输出 1 2 3 4 5 6 8 9 10
8、求1-100的所有数的和（三种方法）
9、输出1-100内的所有奇数（两种方法）
10、输出1-100内的所有偶数（两种方法）
11、求1-2+3-4+5...99的所有数的和
12、用户登录（三次输错机会）切每次输错时想视剩余错误次数（提示：使用字符串格式化）
'''
# 7
# n = 1
# while n < 11:
#     if n != 7:
#         print(n)
#     n += 1

# n = 1
# while n < 11:
#     if n == 7:
#         n += 1
#     else:
#         print(n)
#         n += 1

# n = 1
# while n < 11:
#     if n == 7:
#         n += 1 #必须要有这个，否则N值一直是6，下面的print 和 n+=1不执行？无限循环
#         continue
#     print(n)
#     n += 1

# 8
# sum1 = 0
# n = 1
# while n < 101:
#     sum1 += n
#     n += 1
# print(sum1)

# sum2 = 0
# n = 1
# while True:
#     sum2 += n
#     n += 1
#     if n == 101:
#         print(sum2)
#         break

# sum2 = 0
# n = 1
# while True:
#     sum2 += n
#     n += 1
#     if n == 101:
#         break
# print(sum2)

# 11
# count = 0
# n = 1
# while n < 100:
#     if n % 2 == 1:
#         count += n
#     else:
#         count -= n
#     n += 1
# print(count)

# 另一个思路是求奇数的和，偶数的和，相减

# 12
# n=1
# while n < 4:
#     username = input('请输入用户名')
#     password = input('请输入密码')
#     if username == 'abc' and password == 'def':
#         print('登陆成功')
#         break
#     else:
#         print('用户名或密码错误，请重新输入，已使用%d次，还剩%d次' % (n, 3-n))
#     n += 1

# 思考题：如果机会用完了，可以在个用户选择继续的机会。
# 如果继续，再给三次机会，如果不继续退出循环，并且说一句：要不要脸呀！
# msg = 1
# while msg != 'Q':
#     n=1
#     while n < 4:
#         username = input('请输入用户名')
#         password = input('请输入密码')
#         if username == 'abc' and password == 'def':
#             print('登陆成功')
#             break
#         else:
#             print('用户名或密码错误，请重新输入，已使用%d次，还剩%d次' % (n, 3-n))
#         n += 1
#     msg = input('按任意键继续重试,按Q退出')
# else:
#     print("要不要脸呀！")