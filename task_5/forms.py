from django import forms
from django.core.exceptions import ValidationError


class QuestionForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=((1, 'male'), (2, 'female')))
    level_eng = forms.ChoiceField(choices=((1, 'a1'), (2, 'a2'), (3, 'b1'), (4, 'b2'), (5, 'c1'), (6, 'c2')))

    def clean(self):
        cd = super().clean()
        if (
                (int(cd['gender']) == 1) and
                (int(cd['age']) >= 20) and
                (int(cd['level_eng']) >= 4)):
            pass
        elif (
                (int(cd['gender']) == 2) and
                (int(cd['age']) > 22) and
                (int(cd['level_eng']) >= 3)):
            pass
        else:
            raise ValidationError('error', code='invalid')


class UserLoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cd = super(UserRegisterForm, self).clean()
        if cd['password'] != cd['password1']:
            forms.ValidationError('incorrect password')


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cd = super(ChangePasswordForm, self).clean()
        if cd['password'] != cd['password1']:
            raise ValidationError('incorrect password')



