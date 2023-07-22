from django.shortcuts import render

from product.models import Product, Category

def homepage(request):
    products = Product.objects.all()[0:8]
    
    context = {
        'products': products
    }
    return render(request, 'core/homepage.html', context)

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'core/shop.html', context)