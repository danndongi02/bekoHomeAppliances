from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from product.models import Product, Category
from .forms import SignUpForm

def homepage(request):
    products = Product.objects.all()[0:8]
    
    context = {
        'products': products
    }
    return render(request, 'core/homepage.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('/')
        
    else:
        form = SignUpForm()
        
    context = {
        'form': form
    }
        
    return render(request, 'core/signup.html', context)

@login_required
def myAccount(request):
    return render(request, 'core/myaccount.html')

@login_required
def account_edit(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()
        
        return redirect('myAccount')
        
    return render(request, 'core/account_edit.html')

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__slug=active_category)
        
    query = request.GET.get('query', '')
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }
    return render(request, 'core/shop.html', context)

def about(request):
    return render(request, 'core/about.html')
