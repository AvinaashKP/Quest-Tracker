# Generated by Django 4.1.4 on 2023-01-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_notification_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ProStatus',
        ),
        migrations.RemoveField(
            model_name='task',
            name='TaskStatus',
        ),
        migrations.AddField(
            model_name='project',
            name='Status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Project Status'),
        ),
        migrations.AddField(
            model_name='project',
            name='upload_file',
            field=models.FileField(blank=True, max_length=130, null=True, upload_to='project_file', verbose_name='Project file'),
        ),
        migrations.AddField(
            model_name='task',
            name='Status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Task Status'),
        ),
        migrations.AddField(
            model_name='task',
            name='upload_file',
            field=models.FileField(blank=True, max_length=130, null=True, upload_to='task_file', verbose_name='Task file'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProName',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Project Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Prodesc',
            field=models.TextField(blank=True, max_length=130, null=True, verbose_name='Project Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskName',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Task Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='Taskdesc',
            field=models.TextField(blank=True, max_length=130, null=True, verbose_name='Task Description'),
        ),
    ]
