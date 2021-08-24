# Generated by Django 3.2.2 on 2021-08-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='privacy',
            field=models.CharField(choices=[(True, 'Private'), (False, 'Public')], default='Public', max_length=7),
        ),
    ]