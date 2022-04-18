from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields=['name','email','message']
        
                
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        