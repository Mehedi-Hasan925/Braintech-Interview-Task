from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from app_login import models


# Forms Here
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Email','class':'mb-2'}))
    password1 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'mb-2'}))
    password2 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'mb-2'}))
    class Meta:
        model = models.CustomUser
        fields = ('email','password1','password2')







class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder':'Enter First Name','class':'mb-3 mt-3'}))
    last_name = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Last Name','class':'mb-3'}))
    address = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Address','class':'mb-3'}))
    zip_code = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder':'Zip Code','class':'mb-3'}))
    Country = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder':'Country','class':'mb-3'}))
    dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={'type':'date','class':'mb-3'}))
    class Meta:
        model = models.Profile
        fields = ('profile_pic','first_name','last_name','address','zip_code','Country','dob','facebook_id')


class ProfilePicChange(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('profile_pic',)

