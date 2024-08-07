# Generated by Django 5.0.6 on 2024-06-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_itemstatus_accepted_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemstatus',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Ready for Pickup', 'Ready for Pickup'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
