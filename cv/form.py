from django import forms
from .models import Contact
from resume.context_processors import project_context

class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'name':'name',
			'class':'form-control',
			'id':'name',
			'placeholder':'Votre Nom',
			}))
	mailadress = forms.EmailField(max_length=254, required=True, 
		widget=forms.EmailInput(attrs={
			'class':'form-control',
			'name':'email',
			'id':'email',
			'placeholder':'Votre Email'
			}))
	subject = forms.CharField(max_length=100,required=True,
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'name':'subject',
			'id':'subject',
			'placeholder':'Objet'
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'class':'form-control',
			'name':'message',
			'rows':5,
			'placeholder':'Message'
			}))
	
	
	
	class Meta:
		model = Contact
		exclude = ["profile"]
		fields = ('name', 'subject', 'mailadress', 'message')