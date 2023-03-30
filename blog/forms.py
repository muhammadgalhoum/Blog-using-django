from django import forms
from .models import *


class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control',
			'placeholder': 'Comment here!',
			'rows': 2,
			'cols': 50
		}))

	class Meta:
		model = Comment
		fields = ['content']


class ContactForm(forms.ModelForm):
  
	class Meta:
		model = Contact
		fields = ['name','email','message']


class NewsletterForm(forms.ModelForm):
  
	class Meta:
		model = Newsletter
		fields = ['email']