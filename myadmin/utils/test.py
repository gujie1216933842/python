import common
import os
'''
此文件仅用于日志测试
'''

class Test(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        common.my_log(self.name, 'first')
        return self.name


aa = Test('daxiong', 12)

aa.getName()
