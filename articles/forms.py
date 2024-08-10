from django import forms
from .models import Article, ArticleImage


class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ['image']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'\"{title.lower()}\" is already in use.')
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'dressing with ai style':
            self.add_error('title', 'This title is taken.')
            #  raise forms.ValidationError('This title is taken.')
        if "office" in content or "office" in title.lower():
            self.add_error('content', 'Office can not be in content(he is the god)')
            raise forms.ValidationError("Office is not allowed")
        return cleaned_data
