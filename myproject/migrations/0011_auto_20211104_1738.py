# Generated by Django 3.2.8 on 2021-11-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0010_fileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='FileUL',
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='MaTL',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='Path',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='filename',
            field=models.CharField(max_length=100),
        ),
    ]