# Generated by Django 4.2.2 on 2023-07-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_sports_collections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Concept',
            field=models.CharField(max_length=1000),
        ),
    ]
