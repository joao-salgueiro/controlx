# Generated by Django 5.1.7 on 2025-06-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_gamingcontroller_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamingcontroller',
            name='post_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
