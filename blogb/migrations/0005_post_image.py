# Generated by Django 3.2.2 on 2021-08-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogb', '0004_post_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
