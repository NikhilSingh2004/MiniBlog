# Generated by Django 5.0.1 on 2024-01-11 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 17, 14, 40, 461533)),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
