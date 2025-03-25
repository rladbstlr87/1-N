from django.forms import ModelForm
from django import forms
from .models import Article, Comment

# 유효성 검사때문에 이거 하느거다
class ArticleForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    class Meta():
        model = Article
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # fields = '__all__'

        # # 추가할 필드 목록
        # fields = ('content', ) # 쉼표까지 적어줘야함(선택했으니 보여주세요)

        # 제외할 필드 목록
        exclude = ('article', )
        widgets = {
            'content': forms.Textarea(
                attrs = {
                'rows': 4,
                'cols': 50,
                'style': 'width:80%; height:50;'
                }
            )
        }