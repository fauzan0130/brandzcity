# Generated by Django 3.2.7 on 2022-12-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20221012_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_available',
            field=models.CharField(default=(1, 2, 3, 4, 5, 6, 7, 8, 9), max_length=150),
            preserve_default=False,
        ),
    ]
