# Generated by Django 2.2 on 2019-11-23 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church_social', '0002_discussionreaction_recommendation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussionreaction',
            old_name='recommendation',
            new_name='recomendation',
        ),
    ]