# Generated by Django 4.1.2 on 2023-07-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletlistdb',
            name='price',
            field=models.FloatField(),
        ),
    ]
