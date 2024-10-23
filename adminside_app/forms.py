from django import forms
from .models import CategoryTable

# creating a form to handle category data
class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryTable
        fields = ['category_name','description','category_image']
