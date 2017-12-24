from django.contrib import admin
from .models import Article,Tag,Category
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('views',)
# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)
