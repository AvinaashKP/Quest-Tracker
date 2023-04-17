# Generated by Django 4.1.4 on 2023-01-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_alter_project_upload_file_alter_task_upload_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Status',
            field=models.CharField(blank=True, default='progress', max_length=10, null=True, verbose_name='Project Status'),
        ),
        migrations.AlterField(
            model_name='task',
            name='Status',
            field=models.CharField(blank=True, default='progress', max_length=10, null=True, verbose_name='Task Status'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='Picture',
            field=models.FileField(blank=True, default='User.jpg', null=True, upload_to='Profile_pictures'),
        ),
    ]
