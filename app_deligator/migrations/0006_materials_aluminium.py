# Generated by Django 4.0.7 on 2022-12-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_deligator', '0005_materials_red_mud'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='aluminium',
            field=models.IntegerField(null=True),
        ),
    ]