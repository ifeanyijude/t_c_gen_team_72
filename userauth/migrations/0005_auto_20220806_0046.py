# Generated by Django 3.2.12 on 2022-08-05 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_questions_questiontwo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionTwo',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='answer',
        ),
    ]
