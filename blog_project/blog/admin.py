from django.contrib import admin

# Register your models here.
from .models import *


# 自定义
class AticleAdmin(admin.ModelAdmin):
    # fields = ('title', 'desc', 'content')  # 后台管理只显示这三项,下面注册需要用自定义的类名
    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',

        )





'''
属性:
exclude = ()  与fields相反
fieldsets  
list_display = ()   在列表中显示几个配置
list_dispaly_links = ()  列表可点击
list_editable = ()  在列表中可修改
list_filter = ()    
inlines


'''



admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, AticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
