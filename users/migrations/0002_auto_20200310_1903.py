# Generated by Django 3.0.3 on 2020-03-11 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='posts_count',
            field=models.IntegerField(default=0),
        ),
    ]
