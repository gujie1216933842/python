from django.db import models

Type = {
    '1': '新',
    '2': '老',
    '3': '外联用户',
}

class UserInfo(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(choices=Type)

    raw_add_time = models.DateTimeField()