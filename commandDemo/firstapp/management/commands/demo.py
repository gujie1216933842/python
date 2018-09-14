# -*- coding: utf-8 -*-
'''
Python的每个新版本都会增加一些新的功能，或者对原来的功能作一些改动。
有些改动是不兼容旧版本的，也就是在当前版本运行正常的代码，到下一个版本运行就可能不正常了
目的在于做版本的兼容性
'''
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
import logging

logger = logging.getLogger('ant_delivery_package')


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info('hahahaha')
        logger.debug('aaaaa')
        logger.error('kkkkk')
        logger.fatal('ffffff')
        print 'first command'
