# Generated by Django 4.2.3 on 2023-07-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
