# Generated by Django 5.0 on 2024-01-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_foydalanuvchi_stared_alter_foydalanuvchi_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='stared',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]