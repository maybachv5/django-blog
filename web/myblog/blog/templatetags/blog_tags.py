from django import template
from ..models import Article,Category,Tag
register = template.Library()
@register.simple_tag
def get_recent_articles(num=5):
	return Article.objects.all()[:num]

@register.simple_tag
def archives():
	return Article.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_category():
	return Category.objects.all()

@register.simple_tag
def get_tags():
	return Tag.objects.all()


