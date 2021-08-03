from django import forms
from django.forms import Textarea

from item.models import Item
from category.models import Category

class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title_item', 'description_item', 'price', 'categories', 'active', 'picture']

        widgets = {
            'description_item': Textarea(attrs={'cols': 80, 'rows': 10}),
        }

        categories = forms.ModelMultipleChoiceField(
            queryset = Category.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
