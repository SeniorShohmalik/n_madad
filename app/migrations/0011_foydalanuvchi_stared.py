# Generated by Django 5.0 on 2024-01-02 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_mahsulot_saved_mahsulot_stared'),
    ]

    operations = [
        migrations.AddField(
            model_name='foydalanuvchi',
            name='stared',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ball'),
        ),
    ]
