# Generated by Django 4.2.3 on 2023-07-26 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_alter_organization_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='root_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_children', to='organization.organization'),
        ),
    ]