from django.shortcuts import render

# Create your views here.

class user():
    def login(request):
        render(request,'user/login')
