# Generated by Django 4.0.3 on 2022-04-18 20:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0006_remove_notification_to_adviser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]