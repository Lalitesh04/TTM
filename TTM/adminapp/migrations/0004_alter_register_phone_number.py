# Generated by Django 5.0 on 2024-02-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_register_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
