# Generated by Django 4.2.13 on 2024-06-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core_app", "0003_user_address_user_birthdate_user_mobile_number")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="mobile_number",
            field=models.CharField(max_length=50),
        )
    ]
