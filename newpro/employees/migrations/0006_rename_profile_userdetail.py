# Generated by Django 4.1.4 on 2023-01-08 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_rename_user_project_assigned_to_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserDetail',
        ),
    ]
