from django.shortcuts import render, redirect
from . models import Profile, Project, Task, Notification
from django.contrib import messages
import os
from .forms import CreateUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

# Create your views here.


# INDEX PAGE
def indexpage(request):
    logout(request)
    return render(request, 'indexpage/index.html')

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                firstname = form.cleaned_data.get('first_name')
                lastname = form.cleaned_data.get('last_name')
                Profile(Username=username, First_name=firstname, Last_name=lastname, Email=email).save()
                form.save()
                messages.success(request, 'Registration Successful')
                return redirect('/login')
        context = {'form': form}
        return render(request, 'indexpage/registerpage.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method =='POST':
              username = request.POST.get('username')
              password = request.POST.get('password')
              user = authenticate(request, username=username, password=password)

              if user is not None:
                    login(request, user)
                    messages.success(request, 'Welcome ' + username)
                    return redirect('/home')
              else:
                   messages.error(request, 'Incorrect password or username')
                   return redirect("/login")
        return render(request, 'indexpage/loginpage.html')


# ADMIN PAGE
@login_required(login_url="/login")
def user_list(request):
    data = Profile.objects.all()
    context = {'users': data}
    return render(request, "adminpage/userlist.html", context)

def user_details(request, pk):
    data = Profile.objects.get(id=pk)
    context = {'data': data}
    return render(request, "adminpage/userdetails.html", context)

@login_required(login_url="/login")
def user_projects(request):
    data = Project.objects.all()
    context = {'project': data}
    return render(request, "adminpage/viewprojects.html", context)

@login_required(login_url="/login")
def add_projects(request):
    userlist = User.objects.all()
    data = Project()
    if request.method == 'POST':
        data.Assigned_to_id = request.POST.get('assigned')
        data.startdate = request.POST.get('sdate')
        data.duedate = request.POST.get('ddate')
        data.ProName = request.POST.get('pname')
        data.Prodesc = request.POST.get('desc')
        data.save()
        return redirect("/view_projects")
    context = {'users': userlist}
    return render(request, "adminpage/addprojects.html", context)

@login_required(login_url="/login")
def edit_projects(request, pk):
    data = Project.objects.get(id=pk)
    if request.method == 'POST':
        data.ProName = request.POST.get('pname')
        data.Prodesc = request.POST.get('desc')
        data.startdate = request.POST.get('sdate')
        data.duedate = request.POST.get('ddate')
        data.save()
        return redirect("/view_projects")
    context = {'data': data}
    return render(request, "adminpage/editprojects.html", context)

@login_required(login_url="/login")
def user_tasks(request):
    data = Task.objects.all()
    context = {'task': data}
    return render(request, "adminpage/viewtasks.html", context)

@login_required(login_url="/login")
def add_tasks(request):
    data = User.objects.all()
    context = {'users': data}
    return render(request, "adminpage/addtasks.html", context)

@login_required(login_url="/login")
def edit_tasks(request, pk):
    data = Task.objects.get(id=pk)
    context = {'data': data}
    return render(request, "adminpage/edittasks.html", context)

def delete_project(request, pk):
    Project.objects.filter(id=pk).delete()
    return redirect('/view_projects')

def delete_task(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('/view_tasks')

# HOME PAGE
@login_required(login_url="/login")
def homepage(request):
    Username = request.user
    ID = request.user.id
    data = Profile.objects.get(Username=Username)

    if data.user_id == None:     # To update the profile id of users
        data.user_id = ID
        data.save()

    if not request.user.is_superuser and not request.user.is_staff:   # Group name is automatically assigned for Users
            my_group = Group.objects.get(name='Junior Staff')
            my_group.user_set.add(request.user)

    # To get Project Status
    project_by_ID = Project.objects.filter(Assigned_to_id=ID)
    count_project_progress = project_by_ID.filter(Status="progress").count()
    count_project_completed = project_by_ID.filter(Status="completed").count()

    # To get Task Status
    task_by_ID = Task.objects.filter(Assigned_to_id=ID)
    count_task_progress = task_by_ID.filter(Status="progress").count()
    count_task_completed = task_by_ID.filter(Status="completed").count()

    context = {
            'PC': count_project_completed,
            'PP': count_project_progress,
            'TC': count_task_completed,
            'TP': count_task_progress,
            'data': data,
            }
    return render(request, "homepage/dashboard.html", context)

@login_required(login_url="/login")
def project_list(request):
    data = Project.objects.all()
    context = {'project': data}
    return render(request, 'projects/projectlist.html', context)

@login_required(login_url="/login")
def project_details(request, pk):
    data = Project.objects.get(id=pk)
    if request.method == 'POST':
        data.file = request.FILES.get('project_file')

        if data.file != 'None':
            data.Status = "Completed"

        else:
            data.Status = "Progress"

        data.save()
        messages.success(request, 'Project Submitted Successfully')
        return redirect('/projects')

    data.Read = True
    data.save()

    context = {'data': data}
    return render(request, 'projects/projectdetails.html', context)

@login_required(login_url="/login")
def task_list(request):
    data = Task.objects.all()
    context = {'task': data}
    return render(request, 'tasks/tasklist.html', context)

@login_required(login_url="/login")
def task_details(request, pk):
    data = Task.objects.get(id=pk)
    if request.method == 'POST':

        if data.file != 'None':
            data.Status = "Completed"
        else:
            data.Status = "Progress"

        data.file = request.FILES.get('task_file')
        data.save()
        messages.success(request, 'Task Submitted Successfully')
        return redirect('/tasks')

    data.Read = True
    data.save()
    context = {'data': data}
    return render(request, 'tasks/taskdetails.html', context)

@login_required(login_url="/login")
def settings(request):
    data = Profile.objects.all()
    return render(request, 'homepage/settings.html',{'data': data})

@login_required(login_url="/login")
def viewprofile(request):
    data = Profile.objects.all()
    return render(request, 'profile/viewprofile.html', {'data': data})

@login_required(login_url="/login")
def editprofile(request, pk):
    data = Profile.objects.get(id=pk)
    if request.method == 'POST':
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        designation = request.POST.get('designation')
        number = request.POST.get('number')
        if len(request.FILES) != 0:
            if os.path.exists(data.Picture.url):
                os.remove(data.Picture.path)
            data.Picture = request.FILES.get('picture')
        data.Gender = gender
        data.Address = address
        data.Designation = designation
        data.Number = number

        if data.Picture != "User.jpg" and data.Gender != None and data.Address != None\
                and data.Designation != None and data.Number != None:

            data.Status = True
        else:
            data.Status = False

        data.save()
        messages.success(request, 'Profile Updated Successfully')
        return redirect('/view_profile')
    return render(request, 'profile/editprofile.html', {'data': data})

@login_required(login_url="/login")
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'homepage/resetpassword.html', {'form': form})

@login_required(login_url="/login")
def notification(request):
    data2 = Notification.objects.all()
    context = {'inbox': data2}
    return render(request, 'homepage/notification.html', context)

@login_required(login_url="/login")
def read_message(request, pk):
    data = Notification.objects.get(id=pk)
    data.Read = True
    data.save()
    context = {'data': data}
    return render(request, 'homepage/readmessage.html', context)


