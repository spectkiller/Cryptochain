from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

User = get_user_model()


                   
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Email', 'title': 'Enter a valid email address'}))
    username = forms.CharField(max_length=30, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', widget=forms.TextInput(attrs={'placeholder': 'Username', 'title': 'Enter a username with 150 characters or fewer. Letters, digits and @/./+/-/_ only.'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'title': 'Your password must contain at least 8 characters.'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'title': 'Enter the same password as before, for verification.'}))
    captcha = ReCaptchaField(
        label='',  # Add this line
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.5,
                'widget_options': {'size': 'invisible'},
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    captcha = ReCaptchaField(
        label='',  # Add this line
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.5,
                'widget_options': {'size': 'invisible'},
            }
        )
    )
