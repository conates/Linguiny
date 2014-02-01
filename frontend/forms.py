from django import forms

class SearchForm(forms.Form):
	translate_from = forms.CharField(label='Translate From', required=True)
	translate_to = forms.CharField(label='Translate To')
	
	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['translate_from'].widget.attrs['class'] = 'form-control'
		self.fields['translate_to'].widget.attrs['class'] = 'form-control'
		