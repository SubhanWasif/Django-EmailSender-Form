from django import forms
from django.conf import settings
from django.core.mail import send_mail



class Contactform(forms.Form):
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email       = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    subject     = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}))  
    message     = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))



#class AuthorForm(ModelForm):
    # class Meta:
    #     model = Author
    #     fields = ('name', 'title', 'birth_date')
    #     widgets = {
    #         'name': Textarea(attrs={'cols': 80, 'rows': 20}),
    #     }
