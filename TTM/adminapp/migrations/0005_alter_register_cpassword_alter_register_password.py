# Generated by Django 5.0 on 2024-02-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_register_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='cpassword',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
