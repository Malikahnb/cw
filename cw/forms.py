from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.EmailField()
    salary = forms.IntegerField()