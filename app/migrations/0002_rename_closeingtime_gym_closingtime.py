# Generated by Django 4.2 on 2023-05-02 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='closeingtime',
            new_name='closingtime',
        ),
    ]
