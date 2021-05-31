from django.shortcuts import render, redirect
from .models import Users

# Create your views here.


def index(request):
    return render(request, 'index.html')


def student_index(request):
    return render(request, 'student/index.html')


def student_join_course(request):
    return render(request, 'student/join_course.html')


def student_to_do(request):
    return render(request, 'student/to_do.html')


def student_profile(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        return render(request, 'student/edit_profile.html', {'user': user})
    else:
        return render(request, 'student/edit_profile.html')


def teacher_index(request):
    return render(request, 'Teacher/teacherSpace.html')


def user_logout(request):
    return redirect('PFES6:index')


def user_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users.objects.get(email=email)

        if user is not None and password == user.password:
            if user.role == 's':
                return render(request, 'student/index.html', {'user': user})
            else:
                return render(request, 'teacher/teacherSpace.html', {'user': user})
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')
