# Generated by Django 3.1.4 on 2021-01-02 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='salary',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(max_length=4),
        ),
    ]
