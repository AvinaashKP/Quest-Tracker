from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

status = (
    ('Completed', 'Completed'),
    ('Progress', 'Progress'),
)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    First_name = models.CharField(max_length=20,null=True,blank=True, verbose_name='First Name')
    Last_name = models.CharField(max_length=20,null=True,blank=True, verbose_name='Last Name')
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Username = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=6, null=True, blank=True, choices=gender)
    Address = models.TextField(max_length=50, null=True, blank=True)
    Designation = models.CharField(max_length=30, null=True, blank=True)
    Number = models.CharField(max_length=10, null=True, blank=True)
    Picture = models.FileField(default="User.jpg", upload_to="Profile_pictures", null=True, blank=True)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Username


class Project(models.Model):

    Assigned_to = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    startdate = models.DateField()
    duedate = models.DateField()
    ProName = models.CharField(max_length=20, null=True, blank=True, verbose_name="Project Name")
    Prodesc = models.TextField(max_length=200, null=True, blank=True, verbose_name="Project Description")
    file = models.FileField(null=True, blank=True, upload_to= "Project_file", verbose_name="Project file")
    Status = models.CharField(max_length=10, default="Progress", choices=status, null=True, blank=True)
    Read = models.BooleanField(default=False)
    def __str__(self):
        return self.ProName

class Task(models.Model):

    Assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    startdate = models.DateField()
    duedate = models.DateField()
    TaskName = models.CharField(max_length=20, null=True, blank=True, verbose_name="Task Name")
    Taskdesc = models.TextField(max_length=200, null=True, blank=True, verbose_name="Task Description")
    file = models.FileField(null=True, blank=True, upload_to= "Task_file", verbose_name="Task file")
    Status = models.CharField(max_length=10, default="Progress", choices=status, null=True, blank=True)
    Read = models.BooleanField(default=False)

    def __str__(self):
        return self.TaskName

class Notification(models.Model):
    From = models.CharField(max_length=20, null=True, blank=True)
    To = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Subject = models.CharField(max_length=20, null=True, blank=True)
    Message = models.TextField(max_length=200, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, verbose_name="Date and Time")
    Read = models.BooleanField(default=False)

    def __str__(self):
        return self.Subject