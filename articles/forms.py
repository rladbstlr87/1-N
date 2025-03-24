from django.forms import ModelForm
from .models import Article

# 유효성 검사때문에 이거 하느거다
class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'