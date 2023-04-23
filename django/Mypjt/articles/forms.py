from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=[('선택', 'None'), ('Nature','Nature'), ('Character', 'Character')]
    )
    class Meta:
        model = Article
        exclude = ('user', )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article', )