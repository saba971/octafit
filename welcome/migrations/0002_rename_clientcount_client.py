# Generated by Django 4.0.3 on 2022-03-20 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clientcount',
            new_name='client',
        ),
    ]
