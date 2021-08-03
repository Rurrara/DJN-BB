from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:item_id>/add_review', views.add_review_form, name='add_review_form'),

    path('<int:id>/update_form', views.update_item_form, name='update_item_form'),
    path('<int:id>/update_item', views.update_item, name='update_item'),
    path('<int:id>/picture', views.item_picture, name='item_picture'),

    path('add', views.add_item, name='add_item'),
    path('list', views.list_items, name='list_items'),
    path('<int:id>', views.item_info, name='item_info'),
    path('<int:id>/buy', views.buy_item, name='buy_item'),

    path('<int:id>/wl/add', views.add_to_watch_list, name='add_to_watch_list'),
    path('<int:id>/wl/rem', views.remove_from_watch_list, name='remove_from_watch_list'),

    path('<int:id>/rev/set', views.set_review, name='set_review'),
    path('<int:id>/rev/rem', views.rem_review, name='rem_review'),

]


