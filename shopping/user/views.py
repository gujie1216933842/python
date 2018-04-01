from django.shortcuts import render


# Create your views here.

class user():
    def login(request):
        return render(request, 'user/login.html')
