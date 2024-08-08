# Generated by Django 4.2.2 on 2023-07-14 05:26

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_chennai_tamil_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chennai_Other_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=app.models.getFilename)),
                ('movie_name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
