"""from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile, AccountRequest

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email in User.objects.values_list('email', flat=True):
            raise forms.ValidationError("This email already belongs to another account")
        return email

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        if '@' in username:
            raise forms.ValidationError("This @ special charater is not allowed")
        else:
            return username

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','link1','link2','location', 'pic', 'banner', 'age', 'private',)


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
        exclude = ('password',)

class RequestForm(forms.ModelForm):
    class Meta:
        model = AccountRequest
        fields = ('sent',)
"""
