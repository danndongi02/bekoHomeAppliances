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
    
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__slug=active_category)
    
    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }
    return render(request, 'core/shop.html', context)