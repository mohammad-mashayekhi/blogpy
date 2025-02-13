from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        
        article_data = []
        all_article = Article.objects.all().order_by('-created_at')[:9]

        for article in all_article:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'author': article.author.user.first_name + ' ' + article.author.user.last_name,
                'created_at': article.created_at,
            })

        context = {
            'article_data': article_data,
        }
        return render(request, 'index.html', context)
