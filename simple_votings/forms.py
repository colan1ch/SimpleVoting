from django import forms

class Edit(forms.Form):
    name = forms.CharField(label = "Имя", required = "True")
    oldpass = forms.CharField(label="Старый пароль", required="True")
    newpass = forms.CharField(label="Новый пароль", required="True")
    email = forms.CharField(label="Почта", required="True")
    surname = forms.CharField(label="Фамилия", required="True")
    login = forms.CharField(label="Логин", required="True")

