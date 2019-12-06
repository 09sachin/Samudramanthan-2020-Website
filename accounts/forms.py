from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())
    confirm_email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'email',
            'College',
            'Contact',
            'state',
            'city',
            'birth_date',
            'events',
        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email != confirm_email:
            raise forms.ValidationError(
                "Emails must match!"
            )


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, )
    contact = forms.CharField(max_length=30, required=False, )
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'contact', 'email', 'password1', 'password2', )

