# Generated by Django 4.0.4 on 2022-06-19 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_composer_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_premium', models.BooleanField(max_length=200, null=True)),
                ('file', models.FileField(max_length=200, null=True, upload_to='files/')),
                ('project', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.genre')),
            ],
        ),
    ]
