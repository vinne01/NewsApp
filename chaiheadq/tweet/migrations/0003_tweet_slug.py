# Generated by Django 5.1 on 2024-09-17 12:46

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_tweet_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
