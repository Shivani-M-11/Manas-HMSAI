# Generated by Django 5.1.6 on 2025-03-05 18:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('No_of_doctors', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(default='We have skilled doctors')),
                ('phoneno', models.CharField(default='0000000000', max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits.', regex='^\\d{10}$')])),
            ],
        ),
    ]
