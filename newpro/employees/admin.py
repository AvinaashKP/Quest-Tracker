from django.contrib import admin
from .models import Profile, Project, Task, Notification
# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display = ['Username', 'Email', 'Designation', 'Status']
    search_fields = ['Username']

class AdminProject(admin.ModelAdmin):
    list_display = ['ProName', 'Assigned_to', 'startdate', 'duedate', 'Status']
    search_fields = ['ProName']

class AdminTask(admin.ModelAdmin):
    list_display = ['TaskName', 'Assigned_to', 'startdate', 'duedate', 'Status']
    search_fields = ['TaskName']

class AdminNotification(admin.ModelAdmin):
    list_display = ['Subject', 'Date', 'Read']
    search_fields = ['Subject']

admin.site.register(Profile, AdminProfile)
admin.site.register(Project, AdminProject)
admin.site.register(Task, AdminTask)
admin.site.register(Notification, AdminNotification)
