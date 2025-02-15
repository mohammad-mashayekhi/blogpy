from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        promoted_data = []
        promoted_articles = Article.objects.filter(promot=True).order_by('-created_at')[:3]
        for promoted_article in promoted_articles:
             promoted_data.append({
            'category': article.category.title,
            'title': article.title,
            'author': article.author.user.first_name + ' ' + article.author.user.last_name,
            'avatar': article.author.avatar.url if promoted_article.author.avatar else None,
            'cover': article.cover.url if promoted_article.cover else None,
            'created_at' : article.created_at.date(),
        })

        context = {
            'article_data': article_data,
            'promoted_article':promoted_article,
        }
        return render(request, 'index.html', context)

class ContactPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'page-contact.html')
    

class AllArticleApiView(APIView):
    
    def get(self, request, format=None):
        try:
            
            all_articles = Article.objects.all().order_by('-created_at')[:3]
            data = []
            
            for article in all_articles:
                data.append({
                    "title": article.title,
                    "cover": article.cover.url if article.cover else None,
                    "content": article.context,
                    "category": article.category.title,
                    "author": article.author.user.first_name + ' ' + article.author.user.last_name,
                    "created_at": article.created_at,
                    "promot": article.promot
                })
                
            return Response({'data': data}, status=status.HTTP_200_OK)
        
        except:    
            return Response({'status':"Internal server error"}, 
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)

          