# -*- coding: utf-8 -*-

from django import forms
from wistock.models import user

class loginForm(forms.Form):
  email = forms.EmailField(label = 'Email')
  password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
  def clean(self):
    cleaned_data = super(loginForm,self).clean()
    email = cleaned_data.get("email")
    password = cleaned_data.get("password")
    if email and password:
      result = user.objects.filter(password=password, email=email)
      if len(result) != 1:
        raise forms.ValidationError("Wrong email or password.")
    return cleaned_data
