# Generated by Django 3.1.7 on 2021-05-24 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zotify', '0010_auto_20210524_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role_name',
            new_name='name',
        ),
    ]
