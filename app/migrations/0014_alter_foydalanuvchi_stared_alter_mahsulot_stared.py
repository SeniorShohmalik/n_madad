# Generated by Django 5.0 on 2024-01-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_foydalanuvchi_stared_alter_mahsulot_stared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foydalanuvchi',
            name='stared',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='stared',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
