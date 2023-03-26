from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=[('선택', 'None'), ('Nature','Nature'), ('Character', 'Character')]
    )
    class Meta:
        model = Article
        fields = '__all__'