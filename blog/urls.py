from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index' ),
    path('contact/', views.ContactPage.as_view(), name='contact' ),
    
    path('article/', views.SingleArtickeApiView.as_view(), name='Singlearticle' ),
    path('article/all/', views.AllArticleApiView.as_view(), name='article_all' ),
    
    path('article/search/', views.SearchArticleApiView.as_view(), name='search_article' ),
]