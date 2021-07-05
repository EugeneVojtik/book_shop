from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, EmailField

from manager.models import Comment, Book, CustomersFeedback

class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass

    username = UsernameField(widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(
        label=("Password"),
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )
    password2 = CharField(
        label=("Password confirmation"),
        widget=PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
    )

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 10})
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'})
        }
        help_texts = {
            'text': "please enter your comment here"
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control'}),
    )



class CustomersFeedbackForm(ModelForm):
    class Meta:
        model = CustomersFeedback
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'})
        }
        help_texts = {'text': "please enter your feedback here"}
