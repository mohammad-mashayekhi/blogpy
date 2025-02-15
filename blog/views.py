from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers as Serializers

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

          
class SingleArtickeApiView(APIView):
    
    def get(self, request, format=None):
        try:
            article_title = request.GET.get('title')
            atricle = Article.objects.filter(title__contains=article_title)
            serialized_data = Serializers.SingleArticleSerializer(atricle, many=True)
            data = serialized_data.data
            
            return Response({'data': data}, status=status.HTTP_200_OK)
        except Exception as e:
           return Response(
                {'status': "Internal server error", 'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
           
           
class SearchArticleApiView(APIView):
    
   def get(self, request, fornamt=None):
        try:
            from django.db.models import Q
            query = request.GET.get('query')
            artickes = Article.objects.filter(Q(title__contains=query) | Q(context__icontains=query))
            serialized_data = Serializers.SearchArticleSeializer(artickes, many=True)
            data= serialized_data.data
            
            return Response({'data': data}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                    {'status': "Internal server error", 'error': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )                   

class CreateArticleApiView(APIView):
    
    def post(self, request, formant=None):
        try:
            serializers = Serializers.CreateArticleSerializer(data=request.data)
            if serializers.is_valid():
                title = serializers.data.get('title')
                cover = serializers.data.get('cover')
                context = serializers.data.get('context')
                category_id = serializers.data.get('category')
                author_id = serializers.data.get('author')
                promot = serializers.validated_data.get('promot', False) 
            else:
                return Response({'status': 'Bad request', 'error': serializers.errors},status=status.HTTP_200_OK)
        
        
            user = User.objects.get(id=author_id)
            author = UserProfile.objects.get(user=user)
            category = Category.objects.get(id=category_id)
            
            article = Article()
            article.title = title
            article.cover = cover
            article.context = context
            article.category = category
            article.author = author
            article.promot = promot
            article.save()
            
            
            return Response({'status':'ok',"id":article.id},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'status': "Internal server error", 'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )                   