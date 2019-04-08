# Generated by Django 2.2 on 2019-04-08 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import member.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(default='member', max_length=20)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MemberRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
                ('role', models.ForeignKey(default=member.models.Role.get_role, on_delete=django.db.models.deletion.CASCADE, to='member.Role')),
            ],
        ),
        migrations.CreateModel(
            name='MemberResidence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('town', models.CharField(blank=True, max_length=200, verbose_name='town')),
                ('road', models.CharField(blank=True, max_length=200, verbose_name='Road')),
                ('street', models.CharField(blank=True, max_length=200, verbose_name='street')),
                ('village_estate', models.CharField(blank=True, max_length=200, verbose_name='village/estate')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='description')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberMaritalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('M', 'Married'), ('S', 'Single')], max_length=2, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('postal', models.CharField(blank=True, max_length=200, verbose_name='Postal Address')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Telephone(Mobile)')),
                ('contact', models.CharField(blank=True, max_length=200, verbose_name='Contact No.')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberAge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('d_o_b', models.DateField()),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Family')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
        migrations.AddField(
            model_name='family',
            name='head',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='familyHeads', to='member.Member'),
        ),
    ]
