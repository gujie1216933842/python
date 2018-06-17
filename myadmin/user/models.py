from django.db import models

class UserInfo(models.Model):
    Type = {
        '1': '新',
        '2': '老',
        '3': '外联用户',
    }
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(choices=Type, max_length=30)

    raw_add_time = models.DateTimeField()