from django import forms

class ItemForm(forms.Form):
    value = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Value', }), required = True)