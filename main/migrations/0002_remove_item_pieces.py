# Generated by Django 2.2.7 on 2021-12-07 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='pieces',
        ),
    ]