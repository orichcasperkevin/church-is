# Generated by Django 2.2 on 2019-04-05 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0005_auto_20190405_1053'),
        ('projects', '0001_initial'),
        ('finance', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PledgePayment',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('projects.pledge',),
        ),
        migrations.AddField(
            model_name='titheparent',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tithe_recorded_by', to='member.Member'),
        ),
        migrations.AddField(
            model_name='tithe',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.AddField(
            model_name='tithe',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.TitheParent'),
        ),
        migrations.AddField(
            model_name='offering',
            name='church_group',
            field=models.ManyToManyField(to='groups.ChurchGroup'),
        ),
        migrations.AddField(
            model_name='offering',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offering_recorded_by', to='member.Member'),
        ),
        migrations.AddField(
            model_name='income',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='income_recorded_by', to='member.Member'),
        ),
        migrations.AddField(
            model_name='income',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.IncomeType'),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenditure_recorded_by', to='member.Member'),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.ExpenditureType'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Member'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contribution_recorded_by', to='member.Member'),
        ),
    ]
