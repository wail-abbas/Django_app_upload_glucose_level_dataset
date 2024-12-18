# Generated by Django 4.2.13 on 2024-06-21 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("core_app", "0002_user_user_abbreviation")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="birthdate",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="mobile_number",
            field=models.CharField(
                default=django.utils.timezone.now, max_length=20, unique=True
            ),
            preserve_default=False,
        ),
    ]
