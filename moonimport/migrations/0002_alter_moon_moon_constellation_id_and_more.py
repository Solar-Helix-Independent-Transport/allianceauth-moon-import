# Generated by Django 4.0.10 on 2023-11-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moonimport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moon',
            name='moon_constellation_id',
            field=models.BigIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='moon',
            name='moon_r_rating',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='moon',
            name='moon_region_id',
            field=models.BigIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='moon',
            name='moon_system_id',
            field=models.BigIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='moonores',
            name='type_id',
            field=models.BigIntegerField(db_index=True),
        ),
    ]
