# Generated by Django 3.2.2 on 2021-08-23 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogb', '0002_post_privacy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='privacy',
        ),
    ]
