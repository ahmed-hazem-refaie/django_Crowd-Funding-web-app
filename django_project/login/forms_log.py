from django import forms
from .models import *

class rejesterform(forms.ModelForm):
    # confirmpass = forms.CharField(max_length=20)

    password_confirmation = forms.CharField(
        label='Password confirmation',
        max_length=70,
        widget=forms.PasswordInput(),
        required=True,
    )
    class Meta:

        model=User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields=('f_name','l_name','email','password','phone','profile_pic','gender')

    def clean(self):
        cleaned_data =super(rejesterform,self).clean()

        password=cleaned_data.get('password')
        password_confirmation=cleaned_data.get('password_confirmation')
        print('hhhhhere')

        if password != password_confirmation:
            raise  forms.ValidationError('pass word confirmation must be match')




