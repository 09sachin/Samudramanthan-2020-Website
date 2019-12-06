from django import forms
from .models import FeedBack, RegisterForm


class FeedbackCreate(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    # email = forms.EmailField(widget=forms.EmailInput(), required=True, max_length=100)
    # subject = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    # message = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    class Meta:
        model = FeedBack
        fields = ['name', 'email', 'subject', 'message']


class Register(forms.ModelForm):
    # eventlist = [
    #     ('a', 'a'),
    #     ('a', 'a'),
    #     ('a', 'a'),
    #     ('a', 'a'),
    #     ('a', 'a'),
    #     ('a', 'a')
    # ]
    # name = forms.CharField(widget=forms.TextInput(), required=True, max_length=250)
    # email = forms.EmailField(widget=forms.EmailInput(), required=True, max_length=300)
    # contact = forms.CharField(widget=forms.TextInput(), required=True, max_length=400)
    # college = forms.CharField(widget=forms.TextInput(), required=True, max_length=1000)
    # department = forms.CharField(widget=forms.TextInput(), required=True, max_length=1000)
    # year = forms.CharField(widget=forms.TextInput(), required=True, max_length=1000)
    # event = forms.CharField(widget=forms.Select(choices=eventlist))
    class Meta:
        model = RegisterForm
        fields = ['name', 'email', 'contact', 'college', 'department', 'year']
