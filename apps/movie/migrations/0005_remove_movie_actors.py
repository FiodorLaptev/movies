# Generated by Django 2.2.5 on 2019-09-13 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_artist_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
    ]