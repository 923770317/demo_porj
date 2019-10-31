from django import forms


class AddFrom(forms.Form):
    name = forms.CharField(required=True, max_length=10,label='name_form')
    age = forms.IntegerField(required=True,label='age_form')
