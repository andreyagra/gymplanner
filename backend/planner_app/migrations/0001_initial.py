# Generated by Django 4.2.5 on 2023-09-22 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('password', models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(message='Password must have at least 6 characters, 1 letter, 1 number, and 1 special character.', regex='^(?=.*[A-Za-z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{6,}$')])),
                ('profile', models.CharField(choices=[('user', 'User'), ('trainer', 'Trainer')], default='user', max_length=7)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
