# Generated by Django 4.2.3 on 2023-07-21 08:48

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsType', '0002_alter_newstype_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='newsType.newstype'),
        ),
        migrations.AddField(
            model_name='newstype',
            name='parent_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
    ]