from django import forms
from digiTech.choice import *
from digiTech.models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, label='用户名', widget=forms.TextInput(attrs={'class': 'input-text'}))
    email = forms.EmailField(max_length=50, label='邮箱账号', widget=forms.TextInput(attrs={'class': 'input-text'}))
    password1 = forms.CharField(min_length=6, max_length=20, label='设置密码', widget=forms.PasswordInput(attrs={
        'placeholder': '6-20个字符，建议使用字母、数字和符号两种及以上的组合', 'class': 'input-text'}))
    password2 = forms.CharField(min_length=6, max_length=20, label='确认密码', widget=forms.PasswordInput(attrs={
        'placeholder': '请再次输入密码', 'class': 'input-text'}))
    location = forms.CharField(max_length=2, label='所在地', widget=forms.Select(choices=(('', '请选择您的所在地...'),)
                               + PLACE_CHOICES, attrs={'class': 'country_to_state country_select'}), required=False)
    school = forms.CharField(max_length=50, label='学校', widget=forms.TextInput(attrs={'class': 'input-text'}),
                             required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError('用户名已被注册，请更换用户名')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__exact=email):
            raise forms.ValidationError('邮箱已被注册，请更换邮箱地址')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('两次密码输入不一致')
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': '用户名'}))
    password = forms.CharField(max_length=20, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': '密码',
                                                                                              'class': 'form-control'}))


class PasswordForgetForm(forms.Form):
    nameoremail = forms.CharField(max_length=50, widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '请输入用户名或注册邮箱'}))


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput(
                                attrs={'placeholder': '请输入6-20个字符的密码', 'class': 'form-control'}))
    password2 = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput(
                                attrs={'placeholder': '请再次输入密码', 'class': 'form-control'}))

    def clean_password2(self):
        cleaned_data = super(PasswordResetForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('两次密码输入不一致')
        return password2
