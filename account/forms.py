from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))


    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError('username or password are wrong', code='invalid_login_info')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'input100'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل وجود دارد')

        return email    
