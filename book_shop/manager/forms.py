from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput

from manager.models import Comment, Book, CustomersFeedback


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
    username = UsernameField(widget=TextInput(attrs={'autofocus': True}))
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class CustomersFeedbackForm(ModelForm):
    class Meta:
        model = CustomersFeedback
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'})
        }
        help_texts = {'text': "please enter your feedback here"}
