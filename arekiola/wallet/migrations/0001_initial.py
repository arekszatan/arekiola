# Generated by Django 4.1.2 on 2023-07-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WalletListDb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('famale', models.BooleanField(blank=True, default=False)),
                ('person', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]