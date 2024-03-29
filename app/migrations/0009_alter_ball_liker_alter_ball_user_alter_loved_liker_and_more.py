# Generated by Django 5.0 on 2024-01-01 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_loved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ball',
            name='liker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like', to='app.foydalanuvchi'),
        ),
        migrations.AlterField(
            model_name='ball',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app.foydalanuvchi'),
        ),
        migrations.AlterField(
            model_name='loved',
            name='liker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lover', to='app.foydalanuvchi'),
        ),
        migrations.AlterField(
            model_name='loved',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loved', to='app.foydalanuvchi'),
        ),
    ]
