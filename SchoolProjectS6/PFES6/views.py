from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def student_index(request):
    return render(request, 'student/index.html')


def teacher_index(request):
    return render(request, 'Teacher/allCourses.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('PFES6:index')


def user_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            userInfo = Users.objects.get(email=email)
            if userInfo.role == 'student':
                return render(request, 'student/index.html', {'user': userInfo})

            elif userInfo.role == 'teacher':
                return render(request, 'Teacher/teacherSpace.html', {'user': userInfo})

            else:
                return redirect('PFES6:index')
        else:
            return redirect('PFES6:teacher')
    else:
        return render(request, 'index.html', {})
