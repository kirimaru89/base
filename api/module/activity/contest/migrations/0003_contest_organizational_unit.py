# Generated by Django 4.2.3 on 2023-07-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_alter_contest_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='organizational_unit',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
