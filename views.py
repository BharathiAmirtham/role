from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import csv
from .forms import UploadCSVForm
import io
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.hashers import make_password




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff == True:
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return redirect('home.html')

            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string, delimiter=',')
            next(reader)  

            added_count = 0
            skipped_count = 0

            for row in reader:
                name=row[0]
                email=row[1]
                department=row[2]

                if Person.objects.filter(name=name).exists():
                    skipped_count += 1
                    continue    
                
                Person.objects.create(
                    name=name,
                    email=email,
                    department=department,
                )
                added_count += 1
            
            messages.success(request, f'Successfully added {added_count} entries.')
            return redirect('home')
                
    else:
        form = UploadCSVForm()
        data=Person.objects.all()
        print(data,"data")
        return render(request, 'home.html', {'form': form,'data':data})

def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    messages.success(request, f"Deleted {person.name}'s Details.")
    return redirect('home')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        return redirect('show_details')
        # if user is not None:
        #         login(request, user)
        #         return redirect('home')

    else:
        messages.error(request, 'Invalid credentials')
    return render(request, 'user_login.html')

def teacher_register_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        biometric_id = request.POST.get('biometric_id')
        phone_no = request.POST['phone_no']
        city = request.POST['city']
        User.objects.create(username=biometric_id,first_name=username,password=make_password("teacher@123"))
        user_id=User.objects.latest('id')
        userId=user_id.id
        role=Role.objects.get(role="teacher")
        user = Admin.objects.create(
                user_id=userId,
                biometric_id=biometric_id,
                phone_no=phone_no,
                city = city,
                role=role,
                )

        messages.success(request, 'Account created successfully')
        return redirect('admin_login')
    return render(request, 'teacher_register.html')


def student_register_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        roll_no = request.POST['roll_no']
        phone_no = request.POST['phone_no']
        city = request.POST['city']
        User.objects.create(username=roll_no,first_name=username,password=make_password("student@123"))
        user_id=User.objects.latest('id')
        userId=user_id.id
        role=Role.objects.get(role="student")
        Admin.objects.create(
                user_id=userId,
                roll_no=roll_no,
                phone_no=phone_no,
                city = city,
                role=role,
                )
            
        messages.success(request, 'Account created successfully')
        return redirect('admin_login')
    return render(request, 'student_register.html')

def show_details(request):
    if request.method == 'POST':
        for row in data:
                username=row[0]
                roll_no=row[1]
                phone_no=row[2]
                city=row[3]
                role=row[4]

                if User.objects.filter(username=username).exists():
                    skipped_count += 1
                    continue    
                
                User.objects.create(
                    roll_no=roll_no,
                    phone_no=phone_no,
                    city = city,
                    role=role,
                )
                added_count += 1
            
        messages.success(request, f'Successfully added {added_count} entries.')
        return redirect('show_details')
    data=User.objects.all()
    print(data,"data")
    return render(request, 'show_details.html', {'data':data})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, f"Deleted {user.username}'s Details.")
    return redirect('show_details')
