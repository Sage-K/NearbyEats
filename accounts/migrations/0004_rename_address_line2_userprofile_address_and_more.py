# Generated by Django 5.1.5 on 2025-03-12 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line2',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_1',
        ),
    ]
