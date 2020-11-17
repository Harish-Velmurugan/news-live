from django.contrib import admin
from .models import Article,Comment
from . import models
# Register your models here.
class CommentInline(admin.TabularInline): 
    model = models.Comment
class ArticleAdmin(admin.ModelAdmin): 
    inlines = [
        CommentInline,
    ]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,)