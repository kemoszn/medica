# Generated by Django 2.2.10 on 2020-05-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200509_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='acute_care_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='gloves_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='icu_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='masks_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='respirators_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='ventilators_total',
            field=models.IntegerField(null=True),
        ),
    ]
