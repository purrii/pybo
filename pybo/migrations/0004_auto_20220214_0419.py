# Generated by Django 3.1.3 on 2022-02-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_fate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_fate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
