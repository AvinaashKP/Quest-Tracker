from . models import User, Profile, Project, Task, Notification
from django.shortcuts import render

def Admin_Dashboard(request):

    total_user = User.objects.all().count()
    staff = User.objects.filter(is_staff=True).count()
    active = User.objects.filter(is_staff=False).count()

    return {'user_count': total_user, 'senior_count': staff, 'junior_count': active}

def Profile_Picture(request):
    pic = Profile.objects.all()
    user_pic = pic.filter(user_id=request.user.id)
    return {'pic': user_pic}

def Message_Count(request):
    data1 = Notification.objects.all()
    data2 = Project.objects.all()
    data3 = Task.objects.all()

    get_msg = data1.filter(To_id=request.user.id)
    get_pro = data2.filter(Assigned_to_id=request.user.id)
    get_task = data3.filter(Assigned_to_id=request.user.id)

    get_msg_count = get_msg.filter(Read=False).count()
    get_pro_count = get_pro.filter(Read=False).count()
    get_task_count = get_task.filter(Read=False).count()

    context = {
        'msg_count': get_msg_count,
        'pro_count': get_pro_count,
        'task_count': get_task_count
    }
    return context


