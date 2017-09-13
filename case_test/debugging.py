#调试
#print()
# def foo(s):
#     n=int(s)
#     print('>>n=%d' %n)
#     return 10/n
#
# def main():
#     foo('0')
# main()

#断言,assert()
# def foo(s):
#     n=int(s)
#     assert n!=0,'n is zero!'
#     return 10/0
# def main():
#     foo('0')
# main()

#logging
# import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d' %n)
# print(10/n)

#pdb
import pdb
s='0'
n=int(s)
pdb.set_trace()
print(10/n)















