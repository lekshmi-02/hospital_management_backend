# Generated by Django 4.2 on 2023-04-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('doctorname', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
            ],
        ),
    ]
