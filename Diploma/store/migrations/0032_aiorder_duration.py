# Generated by Django 4.0.4 on 2022-06-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_aiorder_license_file_aiorder_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiorder',
            name='duration',
            field=models.IntegerField(default=15),
        ),
    ]
