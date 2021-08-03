from rest_framework import serializers

from user.models import User
from item.serializers import ItemSerializer

class UserSerializer(serializers.ModelSerializer):
    watched_items = ItemSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['username', 'contact_telephone', 'watched_items', 'balance']

