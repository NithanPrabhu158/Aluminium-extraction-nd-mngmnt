# Generated by Django 4.0.7 on 2022-12-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bauxite', models.IntegerField()),
                ('aluminiumoxide', models.IntegerField()),
                ('carbon', models.IntegerField()),
                ('aluminiumfluoride', models.IntegerField()),
                ('cryolite', models.IntegerField()),
                ('electricalenergy', models.IntegerField()),
            ],
        ),
    ]
