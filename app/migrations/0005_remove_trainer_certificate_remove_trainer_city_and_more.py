# Generated by Django 4.2 on 2023-05-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_gym_charge_gym_phone_trainer_slot_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='state',
        ),
        migrations.AlterField(
            model_name='gym',
            name='charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gym',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
