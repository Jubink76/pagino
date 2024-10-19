from django.shortcuts import render
from log_reg_app.models import UserTable
# Create your views here.
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def admin_users(request):
    user_data = UserTable.objects.all() 
    return render(request,'admin_users.html',{'data':user_data})

def add_users(request):
    return render(request,'add_users.html')

def edit_users(request):
    return render(request,'edit_users.html')

def admin_category(request):
    return render(request,'admin_category.html')

def add_category(request):
    return render(request,'add_category.html')

def edit_category(request):
    return render(request,'edit_category.html')

def admin_products(request):
    return render(request,'admin_products.html')