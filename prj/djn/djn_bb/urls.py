"""djn_bb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from .views import login_view, home_view, search_cat_form, search_item_form, index_view

from item.views import feed, add_item_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_view'),

    path('search_item/', search_item_form, name='search_item_form'),
    path('search_cat/', search_cat_form, name='search_cat_form'),

    path('feed/', feed, name='centrifugo_feed'),
    path('add_item_form/', add_item_form, name='add_item_form'),

    path('api/cat/', include('category.urls')),
    path('api/item/', include('item.urls')),
    path('api/user/', include('user.urls')),

    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
]

