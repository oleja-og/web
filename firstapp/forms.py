from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label = 'client', max_length=15, initial="fio")
    age = forms.IntegerField()
    comment = forms.CharField(label = 'комментарий', widget = forms.Textarea)
    basket = forms.BooleanField(label= ' положить в корзину',required=False)
    choice = forms.NullBooleanField(label= "играем?")
    email = forms.EmailField(label= 'EMAIL')

class UserForm1(forms.Form):
    name = forms.CharField(label="имя")