# Generated by Django 5.0 on 2024-01-02 03:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_ball_liker_alter_ball_user_alter_loved_liker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='saved',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.loved'),
        ),
        migrations.AddField(
            model_name='mahsulot',
            name='stared',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ball'),
        ),
    ]
