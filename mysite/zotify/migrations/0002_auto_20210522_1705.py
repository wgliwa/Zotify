# Generated by Django 3.1.7 on 2021-05-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zotify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='no_songs',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]