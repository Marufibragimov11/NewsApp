# Generated by Django 4.0 on 2024-06-18 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0005_news_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_count',
        ),
    ]