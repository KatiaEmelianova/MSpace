# Generated by Django 4.0.4 on 2022-06-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_composerorder_file_alter_product_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/composers/'),
        ),
        migrations.AlterField(
            model_name='composerorder',
            name='file',
            field=models.FileField(max_length=200, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/customers/'),
        ),
        migrations.AlterField(
            model_name='emotion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/emotions/'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/genres/'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/instruments/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(max_length=200, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products/'),
        ),
    ]