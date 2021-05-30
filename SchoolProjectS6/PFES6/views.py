from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib import messages
from .models import userApp
# Create your views here.

'''
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        ps = request.POST['psw']
        user = userApp(email=email, password=ps)
=======
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

>>>>>>> 83f27afee888c4afde06d3493f85a085b76a5d2e
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
<<<<<<< HEAD
        return render(request, 'index.html')
'''
=======
        return render(request, 'index.html', {})
>>>>>>> 83f27afee888c4afde06d3493f85a085b76a5d2e
