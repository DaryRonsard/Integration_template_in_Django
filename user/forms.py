from django import forms


class UserForm(forms.Form):
    pseudo = forms.CharField(max_length=10, required=True)
    date = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
