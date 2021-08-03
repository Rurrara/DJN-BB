from rest_framework import serializers

from review.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['bought_item', 'review_text', 'rating']

