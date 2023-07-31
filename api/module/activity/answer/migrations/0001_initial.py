# Generated by Django 4.2.3 on 2023-07-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('correct', models.BooleanField()),
            ],
            options={
                'db_table': 'answers',
                'ordering': ['-id'],
            },
        ),
    ]