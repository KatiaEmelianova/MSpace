# Generated by Django 4.0.4 on 2022-06-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_composer_rating_alter_emotion_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='composer',
            name='email',
            field=models.CharField(max_length=320, null=True),
        ),
        migrations.AddField(
            model_name='composer',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='composer',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=320, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
