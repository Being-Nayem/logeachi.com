from django.shortcuts import render
from home.models import Banner, Subscribers
from accounts.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Category, Subcategory, Product
from django.contrib.auth.decorators import login_required



def home(request):
    sliders= Banner.objects.filter(banner_type='slider')
    newslatters= Banner.objects.filter(banner_type='newslatter')
    tosters = Banner.objects.filter(banner_type='toster')
    categories = Category.objects.all()
    products = Product.objects.all()
    best_solds = Product.objects.order_by('-product_sold_quantity')[:5]
    
    
    context = {
    'sliders': sliders,
    'newslatters': newslatters,
    'tosters': tosters,
    'categories': categories,
    'products': products,
    'best_solds': best_solds,
    }
    return render(request, 'home/home.html', context)

def registerSunbscriberView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Check if a user with the given email exists
        user_exists = Subscribers.objects.filter(email=email).exists()
        
        if not user_exists:
            # If the user does not exist, create a new Subscriber
            Subscribers.objects.create(email=email)
            messages.error(request, "You have successfully subscribed to Logeachi Dot Com newslatter.")
            return redirect('home')
        else:
            messages.error(request, "This e-mail is already subscribed")
            return redirect('home')
    
    return redirect('home')





# Search options for keywords
def search(request):
    get_method =  request.GET.copy()
    key_words = get_method.get('keywords') or None
    product = Product.objects.all()
    products = []  
    print(key_words)
    if key_words:
        key_word = get_method.get('keywords')
        products = product.filter(product_description__icontains=key_word)
    

    context= {
        'categories': Category.objects.all(),
        'products': products
    }

    return render(request, 'products/category-products.html', context)

