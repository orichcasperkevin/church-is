# Generated by Django 2.2 on 2020-01-28 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_churchgroup_anvil_space_only'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmeeting',
            name='host',
        ),
        migrations.AddField(
            model_name='groupmeeting',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=160),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupmeeting',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='groupmeeting',
            name='location',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='GroupPhoto',
        ),
    ]
