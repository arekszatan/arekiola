# Generated by Django 4.1.2 on 2023-07-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingdb',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
