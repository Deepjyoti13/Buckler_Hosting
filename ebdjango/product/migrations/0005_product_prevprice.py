# Generated by Django 3.0.7 on 2020-12-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201217_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prevprice',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]