# Generated by Django 2.2 on 2020-01-29 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_merge_20200128_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=160, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='offering',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.OfferingType'),
        ),
    ]