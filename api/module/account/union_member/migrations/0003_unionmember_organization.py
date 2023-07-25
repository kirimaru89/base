# Generated by Django 4.2.3 on 2023-07-20 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('union_member', '0002_unionmember_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unionmember',
            name='organization',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='union_members', to='organization.organization'),
        ),
    ]