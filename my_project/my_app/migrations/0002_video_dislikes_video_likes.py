# Generated by Django 5.0.3 on 2024-03-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="dislikes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="video",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]
