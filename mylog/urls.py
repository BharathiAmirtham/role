
from django.contrib import admin
from django.urls import path, include
from myapp import views
from myapp import forms



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.register, name='register'),
    path("user_login/", views.user_login, name="login"),
    path("user_logout/", views.user_logout, name='logout'),
    path("home/", views.home, name='home'),
    path("delete/<int:person_id>/", views.delete_person, name='delete_person'),
    path("home/teacher_register_form/", views.teacher_register_form, name='teacher'),
    path("home/student_register_form/", views.student_register_form, name='student'),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("show_details/", views.show_details, name="show_details"),
    path("delete_user/<int:user_id>/", views.delete_user, name='delete_user'),



]






    
