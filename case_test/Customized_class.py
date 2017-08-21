#定制类
'''
class Student(object):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'Student objcet (name:%s)' %self.name
    __repr=__str__

s=Student('Mick')
print(s)

---------------------------------------------------------------
#__iter__
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1      #初始化两个计数啊，b

    def __iter__(self):
        return self           #实例本身就是迭代对象，返回自身

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b   #计算出下一个值
        if self.a>1000:
            raise StopIteration()
        return self.a              #返回下一个值

# for n in Fib():
#     print(n)
s=Fib()[5]
'''
#__getitem()__方法

# class Fib(object):
#     def __getitem__(self, n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
#
# f=Fib()
# print(f[3],f[100])
#
# l=list(range(12)[5:10])
# print(l)

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
# f=Fib()
# print(f[4])
# print(f[0:5])
# print(f[:10])
# print(f[:10:2])   #没有对step(部长)进行处理

# class Student(object):
#     def __init__(self):
#         self.name='kevin'
#     def __getattr__(self, attr):   #只有在没有找到属性的情况下，才调用 __getattr__
#         if attr=='score':
#             return 88
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# s=Student()
# print(s.name)
# print(s.score)
# print(s.abc)    #没有abc这个属性

#利用完全动态的__getattr__,写出一个链式调用

# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# s=Chain().status.user.timeline.list
# print(s)
#q=Chain().users('michael').repos
#print(q)

#__call__,在实例本身上调用
class Student(object):
    def __init__(self,name):
        self.name=name

    def __call__(self):
        print('My name is %s.' %self.name)
s=Student('Jack')
s()

