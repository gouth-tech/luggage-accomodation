# Generated by Django 2.2.1 on 2019-11-07 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0007_auto_20191107_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='luggage',
            name='total_amount',
        ),
    ]
