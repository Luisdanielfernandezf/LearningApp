# Generated by Django 5.0.6 on 2024-05-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('T', 'Text'), ('M', 'Multiple Choice')], default='T', max_length=1),
        ),
    ]
