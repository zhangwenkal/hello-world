import os

def get_super_path():
    pwd=os.path.split(os.path.realpath(__file__))[0]
    #super_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+'..')
    super_path=os.path.abspath(os.path.dirname(pwd))
    return super_path



