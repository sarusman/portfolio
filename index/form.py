from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100)
    mail = forms.EmailField(label='Mail', max_length=100)
    message = forms.CharField(widget=forms.Textarea, label='Message')
