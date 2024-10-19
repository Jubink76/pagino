from django.shortcuts import render
from log_reg_app.models import UserTable
# Create your views here.
def admin_users(request):
    user_data = UserTable.objects.all() 
    return render(request,'admin_users.html',{'data':user_data})