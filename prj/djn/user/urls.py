from django.urls import path, re_path

from . import views

urlpatterns = [
    path('self', views.get_user_info, name='view_user_info'),
    path('completed', views.get_bought_items, name='get_bought_items'),

    path('<int:id>/items', views.get_user_items, name='get_user_items'),
    path('<int:id>/reviews', views.get_user_reviews, name='get_user_reviews'),
]

