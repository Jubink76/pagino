from django.shortcuts import render

# Create your views here.
def homepage_before_login(request):
    return render(request, 'homepage_before_login.html')

def homepage_after_login(request):
    return render(request,'homepage_after_login')

def all_products(request):
    return render(request,'all_products.html')

def single_product(request):
    return render(request,'single_product.html')