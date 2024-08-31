from django import forms
from .models import Post

class PostForm(forms.Form):
        title = forms.CharField()
        url = forms.URLField(required=False)
        description = forms.CharField(widget=forms.Textarea, required=False)

class RegistrationForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
        password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

