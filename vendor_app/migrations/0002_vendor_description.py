# Generated by Django 5.0.1 on 2024-01-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
