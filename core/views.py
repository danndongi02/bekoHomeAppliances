from django.shortcuts import render

from product.models import Product

def homepage(request):
    products = Product.objects.all()[0:8]
    
    context = {
        'products': products
    }
    return render(request, 'core/homepage.html', context)