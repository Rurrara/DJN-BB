from django import forms

from category.models import Category

class CatAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_category', 'description_category']
