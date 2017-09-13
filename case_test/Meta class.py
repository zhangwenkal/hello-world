#元类
#动态语言和静态语言最大的不同就是，函数和类的定义，不是编译的时候定义，而是运行的时候动态的创建
from hello import Hello
# h=Hello()
# h.hello()
# print(type(Hello))
# print(type(h))

def fn(self,name='world'):  #先定义函数
    print('Hello,%s' %name)
Hello=type('Hello',(object,),dict(hello=fn))  #创建Hello class
h=Hello()
h.hello()
print(type(Hello))
print(type(h))