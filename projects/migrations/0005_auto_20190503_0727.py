# Generated by Django 2.2 on 2019-05-03 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190503_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledgepayment',
            name='pledge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Pledge'),
        ),
    ]