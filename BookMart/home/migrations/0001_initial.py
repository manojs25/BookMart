# Generated by Django 4.0.5 on 2022-12-15 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('mobile', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('passwd', models.CharField(max_length=8)),
            ],
        ),
    ]
