from django.shortcuts import render

# Create your views here.

#控制器中以方法的方式
# def index(request):
#     return  render(request,'goods/index.html')


#控制器中以类的方式
class goods():
    def index(request):
        return render(request,'goods/index.html')

    def detail(request):
        return render(request,'goods/detail.html')







