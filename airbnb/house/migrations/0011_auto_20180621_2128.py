# Generated by Django 2.0.6 on 2018-06-21 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0010_auto_20180621_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenities',
            name='amenities_type',
        ),
        migrations.AddField(
            model_name='amenities',
            name='house',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='house.House'),
            preserve_default=False,
        ),
    ]