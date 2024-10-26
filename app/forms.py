from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import *

"""
This part creates login form and takes the inputs.
The widgets are optional but it creates a better UI/UX and also good for styling-framworks.
"""
class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(EmailOrUsernameAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Email or Username'

"""
This part creates the user signup/registration form and takes input of those.
The widgets are optional but it creates a better UI/UX and also good for styling-framworks.
"""
# class CustomerRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs = {'class':'form-control'}))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'locality', 'city', 'mobile', 'zipcode', 'password1', 'password2']
        #adding widgets makes it better for UI/UX
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            #'firstname':forms.TextInput(attrs={'class':'form-control'}),
            #'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            #'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }

    # def clean_mobile(self):
    #     mobile = self.cleaned_data.get('mobile')
    #     if not mobile.isdigit():
    #         raise forms.ValidationError("Mobile number should be only digits")
    #     return mobile



#This form gathers the information stated in the fields that is in the "Customer" class
#that we have created in the models.py
# class CustomerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ["firstname", "lastname","email", "locality", "city", "mobile", "zipcode"]
#         #adding widgets makes it better for UI/UX
#         widgets = {
#             'firstname':forms.TextInput(attrs={'class':'form-control'}),
#             'lastname':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.TextInput(attrs={'class':'form-control'}),
#             'locality':forms.TextInput(attrs={'class':'form-control'}),
#             'city':forms.TextInput(attrs={'class':'form-control'}),
#             'mobile':forms.NumberInput(attrs={'class':'form-control'}),
#             'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
#         }