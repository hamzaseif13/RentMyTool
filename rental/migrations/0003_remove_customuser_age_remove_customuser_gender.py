# Generated by Django 4.0.6 on 2022-08-01 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_customuser_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
    ]
