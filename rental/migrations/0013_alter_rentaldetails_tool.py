# Generated by Django 4.0.6 on 2022-08-06 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0012_rentaldetails_canceled_rentaldetails_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaldetails',
            name='tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.tool'),
        ),
    ]
