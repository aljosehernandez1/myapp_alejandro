# Generated by Django 4.1.5 on 2023-01-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0002_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='ciudad',
            field=models.CharField(max_length=30),
        ),
    ]
