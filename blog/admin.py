from django.contrib import admin

from .models import Article, Category, UserProfile

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(UserProfile)