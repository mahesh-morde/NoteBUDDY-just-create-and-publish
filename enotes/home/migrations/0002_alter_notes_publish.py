# Generated by Django 5.0 on 2023-12-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]