from django import forms
 
class UserForm(forms.Form):
    login = forms.CharField(label='Логин', label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль', label_suffix='')
    