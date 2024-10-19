from django.shortcuts import render,redirect
from log_reg_app.models import UserTable
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.

def homepage_before_login(request):

    return render(request,'homepage_before_login.html')

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('homepage_after_login')
        else:
            messages.error(request,"username or password is invalid")
            return render(request,'user_login.html')
    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('homepage_after_login')
    return render(request,'user_login.html')

def user_signup(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        
        try:
            #validate require fields
            if UserTable.objects.filter(username=username).exists(): # user name is already exist or not
                messages.error(request,"Username is already taken")
                return render(request,'user_signup.html')
        

            if UserTable.objects.filter(email=email).exists():  # eamil id is already exist or not
                messages.error(request, "Email id is already taken")
                return render(request,'user_signup.html')
            
            if not all([first_name,last_name,username,email,password,phone_number,gender]): # checking all the fields are entered
                messages.error(request, "All fields are required")
                #return render(request,'user_signup.html')
            

            if password != confirm_password: # rechecking the password correct or not
                messages.error(request,"Invalid password")
                return render(request,'user_signup.html')
            

            user = UserTable(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email = email,
                phone_number = phone_number,
                gender = gender
            )
            user.set_password(password) # hash password
            user.save()
            messages.success(request,"Account created successfully")
            return redirect('user_login')
        
        except Exception as e:
            messages.error(request,f"Error occured while creating the account: {e}")
            return render(request, 'user_signup.html')

    return render(request,'user_signup.html')


def homepage_after_login(request):
    return render(request,'homepage_after_login.html')

def user_logout(request):
    logout(request)
    return redirect('homepage_before_login')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password = password)
        
        if user is not None and user.is_superuser:
            login(request,user)
            messages.success(request,f"{username}logined successfully." )
            return redirect(reverse('admin_dashboard'))
        else:
            messages.error(request,"You don't have admin privileges")
            return redirect('admin_login')
        
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('admin_dashboard')
            else:
                messages.error(request,"you dont have admin privileges")
                return redirect('admin_login')

    return render(request,'admin_login.html')