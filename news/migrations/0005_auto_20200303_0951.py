# Generated by Django 2.2 on 2020-03-03 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200229_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='church_group',
        ),
        migrations.RemoveField(
            model_name='news',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='news',
            name='website',
        ),
    ]