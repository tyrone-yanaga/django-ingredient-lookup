from django import forms

MAX_INPUT_LENGTH = 200

class UserInputForm(forms.Form):
    query = forms.CharField(label='Ingredient to search', max_length=MAX_INPUT_LENGTH)