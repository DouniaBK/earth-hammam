# Generated by Django 3.2.22 on 2023-11-21 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('booking', '0002_alter_appointment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='item',
            field=models.ForeignKey(blank=True, limit_choices_to={'category': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.item'),
        ),
    ]
