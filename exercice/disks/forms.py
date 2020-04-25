from django import forms


class RechercheForm(forms.Form):
    key_word = forms.CharField(max_length=220)