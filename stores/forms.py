from random import choice, choices
from django import forms
from . import models


class SearchForm(forms.Form):
    menu = forms.ModelChoiceField(queryset=models.Store.objects.all())
