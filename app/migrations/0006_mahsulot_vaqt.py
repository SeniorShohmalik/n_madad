# Generated by Django 5.0 on 2024-01-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_mahsulot_ega_alter_mahsulot_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='vaqt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]