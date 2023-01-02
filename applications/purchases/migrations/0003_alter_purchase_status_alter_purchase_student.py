# Generated by Django 4.1.4 on 2023-01-02 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchases', '0002_purchase_confirmation_code_purchase_is_confirm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('not_confirmed', 'Not confirmed'), ('waiting', 'Waiting'), ('in_process', 'In process'), ('completed', 'Completed')], default='not_confirmed', max_length=50),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL),
        ),
    ]
