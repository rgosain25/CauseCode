__author__ = 'Rahul G'
from django import forms
class NameForm(forms.Form):
    phone_number = forms.CharField()
    paragraph_text = forms.CharField()
