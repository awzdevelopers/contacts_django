from django import forms
from app1.models import ContactsTable,PhonesTable




class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactsTable
        fields=['name','family','job']

class PhoneForm(forms.ModelForm):
    class Meta:
        model=PhonesTable
        fields="__all__" 
