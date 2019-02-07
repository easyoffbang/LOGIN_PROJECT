from django.forms import ModelForm
from django import forms

from .models import Account


class AccountForm(ModelForm):
    pw1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'blank', 'placeholder': '비밀번호'}))
    pw2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'blank', 'placeholder': '비밀번호 재입력'}))

    def clean(self):
        pw1 = self.cleaned_data['pw1']
        pw2 = self.cleaned_data['pw2']

        if pw1 == pw2:
            self.cleaned_data['pw'] = pw1
        else:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    class Meta:
        model = Account
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'blank', 'placeholder': '이름'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'blank', 'placeholder': '아이디'}))
    pw = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'blank', 'placeholder': '비밀번호'}))

class NewpwForm(forms.Form):
    current_pw = forms.CharField(label='현재 비밀번호', widget=forms.PasswordInput(attrs={'class':'blank'}))
    new_pw1 = forms.CharField(label='새 비밀번호', widget=forms.PasswordInput(attrs={'class':'blank'}))
    new_pw2 = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput(attrs={'class':'blank'}))

