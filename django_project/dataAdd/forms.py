from django import forms
from .models import DataAdd



class data_add(forms.ModelForm):
    class Meta:
        model= DataAdd
        fields = ['birthdate','country','facebookprofile']