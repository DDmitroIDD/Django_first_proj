from django import forms
from django.contrib.auth.models import User

GENDERS = ((1, 'male'), (2, 'female'))
ENGLISH_LEVEL = ((1, 'A'), (2, 'A1'), (3, 'A2'), (4, 'B1'), (5, 'B2'), (6, 'C1'))


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    gender = forms.ChoiceField(choices=GENDERS)
    age = forms.IntegerField()
    english_level = forms.ChoiceField(choices=ENGLISH_LEVEL)

    def clean(self):
        data = self.cleaned_data
        if data.get('gender') == '2':
            if data.get('age') < 20 or data.get('english_level') < '5':
                raise forms.ValidationError('ne norm')
        elif data.get('gender') == '1':
            if data.get('age') < 22 or data.get('english_level') < '4':
                raise forms.ValidationError('ne norm')

        return data


class MyLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class SearchMassageForm(forms.Form):
    search = forms.CharField(required=False)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation')

    def clean(self):
        data = self.cleaned_data
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Passwords do not match!')
        return data

# class PasswordChangeForm(forms.ModelForm):
#     old_password = forms.CharField(required=True, widget=forms.PasswordInput)
#     new_password = forms.CharField(required=True, widget=forms.PasswordInput)
#     new_password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput)


