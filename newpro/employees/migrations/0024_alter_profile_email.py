# Generated by Django 4.1.4 on 2023-02-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0023_alter_project_status_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]