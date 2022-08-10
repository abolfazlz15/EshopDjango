from django import forms
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': '8'}))


    def clean(self):
        name = self.cleaned_data.get('name')
        subject = self.cleaned_data.get('subject')

        if name == subject:
            raise ValidationError('name and subject are same', code='name_message_same')
