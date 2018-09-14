# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


class test(object):
    @staticmethod
    def get_name():
        return 'class name is test'


    def haha(self):
        return self.get_name()


t = test()
print t.haha()

