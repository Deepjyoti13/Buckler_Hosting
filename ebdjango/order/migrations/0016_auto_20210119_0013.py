# Generated by Django 3.1.4 on 2021-01-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_order_daysadded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='daysadded',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
