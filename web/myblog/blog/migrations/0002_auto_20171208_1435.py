# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-08 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '文章类型', 'verbose_name_plural': '文章类型'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '文章标签', 'verbose_name_plural': '文章标签'},
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, max_length=200, verbose_name='文章摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文章作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='文章类型'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='modified_time',
            field=models.DateTimeField(verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='文章标签'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=70, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='文章类型'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='文章标签'),
        ),
    ]