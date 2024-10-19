from django.shortcuts import render

# Create your views here.
def homepage_without_user(request):
    return render(request, 'homepage_without_user.html')