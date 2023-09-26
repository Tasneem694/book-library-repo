from .models import *
from django import forms

class UpdateUser(forms.ModelForm):
    class Meta:
        model=registers
        fields='__all__'

class NewBook(forms.ModelForm):
    class Meta:
        model=books
        fields=['book_name']

class UpdateBook(forms.ModelForm):
    class Meta:
        model=books
        fields='__all__'



