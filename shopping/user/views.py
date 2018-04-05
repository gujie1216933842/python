from django.shortcuts import render
import sys

# Create your views here.

class user():
    def login(request):
        return render(request, 'user/login.html')

    def register(request):
        return render(request, 'user/register.html')


    def register_handler(request):
        #接收用户输入
        post = request.POST
        uname = post.get('user_name')
        print(uname)
        sys.exit()


    def register_exist(request):
        post = request.POST
        uname = post.get('user_name')
        print(uname)
        #sys.exit





