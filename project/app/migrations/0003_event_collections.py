# Generated by Django 4.2.2 on 2023-07-13 18:58

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_streaming_collections'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=app.models.getFilename)),
                ('Event_name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
