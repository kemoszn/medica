# Generated by Django 2.2.10 on 2020-05-09 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_update_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
