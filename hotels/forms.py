from django import forms

class SearchForm(forms.Form):
	search_text = forms.CharField()
	how_much 	= forms.IntegerField()