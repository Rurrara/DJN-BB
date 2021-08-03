from django.shortcuts import render
from rest_framework.response import Response

from user.models import User
from item.models import Item
from review.models import Review

from user.serializers import UserSerializer
from item.serializers import ItemSerializer
from review.serializers import ReviewSerializer


from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
@api_view(['GET'])
def get_user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response({'error': None, 'uesr': serializer.data})


@api_view(['GET'])
def get_user_items(request, id):
    try:
       user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=400)
    items = Item.objects.filter(seller=user, ended=False)
    serializer = ItemSerializer(items, many=True)
    return Response({'error': None, 'items': serializer.data})

@login_required
@api_view(['GET'])
def get_bought_items(request):
    user = request.user
    items = Item.objects.filter(buyer=user)
    serializer = ItemSerializer(items, many=True)
    return Response({'error': None, 'items': serializer.data})

@api_view(['GET'])
def get_user_reviews(request, id):
    try:
       user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=400)
    items = Item.objects.filter(seller=user, ended=True)
    reviews = Review.objects.filter(bought_item__in=items)
#    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response({'error': None, 'reviews': serializer.data})
