# Generated by Django 4.0 on 2023-11-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('loginid', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'UserRegistrations',
            },
        ),
    ]
