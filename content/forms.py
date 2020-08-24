from django import forms


class SearchForm(forms.Form):
    query = forms.CharField()