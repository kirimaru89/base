# Generated by Django 4.2.3 on 2023-07-19 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsType', '0002_alter_newstype_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('cover_image', models.TextField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('status', models.SmallIntegerField()),
                ('news_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='newsType.newstype')),
            ],
            options={
                'db_table': 'news',
                'ordering': ['-id'],
            },
        ),
    ]