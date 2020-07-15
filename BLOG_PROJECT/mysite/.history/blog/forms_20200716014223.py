from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
# for creating user form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


# create the user form
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
