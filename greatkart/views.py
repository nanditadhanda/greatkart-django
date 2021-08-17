from django.shortcuts import render
from store.models import Product
# home function
def home(request):
    products = Product.objects.all().filter(is_available=True)

    #dictionary
    context = {
        'products':products,
    }

    return render(request, 'home.html', context)
