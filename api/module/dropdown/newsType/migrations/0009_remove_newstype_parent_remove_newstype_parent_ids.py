# Generated by Django 4.2.3 on 2023-07-21 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsType', '0008_alter_newstype_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstype',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='newstype',
            name='parent_ids',
        ),
    ]