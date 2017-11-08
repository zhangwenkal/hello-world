__author__ = 'Administrator'
import logging
def use_logging(leveal):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if leveal=="warn":
                logging.warn("%s is running" %func.__name__)
            return func(*args)
        return wrapper
    return decorator

@use_logging(leveal='warn')
def foo(name='foo'):
     print("i am %s" % name)

foo()