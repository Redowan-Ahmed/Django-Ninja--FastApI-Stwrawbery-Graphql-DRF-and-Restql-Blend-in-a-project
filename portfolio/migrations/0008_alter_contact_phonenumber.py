# Generated by Django 4.2.7 on 2023-12-02 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_contact_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phoneNumber',
            field=models.CharField(default=8801632398271, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
