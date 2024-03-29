# Generated by Django 3.1.7 on 2021-05-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zotify', '0011_auto_20210524_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='artist',
            name='formed_in',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='wiki',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
