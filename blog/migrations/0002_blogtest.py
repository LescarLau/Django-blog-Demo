# Generated by Django 2.1.4 on 2019-09-20 01:31

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='文章标题')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文本内容')),
                ('created_time', models.DateTimeField(verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(verbose_name='修改时间')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='文章摘要')),
                ('views', models.IntegerField(default=0, verbose_name='查看次数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签')),
            ],
        ),
    ]
