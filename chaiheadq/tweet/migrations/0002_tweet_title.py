# Generated by Django 5.1 on 2024-09-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='title',
            field=models.CharField(default='Untitled', max_length=100),
        ),
    ]