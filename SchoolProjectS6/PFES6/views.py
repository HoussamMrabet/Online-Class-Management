from django.shortcuts import render, redirect
from .models import JoinClass, Todo, Users, classSubject, course, TP, TD, correction_TD_TP

# Create your views here.


def index(request):
    return render(request, 'index.html')


def student_index(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        classIns = JoinClass.objects.filter(userId=user)
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
    todo = Todo.objects.filter(course=classe)
    return render(request, 'student/course.html', {'user': user, 'userT': userT, 'class': classe, 'course': cours, 'td': td, 'tp': tp, 'corr': corr, 'todo': todo})


def student_join_course(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        return render(request, 'student/join_course.html', {'user': user})
    elif request.method == 'POST':
        userId = request.POST.get('userId')
        code = request.POST.get('codeC')
        user = Users.objects.get(id=userId)
        if classSubject.objects.filter(codeClasse=code).count() > 0:
            classe = classSubject.objects.get(codeClasse=code)
            userTId = classe.userId.id
            userT = Users.objects.get(id=userTId)
            if JoinClass.objects.filter(userId=user, classId=classe).count() > 0:
                return render(request, 'student/join_course.html', {'user': user, 'x': True})
            else:
                courj = JoinClass(userId=user, classId=classe)
                courj.save()
                cours = course.objects.filter(course=classe)
                td = TD.objects.filter(course=classe)
                tp = TP.objects.filter(course=classe)
                corr = correction_TD_TP.objects.filter(course=classe)
                todo = Todo.objects.filter(course=classe)
                return render(request, 'student/course.html', {'user': user, 'userT': userT, 'class': classe, 'course': cours, 'td': td, 'tp': tp, 'corr': corr, 'todo': todo})
        else:
            return render(request, 'student/join_course.html', {'user': user, 'c': True})
    else:
        return render(request, 'student/join_course.html')


def student_to_do(request):
    if request.method == 'GET':
        id = request.GET.get('userId')
        user = Users.objects.get(id=id)
        join = JoinClass.objects.filter(userId=user)
        todo = Todo.objects.all()
        return render(request, 'student/to_do.html', {'user': user, 'todo': todo, 'join': join})
    else:
        return render(request, 'student/to_do.html')


def student_put_todo(request):
    if request.method == 'POST':
        id = request.POST.get('todoId')
        userId = request.POST.get('userId')
        todo = Todo.objects.get(id=id)
        title = todo.title
        creationDateTodo = todo.creationDateTodo
        TodoTFile = todo.TodoTFile
        course = todo.course
        TodoSFile = request.FILES.get('todo')
        todoUp = Todo(id=id, title=title, creationDateTodo=creationDateTodo,
                      TodoTFile=TodoTFile, TodoSFile=TodoSFile, course=course)
        todoUp.save()
        user = Users.objects.get(id=userId)
        join = JoinClass.objects.filter(userId=user)
        todo = Todo.objects.all()
        return render(request, 'student/to_do.html', {'user': user, 'todo': todo, 'join': join})
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
        opassword = request.POST.get('oldpass')
        password = request.POST.get('newpass')
        cpassword = request.POST.get('newpass2')
        user = Users.objects.get(id=id)
        if opassword != "":
            if user.password != opassword:
                p = True
                return render(request, 'student/edit_profile.html', {'user': user, 'p': p})
            else:
                if password != cpassword:
                    np = True
                    return render(request, 'student/edit_profile.html', {'user': user, 'np': np})
                else:
                    picture = user.picture.name
                    role = user.role
                    userUp = Users(id=id, nom=nom, prenom=prenom,
                                   email=email, password=password, picture=picture, role=role)
                    userUp.save()
                    user = Users.objects.get(id=id)
                    return render(request, 'student/edit_profile.html', {'user': user})
        else:
            picture = user.picture.name
            role = user.role
            userUp = Users(id=id, nom=nom, prenom=prenom,
                           email=email, password=user.password, picture=picture, role=role)
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

        userf = Users.objects.filter(email=email)

        if userf.count() > 0:
            user = Users.objects.get(email=email)
            if password == user.password:
                classIns = JoinClass.objects.filter(userId=user)
                if user.role == 's':
                    return render(request, 'student/index.html', {'user': user, 'join': classIns})
                else:
                    return render(request, 'teacher/teacherSpace.html', {'user': user})
            else:
                return render(request, 'index.html')
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
    classIns = JoinClass.objects.filter(userId=user)
    return render(request, 'student/index.html', {'user': user, 'join': classIns})
