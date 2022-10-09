from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from .models import Post


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
        "class": "form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
          'email':'Email'
        }
        widgets = {
          'username':forms.TextInput(attrs={'autofocus' : False, 'class':'form-control'}),
          'email':forms.TextInput(attrs={'class':'form-control'})
        }

    '''
      Overwriting username and email field.
      username --> autofocus - False
      email --> required - True
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = False
            self.fields['email'].required = True

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={"autofocus": False, "class": "form-control"}))
  password = forms.CharField(
      label=_("Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
  )

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['tittle', 'description']
    widgets = {
      'tittle': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}
        )
    }