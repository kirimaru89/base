# Generated by Django 4.2.3 on 2023-07-25 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('occupation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('position', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ethnic', models.CharField(default='', max_length=255, null=True)),
                ('religion', models.CharField(default='', max_length=255, null=True)),
                ('education_level', models.CharField(default='', max_length=255, null=True)),
                ('qualification', models.CharField(default='', max_length=255, null=True)),
                ('it_level', models.CharField(default='', max_length=255, null=True)),
                ('foreign_language_level', models.CharField(default='', max_length=255, null=True)),
                ('political_theory_level', models.CharField(default='', max_length=255, null=True)),
                ('full_name', models.CharField(default='', max_length=255)),
                ('joined_date', models.DateField(null=True)),
                ('gender', models.BooleanField(null=True)),
                ('id_number', models.CharField(default='', max_length=255, null=True)),
                ('id_issued_date', models.DateField(null=True)),
                ('id_issued_place', models.CharField(default='', max_length=255, null=True)),
                ('occupation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occupation.occupation')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='position.position')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'members',
                'ordering': ['-user'],
            },
        ),
    ]
