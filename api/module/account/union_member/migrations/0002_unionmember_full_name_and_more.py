# Generated by Django 4.2.3 on 2023-07-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('union_member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unionmember',
            name='full_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unionmember',
            name='identity_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='unionmember',
            name='issued_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='unionmember',
            name='participated_place_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
