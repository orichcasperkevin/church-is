# Generated by Django 2.2 on 2019-11-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_delete_client'),
        ('church_social', '0002_auto_20191120_1517'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DiscussionReactions',
            new_name='DiscussionReaction',
        ),
        migrations.AlterField(
            model_name='discussion',
            name='topic',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
