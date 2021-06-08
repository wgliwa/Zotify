# Generated by Django 3.1.7 on 2021-05-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zotify', '0003_auto_20210522_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='mp3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='number_of_plays',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
