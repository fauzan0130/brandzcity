# Generated by Django 3.2.3 on 2021-08-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('text', models.CharField(max_length=2000)),
            ],
        ),
    ]
