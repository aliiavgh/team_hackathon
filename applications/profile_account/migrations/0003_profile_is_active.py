# Generated by Django 4.1.4 on 2023-01-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_account', '0002_profile_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]