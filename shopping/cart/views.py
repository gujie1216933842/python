from django.shortcuts import render

# Create your views here.

class cart():
    def index(request):
        render(request,'cart/cart.html')
