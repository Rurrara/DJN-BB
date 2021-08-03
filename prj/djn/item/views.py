from django.shortcuts import render
from rest_framework.response import Response


from item.models import Item
from review.models import Review

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

from item.forms import ItemAddForm
from review.forms import ReviewAddForm

from item.serializers import ItemSerializer

from datetime import datetime

from django.shortcuts import get_object_or_404

from cent import Client


# Create your views here.

centrifugo_url = 'http://127.0.0.1:9003/'
centrifugo_api = '1286dc90-3ecb-43c3-8b57-a30dc6777f1d'


@login_required
def add_item_form(request):
    form = ItemAddForm()
    return render(request, 'addItem.html', {'form': form})

@login_required
def add_review_form(request, item_id):
    form = ReviewAddForm()
    return render(request, 'addReview.html', {'form': form, 'id':item_id})

@login_required
@api_view(['POST'])
def add_item(request):
    form = ItemAddForm(request.POST, request.FILES)
    if not form.is_valid():
        return Response({'error': form.errors})
    new_item = form.save(commit=False)
    new_item.seller = request.user
    new_item.save()
    form.save_m2m()

    client = Client(centrifugo_url, api_key=centrifugo_api, timeout=5)
    item_json = ItemSerializer(new_item).data
    if new_item.active:
        client.publish("feed", {'item': item_json})

    return Response({"success": "Item '{}' created successfully".format(new_item.title_item)})
    

def feed(request):
    items = Item.objects.filter(active=True, ended=False)
    items_json = ItemSerializer(items, many=True).data
    return render(request, 'feed.html', {'items': items_json})


@login_required
def update_item_form(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item not availiable"}, status=400)
    form = ItemAddForm(instance=item)
    return render(request, 'updateItem.html', {'form': form, 'id':id})

@login_required
@api_view(['POST'])
def update_item(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item not availiable"}, status=400)

    if item.seller != request.user:
        return Response({"error": "Can only edit your items"}, status=400)

    form = ItemAddForm(request.POST, request.FILES, instance=item)
    if not form.is_valid():
        return Response({'error': form.errors}, status=400)
    updated_item = form.save(commit=False)
    updated_item.date_edited = datetime.now()
    updated_item.save()
    return Response({"success": "Item '{}' updated successfully".format(item.title_item)})

@api_view(['GET'])
def list_items(request):
    items = Item.objects.filter(ended=False, active=True)
    serializer = ItemSerializer(items, many=True)
    return Response({'error': None, 'items': serializer.data})

@api_view(['GET'])
def item_info(request, id):

    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item doesn't exist"}, status=400)

    if item.active == False or item.ended == True:
        return Response({"error": "Item not availiable"}, status=400)
    serializer = ItemSerializer(item)
    return Response({'error': None, 'item': serializer.data})

@api_view(['GET'])
def item_picture(request, id):

    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item doesn't exist"}, status=400)
    user = request.user
    if item.active == True or item.seller == user:
        return Response({"success": "picture: '{}'".format(item.picture)})
    else:
        return Response({"error": "Item not availiable"}, status=400)


@login_required
@api_view(['GET'])
def add_to_watch_list(request, id):
    user = request.user

    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item doesn't exist"}, status=400)

    user.watched_items.add(item)
    user.save()
    return Response({"success": "Item '{}' added to watch list".format(item.title_item)})

@login_required
@api_view(['GET'])
def remove_from_watch_list(request, id):
    user = request.user

    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item doesn't exist"}, status=400)

    user.watched_items.remove(item)
    user.save()
    return Response({"success": "Item '{}' removed from watch list".format(item.title_item)})


@login_required
@api_view(['POST'])
def set_review(request, id):
    user = request.user

    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item doesn't exist"}, status=400)

    if not item.buyer == user:
        return Response({"error": "Didn't buy this item"}, status=400)
    if item.seller == user:
        return Response({"error": "You cannot buy your item"}, status=400)

    review = Review.objects.filter(bought_item=item)
    if review.count() == 1:
        return Response({'error': 'Already submited review'}, status=400)
    form = ReviewAddForm(request.POST)
    if not form.is_valid():
        return Response({'error': form.errors})

    review = form.save(commit=False)
    review.bought_item=item
    review.author=user
    review.save()
    return Response({"success": "Review added"})


@login_required
@api_view(['GET'])
def rem_review(request, id):
    user = request.user
    try:
        review = Review.objects.get(pk=id)
    except Review.DoesNotExist:
        return Response({"error": "Review doesn't exist"}, status=400)
    review.remove()
    return Response({"success": "Review removed"})

@login_required
@api_view(['GET'])
def buy_item(request, id):
    user = request.user

    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response({"error": "Item doesn't exist"}, status=400)

    if item.active == False or item.ended == True:
        return Response({'error': 'Item not aviliable to buy'}, status=400)
    if (user.balance - item.price) < 0:
        return Response({'error': 'Not enough money'})
    user.balance = user.balance - item.price
    item.buyer = user
    item.ended = True
    item.active = False
    item.save()
    user.save()
    return Response({'success': 'Item bought'})