# Generated by Django 4.0.4 on 2022-06-09 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_rename_confirm_composerorder_composer_confirm_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='composerorder',
            old_name='composer_confirm',
            new_name='confirm',
        ),
    ]
