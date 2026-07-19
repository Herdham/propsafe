from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout

User = get_user_model()

class SignUpForm(forms.Form):
  firstname = forms.CharField(max_length=150, widget=forms.TextInput)
  lastname= forms.CharField(max_length=150, widget=forms.TextInput)
  email = forms.EmailField()
  username = forms.CharField(max_length=150, widget=forms.TextInput)
  password1 = forms.CharField(max_length=200, widget=forms.PasswordInput)
  password2 = forms.CharField(max_length=200, widget=forms.PasswordInput)

  def clean_email(self):
    email = self.cleaned_data.get("email")
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("email already existed try another one or log in")
    
    return email
  
  def clean_username(self):
     username = self.cleaned_data.get("username")
     if User.objects.filter(username=username).exists():
        raise forms.ValidationError("username already exist try another one")
     
     return username
  
  def clean(self):
     cleaned_data = super().clean()

     pass1 = cleaned_data.get("password1")
     pass2 = cleaned_data.get("password2")

     if pass1 != pass2:
        raise forms.ValidationError("password not equal check password")
     
     return cleaned_data
  

class LoginForm(forms.Form):
   email = forms.EmailField()
   password = forms.CharField(max_length=200, widget=forms.PasswordInput)



class SettingForm(forms.Form):
   phone_number = forms.IntegerField()
   timezone = forms.CharField(max_length=150)
   bio = forms.CharField(max_length=200,)
   location = forms.CharField(max_length=150)
   experience = forms.CharField(max_length=150)
   market = forms.CharField(max_length=150)
   instrument = forms.CharField(max_length=150)
   risk_per_trade = forms.DecimalField(max_digits=15, decimal_places=2)
   daily_goal = forms.DecimalField(max_digits=15, decimal_places=2)
   account_size = forms.DecimalField(max_digits=15, decimal_places=2)

