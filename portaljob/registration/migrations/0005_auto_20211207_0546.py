# Generated by Django 3.2.9 on 2021-12-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_user_nif_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_recruiter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_trainer',
            field=models.BooleanField(default=False),
        ),
    ]
