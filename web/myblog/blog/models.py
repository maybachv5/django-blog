import markdown
from django.utils.html import strip_tags
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100,verbose_name='文章类型')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "文章类型"
		verbose_name_plural = '文章类型'

class Tag(models.Model):
	name = models.CharField(max_length=100,verbose_name='文章标签')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "文章标签"
		verbose_name_plural = '文章标签'

class Article(models.Model): #文章属性
	title = models.CharField(max_length=70,verbose_name='标题')
	body = models.TextField(verbose_name='正文')
	created_time = models.DateTimeField(verbose_name='创建时间')
	modified_time = models.DateTimeField(verbose_name='修改时间')
	abstract = models.CharField(max_length=200,blank=True,verbose_name='文章摘要')
	category = models.ForeignKey(Category,verbose_name='文章类型')
	tags = models.ManyToManyField(Tag,blank=True,verbose_name='文章标签')
	author = models.ForeignKey(User,verbose_name='文章作者')
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		if not self.abstract:

			md = markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
			])
			self.abstract = strip_tags(md.convert(self.body))[:100]
		super(Article, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-created_time']
		verbose_name = "文章"
		verbose_name_plural = '文章'



