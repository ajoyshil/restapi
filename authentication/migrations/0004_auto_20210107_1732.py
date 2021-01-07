# Generated by Django 3.1.4 on 2021-01-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210102_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=2)),
                ('salary', models.CharField(max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='device_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_picture_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_picture_url',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
