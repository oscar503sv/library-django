from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'input mt-3 mb-3','placeholder':'Escriba su nombre de usuario'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'input mt-3','placeholder': 'Escriba su contraseña'}))

