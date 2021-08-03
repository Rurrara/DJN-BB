from django import forms

from review.models import Review

class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
