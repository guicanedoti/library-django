from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import (Book, Author)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year_published', 'category', 'description', 'publisher', 'cover']
        widgets = {
            'cover': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'birthdate', 'rating', 'description']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }