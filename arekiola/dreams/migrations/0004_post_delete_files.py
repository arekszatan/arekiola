# Generated by Django 4.1.2 on 2023-07-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreams', '0003_alter_files_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='Files',
        ),
    ]