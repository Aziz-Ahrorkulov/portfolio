from django import forms
from .models import Contactform
# from django.forms import ModelForm, TextInput, EmailInput, Textarea

# class Articleform(ModelForm):
#     class Meta:
#         model = Contactform
#         fields = ['name', 'email', 'message']

#         widgets = {
#             "name": TextInput(attrs={
#                 'class' : 'form-control',
#                 'placeholder' : 'Your Name'
#             }),
#             "email" : EmailInput(attrs={
#                 'class' : 'form-control',
#                 'placeholder' : 'Your Email'
#             }),
#             "message": Textarea(attrs={
#                 'class' : 'form-control',
#                 'placeholder': 'Message'
#             })
#         }