# Generated by Django 4.2.3 on 2023-07-21 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsType', '0003_newstype_parent_newstype_parent_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_type', to='newsType.newstype'),
        ),
    ]