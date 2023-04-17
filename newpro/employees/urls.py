from django.urls import path
from . import views

urlpatterns = [

    # Index page
    path('', views.indexpage, name='LOGOUT'),
    path('admin/', views.indexpage, name='ADMIN'),
    path('register/', views.registerpage, name='REGISTER'),
    path('login/', views.loginpage, name='LOGIN'),

    # Admin Page
    path('view_user_list', views.user_list, name='USER_LIST'),
    path('view_user_details/<int:pk>/', views.user_details, name='USER_DETAILS'),
    path('view_projects/', views.user_projects, name='USER_PROJECT'),
    path('view_tasks/', views.user_tasks, name='USER_TASK'),
    path('add_projects/', views.add_projects, name='ADD_PROJECT'),
    path('add_tasks/', views.add_tasks, name='ADD_TASK'),
    path('edit_projects/<int:pk>/', views.edit_projects, name='EDIT_PROJECT'),
    path('edit_tasks/<int:pk>/', views.edit_tasks, name='EDIT_TASK'),
    path('delete_project/<int:pk>/', views.delete_project, name='DELETE_PROJECT'),
    path('delete_task/<int:pk>/', views.delete_task, name='DELETE_TASK'),

    # Home page
    path('home/', views.homepage, name='DASHBOARD'),
    path('projects/', views.project_list, name='MYPROJECT'),
    path('tasks/', views.task_list, name='MYTASK'),
    path('notification/', views.notification, name='NOTIFICATION'),
    path('view_profile/', views.viewprofile, name='VIEW_PROFILE'),
    path('settings/', views.settings, name='SETTINGS'),
    path('reset_password/', views.ChangePassword, name='RESET_PASSWORD'),
    path('edit_profile/<int:pk>/', views.editprofile, name='EDIT_PROFILE'),
    path('project_details/<int:pk>/', views.project_details, name='PROJECT_DETAILS'),
    path('task_details/<int:pk>/', views.task_details, name='TASK_DETAILS'),
    path('notification_read/<int:pk>/', views.read_message, name='READ_MESSAGE'),

]