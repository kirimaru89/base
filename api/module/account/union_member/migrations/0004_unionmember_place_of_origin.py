# Generated by Django 4.2.3 on 2023-07-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('union_member', '0003_unionmember_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='unionmember',
            name='place_of_origin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
