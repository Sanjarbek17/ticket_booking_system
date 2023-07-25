# Generated by Django 4.2.2 on 2023-07-25 14:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_alter_event_number_of_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(blank=True, related_name='Guests', to=settings.AUTH_USER_MODEL),
        ),
    ]
