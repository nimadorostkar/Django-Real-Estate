from django import forms

class QuickContactForm(forms.Form):
    email= forms.CharField(label='',widget= forms.EmailInput(attrs={'placeholder':'Enter your E-mail address'}))
    textarea = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Write here'}))