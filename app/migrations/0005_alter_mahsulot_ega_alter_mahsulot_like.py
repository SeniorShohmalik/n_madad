# Generated by Django 5.0 on 2024-01-01 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mahsulot_bonus_mahsulot_chegirma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='ega',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ega', to='app.foydalanuvchi'),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='likers', to='app.foydalanuvchi'),
        ),
    ]
