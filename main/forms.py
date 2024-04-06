from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea, ModelForm
from django.contrib.auth.models import User

from .models import News


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['user', 'title', 'anons', 'full_text']

        widgets = {

            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),

            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите анонс'
            }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            })


        }


class NewDateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': "Введите имя",
                'class': 'form-control'
            }),

            'last_name': TextInput(attrs={
                'placeholder': "Введите фамилию",
                'class': 'form-control'
            }),
        }