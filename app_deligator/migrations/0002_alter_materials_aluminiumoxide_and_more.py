# Generated by Django 4.0.7 on 2022-12-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_deligator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='aluminiumoxide',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='materials',
            name='carbon',
            field=models.FloatField(),
        ),
    ]