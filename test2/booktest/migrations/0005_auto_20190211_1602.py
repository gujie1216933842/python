# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-11 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('hobby', models.CharField(max_length=20, verbose_name='爱好')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='update_time',
        ),
    ]
