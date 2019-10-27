from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('content', 'rating', 'anonymous')
		widgets = {
            'content' : forms.Textarea(attrs={
                'maxlength': '800',
            }),
        }

class UpdateReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('content', 'rating', 'anonymous')
		widgets = {
            'content' : forms.Textarea(attrs={
                'maxlength': '800',
            }),
        }