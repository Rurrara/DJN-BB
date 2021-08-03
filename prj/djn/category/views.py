from rest_framework.views import APIView
from rest_framework.response import Response

from category.models import Category
from category.serializers import CategorySerializer
from rest_framework.decorators import api_view

from item.models import Item
from item.serializers import ItemSerializer


@api_view(['GET'])
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({'error': None, 'categories': serializer.data})

@api_view(['GET'])
def list_cat_items(request, id):
    try:
        cat = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"error": "Category doesn't exist"}, status=400)

    items = Item.objects.filter(categories__id=id, ended=False, active=True)
    serializer = ItemSerializer(items, many=True)
    return Response({'error': None, 'items': serializer.data})

