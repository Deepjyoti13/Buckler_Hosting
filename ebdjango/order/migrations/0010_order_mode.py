# Generated by Django 3.1.4 on 2021-01-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20210115_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mode',
            field=models.CharField(choices=[('COD', 'COD'), ('PREPAY', 'PREPAY')], max_length=10, null=True),
        ),
    ]
