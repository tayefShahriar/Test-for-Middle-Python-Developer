# Generated by Django 4.2.3 on 2023-09-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('roll', models.IntegerField()),
                ('address', models.TextField()),
                ('mobile', models.CharField(max_length=75)),
            ],
        ),
    ]
