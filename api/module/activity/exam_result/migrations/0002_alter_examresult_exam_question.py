# Generated by Django 4.2.3 on 2023-07-27 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_question', '0002_rename_question_type_examquestion_type'),
        ('exam_result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresult',
            name='exam_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_results', to='exam_question.examquestion'),
        ),
    ]
