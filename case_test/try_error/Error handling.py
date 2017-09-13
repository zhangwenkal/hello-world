#错误处理
# def foo():
#     r=some_function()
#     if r==-1:
#         return (-1)
#     #do something
#     return r

# def bar():
#     r=foo()
#     if r==(-1):
#         print('Error')
#     else:
#         pass
# bar(6)

#try
# try:
#     print('try....')
#     r=10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')

#print(10/0)

# try:
#     print('try....')
#     r=10/int('a')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# finally:
#     print('finally....')
# print('END')

# try:
#     r=10/int('b')
#     print('result:',r)
# except ValueError as e:
#     print("ValueError:",e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# else:
#     print('no error')
# finally:
#     print('finally....')
# print('END')

#python的错误其实也是class,所有的错误类型都承自BaseException
# def foo():
#     pass
# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')

#try except跨域多层调用，main()
# def foo(s):
#     return 10/int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main(w):
#     try:
#         m=bar(w)
#         print('result:',m)
#     except Exception as e:
#         print('Error:',e)
#     finally:
#         print('finally....')
#
# print(main('q'))

#调用堆栈，logging































































