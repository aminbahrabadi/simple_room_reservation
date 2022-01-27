# Generated by Django 4.0.1 on 2022-01-26 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('number_of_seats', models.PositiveIntegerField(default=0, verbose_name='Number of Seats')),
                ('time_of_availability', models.DateTimeField(null=True, verbose_name='Time of Availability')),
                ('reserved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserver', to=settings.AUTH_USER_MODEL, verbose_name='Reserver')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['-created_at'],
            },
        ),
    ]
