# Generated by Django 2.0.6 on 2018-06-19 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_auto_20180619_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='slug',
        ),
    ]