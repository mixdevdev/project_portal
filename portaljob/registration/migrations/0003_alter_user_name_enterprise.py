# Generated by Django 3.2.9 on 2021-12-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_user_name_enterprise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name_enterprise',
            field=models.CharField(default=' ', max_length=200, verbose_name='Nom entreprise'),
        ),
    ]
