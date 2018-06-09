from django.shortcuts import render

# Create your views here.

from . import tasks

r = tasks.add.delay(3, 5)  # 执行这一行就能在worker的日志中看到运行状况
r.wait()









