from django.urls import path, re_path

from category.views import list_categories, list_cat_items

urlpatterns = [
    path('list', list_categories, name='list categories'),
    path('<int:id>/items', list_cat_items, name='list cat items'),
]

