# Generated by Django 3.2.4 on 2021-08-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_subeb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_ling', models.CharField(max_length=300)),
                ('b_date', models.DateField()),
            ],
        ),
    ]
