# Generated by Django 4.2.2 on 2023-11-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_attendance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(default=2000),
        ),
    ]
