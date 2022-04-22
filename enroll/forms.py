from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','Address']
        widgets = {
            'name':forms.TextInput(),
            'email':forms.EmailInput(),
            'password': forms.PasswordInput(render_value=True),
            'Address': forms.TextInput()
        }