from admn.models import registers,books
from django import forms

class UpdateStudent(forms.ModelForm):
    class Meta:
        model=registers
        fields=['email','password','name']

class UpdateBorrow(forms.ModelForm):
    class Meta:
        model=books
        fields=['is_borrowed','retrn_dt']


