from django.shortcuts import render, redirect
from .models import JoinClass, Users, classSubject, course, TP, TD, correction_TD_TP

# Create your views here.


def index(request):
    return render(request, 'index.html')


def student_index(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        classIns = JoinClass.objects.filter(usersId=user)
        return render(request, 'student/index.html', {'user': user, 'join': classIns})
    else:
        return render(request, 'student/index.html')


def student_course(request):
    userId = request.GET.get('userId')
    classId = request.GET.get('courseId')
    classe = classSubject.objects.get(id=classId)
    user = Users.objects.get(id=userId)
    userTId = classe.userId.id
    userT = Users.objects.get(id=userTId)
    cours = course.objects.filter(course=classe)
    td = TD.objects.filter(course=classe)
    tp = TP.objects.filter(course=classe)
    corr = correction_TD_TP.objects.filter(course=classe)
    return render(request, 'student/course.html', {'user': user, 'userT': userT, 'class': classe, 'course': cours, 'td': td, 'tp': tp, 'corr': corr})


def student_join_course(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        return render(request, 'student/join_course.html', {'user': user})
    elif request.method == 'POST':
        userId = request.POST.get('userId')
        code = request.POST.get('codeC')
        classe = classSubject.objects.get(codeClasse=code)
        user = Users.objects.get(id=userId)
        userTId = classe.userId.id
        userT = Users.objects.get(id=userTId)
        courj = JoinClass(usersId=user, classId=classe)
        courj.save()
        cours = course.objects.filter(course=classe)
        td = TD.objects.filter(course=classe)
        tp = TP.objects.filter(course=classe)
        corr = correction_TD_TP.objects.filter(course=classe)
        return render(request, 'student/course.html', {'user': user, 'userT': userT, 'class': classe, 'course': cours, 'td': td, 'tp': tp, 'corr': corr})
    else:
        return render(request, 'student/join_course.html')


def student_to_do(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        return render(request, 'student/to_do.html', {'user': user})
    else:
        return render(request, 'student/to_do.html')


def student_profile(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        return render(request, 'student/edit_profile.html', {'user': user})
    else:
        return render(request, 'student/edit_profile.html')


def student_picture(request):
    if request.method == 'POST':
        id = request.POST.get('userId')
        user = Users.objects.get(id=id)
        nom = user.nom
        prenom = user.prenom
        email = user.email
        password = user.password
        picture = request.FILES.get('picture')
        role = user.role
        userUp = Users(id=id, nom=nom, prenom=prenom,
                       email=email, password=password, picture=picture, role=role)
        userUp.save()
        user = Users.objects.get(id=id)
        return render(request, 'student/edit_profile.html', {'user': user})
    else:
        return render(request, 'student/edit_profile.html')


def student_edit_profile(request):
    if request.method == 'POST':
        id = request.POST.get('userId')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('newpass')
        user = Users.objects.get(id=id)
        picture = user.picture.name
        role = user.role
        userUp = Users(id=id, nom=nom, prenom=prenom,
                       email=email, password=password, picture=picture, role=role)
        userUp.save()
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
            classIns = JoinClass.objects.filter(usersId=user)
            if user.role == 's':
                return render(request, 'student/index.html', {'user': user, 'join': classIns})
            else:
                return render(request, 'teacher/teacherSpace.html', {'user': user})
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def destroy(request):
    id = request.POST.get('todelete')
    userId = request.POST.get('userId')
    join = JoinClass.objects.get(id=id)
    join.delete()
    user = Users.objects.get(id=userId)
    classIns = JoinClass.objects.filter(usersId=user)
    return render(request, 'student/index.html', {'user': user, 'join': classIns})
