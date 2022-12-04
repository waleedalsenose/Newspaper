from django.contrib import admin
from .models import Article,Comment
# Register your models here.

class CommmentInline(admin.TabularInline):
    model =Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommmentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)