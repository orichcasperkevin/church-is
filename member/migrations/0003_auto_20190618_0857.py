# Generated by Django 2.2 on 2019-06-18 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20190504_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolemembership',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.DeleteModel(
            name='MemberRole',
        ),
    ]
