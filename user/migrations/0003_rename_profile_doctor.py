# Generated by Django 4.1 on 2022-09-29 16:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_alter_appointment_doctor_alter_appointment_patient'),
        ('user', '0002_alter_profile_favourite'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Doctor',
        ),
    ]
