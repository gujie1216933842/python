from django.shortcuts import render


# Create your views here.
class order():
    def index(request):
        return render(request, 'order/user_center_order.html')

    def address(request):
        return render(request,'order/user_center_site.html')
