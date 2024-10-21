from django.shortcuts import render,redirect,get_object_or_404
from log_reg_app.models import UserTable
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def admin_users(request):
    user_data = UserTable.objects.all() 
    return render(request,'admin_users.html',{'data':user_data})

UserTable = get_user_model()

def add_users(request):
    if request.method == "POST":
        print("POST request received")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')

        print(f"Username: {username}, Email: {email}, Password: {password}, Confirm Password: {confirm_password}")
        # Validate required fields
        if not all([first_name, last_name, username, email, password, phone_number, gender]):
            print("All fields are required")
            messages.error(request, "All fields are required")
            return render(request, 'add_users.html')

        # Check if username or email already exists
        if UserTable.objects.filter(username=username).exists():
            print("Username already taken")
            messages.error(request, "Username is already taken")
            return render(request, 'add_users.html')

        if UserTable.objects.filter(email=email).exists():
            print("email already taken")
            messages.error(request, "Email is already taken")
            return render(request, 'add_users.html')

        # Check if passwords match
        if password != confirm_password:
            print("Passwords do not match")
            messages.error(request, "Passwords do not match")
            return render(request, 'add_users.html')

        # Create the user
        try:
            print("Creating user...")
            user = UserTable.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                gender=gender
            )
            user.phone_number = phone_number
            user.save()
            print("User created successfully, redirecting to admin users page")
            messages.success(request, "User created successfully")
            return redirect('admin_users')

        except Exception as e:
            messages.error(request, f"Error occurred: {e}")
            return render(request, 'add_users.html')
        
    # implement pagination
    users = UserTable.objects.all()
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)

    return render(request, 'add_users.html')


def edit_users(request):
    return render(request,'edit_users.html')

def view_users(request, pk):
    # single user view
    #id = request.GET.get('pk')
    user_detail = get_object_or_404(UserTable,id = pk)

    #user block and unblock
    if request.method == "POST":
        if user_detail.is_blocked:
            user_detail.is_blocked = False
            messages.success(request,f"{user_detail.username} has been unblocked.")
        else:
            user_detail.is_blocked = True
            messages.success(request,f"{user_detail.username} has been blocked.")
        user_detail.save()
        return redirect('view_users', pk = user_detail.id)
    return render(request,'view_users.html',{'record':user_detail})

def admin_category(request):
    return render(request,'admin_category.html')

def add_category(request):
    return render(request,'add_category.html')

def edit_category(request):
    return render(request,'edit_category.html')

def admin_products(request):
    return render(request,'admin_products.html')