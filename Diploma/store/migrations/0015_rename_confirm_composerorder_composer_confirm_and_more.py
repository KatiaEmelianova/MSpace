# Generated by Django 4.0.4 on 2022-06-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_composerorder_accept'),
    ]

    operations = [
        migrations.RenameField(
            model_name='composerorder',
            old_name='confirm',
            new_name='composer_confirm',
        ),
        migrations.AddField(
            model_name='composerorder',
            name='customer_confirm',
            field=models.BooleanField(max_length=200, null=True),
        ),
    ]