# Generated by Django 2.1.4 on 2019-09-22 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190920_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='des',
            field=models.CharField(max_length=100, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='des',
            field=models.CharField(max_length=100, null=True, verbose_name='备注'),
        ),
    ]
