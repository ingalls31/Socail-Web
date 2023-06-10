# Generated by Django 4.1.7 on 2023-03-11 06:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0003_alter_customuser_options_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_online',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]