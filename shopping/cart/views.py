from django.shortcuts import render


# Create your views here.

class cart():
    def index(request):
        return render(request, 'cart/cart.html', {'page_name': 1})
