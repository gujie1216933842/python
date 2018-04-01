from django.shortcuts import render

# Create your views here.

# class index():
#     def get(self):

def index(request):
    return  render(request,'goods/index.html')


