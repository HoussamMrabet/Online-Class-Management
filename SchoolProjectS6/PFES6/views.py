from django.shortcuts import render, redirect
from .models import JoinClass, Todo, Users, classSubject, course, TP, TD, correction_TD_TP
import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


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
                    classeS = classSubject.objects.filter(userId=user)
                    d = datetime.datetime.now().strftime('%Y-%m-%d')
                    students = JoinClass.objects.filter(classId__in=classeS)
                    t = []
                    for c in classeS:
                        st = 0
                        studentsPerClasse = JoinClass.objects.filter(classId=c)
                        for spc in studentsPerClasse:
                            st += 1
                        t.append({'titleC': c.titleClass, 'st': st})
                    e = 0
                    for et in students:
                        e += 1
                    nb = 0
                    for n in classeS:
                        nb += 1

                    return render(request, 'teacher/teacherSpace.html', {'liste': t, 'e': e, 'DC': d, 'nb': nb, 'user': user, 'classeS': classeS})
            else:
                return render(request, 'index.html')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def user_logout(request):
    return redirect('PFES6:index')

# Student views


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


def destroy(request):
    id = request.POST.get('todelete')
    userId = request.POST.get('userId')
    join = JoinClass.objects.get(id=id)
    join.delete()
    user = Users.objects.get(id=userId)
    classIns = JoinClass.objects.filter(userId=user)
    return render(request, 'student/index.html', {'user': user, 'join': classIns})

# Teacher Views


def teacher_index(request):
    return render(request, 'Teacher/teacherSpace.html')


def statistics(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    classe = classSubject.objects.filter(userId=user)
    d = datetime.datetime.now().strftime('%Y-%m-%d')
    students = JoinClass.objects.filter(classId__in=classe)
    classeS = classSubject.objects.filter(userId=user)
    t = []
    for c in classeS:
        st = 0
        studentsPerClasse = JoinClass.objects.filter(classId=c)
        for spc in studentsPerClasse:
            st += 1
        t.append({'titleC': c.titleClass, 'st': st})
    e = 0
    for et in students:
        e += 1

    nb = 0
    for n in classe:
        nb += 1
    classeS = classSubject.objects.filter(userId=user)

    return render(request, 'Teacher/teacherSpace.html', {'liste': t, 'e': e, 'DC': d, 'nb': nb, 'user': user, 'classe': classe, 'classeS': classeS})


def displayAllStudents(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    idC = request.GET.get('idC')
    classe = classSubject.objects.get(id=idC)
    students = JoinClass.objects.filter(classId=classe)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/allStudents.html', {'user': user, 'classe': classe, 'classeS': classeS, 'myStudents': students})


def sendingHW(request):
    if request.method == 'POST':
        id = request.POST.get('idu')
        user = Users.objects.get(id=id)
        desc = request.POST.get('desc')
        dateCreation = datetime.datetime.now().strftime('%Y-%m-%d')
        fileHW = request.FILES.get('homeworkS')
        classeName = request.POST.get('course')
        cours = classSubject.objects.get(titleClass=classeName)
        sendHW = Todo(title=desc, creationDateTodo=dateCreation,
                      TodoTFile=fileHW, TodoSFile='', course=cours)
        sendHW.save()
        classe = classSubject.objects.filter(userId=user)
        classeS = classSubject.objects.filter(userId=user)
        return render(request, 'Teacher/allCourses.html', {'user': user, 'classe': classe, 'classeS': classeS})


def formUploadHW(request):
    idc = request.GET.get('uId')
    user = Users.objects.get(id=idc)
    urCourses = classSubject.objects.filter(userId=user)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/formUploadHW.html', {'user': user, 'classeS': classeS, 'urCourses': urCourses})


def deleteCorr(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    idC = request.GET.get('idC')
    classe = classSubject.objects.get(id=idC)
    idFileCorr = request.GET.get('idFileCorr')
    dataCorr = correction_TD_TP.objects.get(id=idFileCorr)
    dataCorr.delete()
    courseFile = course.objects.filter(course=classe)
    tdFiles = TD.objects.filter(course=classe)
    tpFiles = TP.objects.filter(course=classe)
    corrFiles = correction_TD_TP.objects.filter(course=classe)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/courseDetails.html', {'user': user, 'classe': classe, 'classeS': classeS, 'courses': courseFile, 'tdFiles': tdFiles, 'tpFiles': tpFiles, 'corrFiles': corrFiles})


def deleteTP(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    idC = request.GET.get('idC')
    classe = classSubject.objects.get(id=idC)
    idFileTP = request.GET.get('idFileTP')
    datatp = TP.objects.get(id=idFileTP)
    datatp.delete()
    courseFile = course.objects.filter(course=classe)
    tdFiles = TD.objects.filter(course=classe)
    tpFiles = TP.objects.filter(course=classe)
    corrFiles = correction_TD_TP.objects.filter(course=classe)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/courseDetails.html', {'user': user, 'classe': classe, 'classeS': classeS, 'courses': courseFile, 'tdFiles': tdFiles, 'tpFiles': tpFiles, 'corrFiles': corrFiles})


def deleteTD(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    idC = request.GET.get('idC')
    classe = classSubject.objects.get(id=idC)
    idFileTD = request.GET.get('idFileTD')
    datatd = TD.objects.get(id=idFileTD)
    datatd.delete()
    courseFile = course.objects.filter(course=classe)
    tdFiles = TD.objects.filter(course=classe)
    tpFiles = TP.objects.filter(course=classe)
    corrFiles = correction_TD_TP.objects.filter(course=classe)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/courseDetails.html', {'user': user, 'classe': classe, 'classeS': classeS, 'courses': courseFile, 'tdFiles': tdFiles, 'tpFiles': tpFiles, 'corrFiles': corrFiles})


def deleteCourseFile(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    idC = request.GET.get('idC')
    classe = classSubject.objects.get(id=idC)
    idFileCourse = request.GET.get('idFileC')
    dataC = course.objects.get(id=idFileCourse)
    dataC.delete()
    courseFile = course.objects.filter(course=classe)
    tdFiles = TD.objects.filter(course=classe)
    tpFiles = TP.objects.filter(course=classe)
    corrFiles = correction_TD_TP.objects.filter(course=classe)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/courseDetails.html', {'user': user, 'classe': classe, 'classeS': classeS, 'courses': courseFile, 'tdFiles': tdFiles, 'tpFiles': tpFiles, 'corrFiles': corrFiles})


def addingCorr(request):
    if request.method == 'POST':
        id = request.POST.get('idu')
        user = Users.objects.get(id=id)
        desc = request.POST.get('desc')
        dateCreation = datetime.datetime.now().strftime('%Y-%m-%d')
        fileCorr = request.FILES.get('fileCorr')
        classeName = request.POST.get('course')
        cours = classSubject.objects.get(titleClass=classeName)
        Corrfile = correction_TD_TP(
            title=desc, creationDateTdTp=dateCreation, corrFile=fileCorr, course=cours)
        Corrfile.save()
        classe = classSubject.objects.filter(userId=user)
        classeS = classSubject.objects.filter(userId=user)
        return render(request, 'Teacher/allCourses.html', {'user': user, 'classe': classe, 'classeS': classeS})


def formUploadCorre(request):
    idc = request.GET.get('uId')
    user = Users.objects.get(id=idc)
    urCourses = classSubject.objects.filter(userId=user)
    classe = classSubject.objects.filter(userId=user)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/formUploadCorr.html', {'user': user, 'urCourses': urCourses, 'classeS': classeS, 'classe': classe})


def addingTP(request):
    if request.method == 'POST':
        id = request.POST.get('idu')
        user = Users.objects.get(id=id)
        desc = request.POST.get('desc')
        dateCreation = datetime.datetime.now().strftime('%Y-%m-%d')
        fileTP = request.FILES.get('fileTP')
        classeName = request.POST.get('course')
        cours = classSubject.objects.get(titleClass=classeName)
        tpfile = TP(titleTp=desc, creationDateTp=dateCreation,
                    tpFile=fileTP, course=cours)
        tpfile.save()
        classe = classSubject.objects.filter(userId=user)
        classeS = classSubject.objects.filter(userId=user)
        return render(request, 'Teacher/allCourses.html', {'user': user, 'classe': classe, 'classeS': classeS})


def formUploadTP(request):
    idc = request.GET.get('uId')
    user = Users.objects.get(id=idc)
    urCourses = classSubject.objects.filter(userId=user)
    classe = classSubject.objects.filter(userId=user)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/formUploadTp.html', {'user': user, 'urCourses': urCourses, 'classe': classe, 'classeS': classeS})


def addingTD(request):
    if request.method == 'POST':
        id = request.POST.get('idu')
        user = Users.objects.get(id=id)
        desc = request.POST.get('desc')
        dateCreation = datetime.datetime.now().strftime('%Y-%m-%d')
        fileTD = request.FILES.get('fileTD')
        classeName = request.POST.get('course')
        cours = classSubject.objects.get(titleClass=classeName)
        tdfile = TD(titleTd=desc, creationDateTd=dateCreation,
                    tdFile=fileTD, course=cours)
        tdfile.save()
        classe = classSubject.objects.filter(userId=user)
        classeS = classSubject.objects.filter(userId=user)
        return render(request, 'Teacher/allCourses.html', {'user': user, 'classe': classe, 'classeS': classeS})


def formUploadTD(request):
    idc = request.GET.get('uId')
    user = Users.objects.get(id=idc)
    urCourses = classSubject.objects.filter(userId=user)
    classe = classSubject.objects.filter(userId=user)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/formUploadTD.html', {'user': user, 'classeS': classeS, 'urCourses': urCourses, 'classe': classe})


def displayCourseDetails(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    idC = request.GET.get('idC')
    classe = classSubject.objects.get(id=idC)
    courseFile = course.objects.filter(course=classe)
    tdFiles = TD.objects.filter(course=classe)
    tpFiles = TP.objects.filter(course=classe)
    corrFiles = correction_TD_TP.objects.filter(course=classe)
    homeWorks = Todo.objects.filter(course=classe)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/courseDetails.html', {'homeWorks': homeWorks, 'user': user, 'classeS': classeS, 'classe': classe, 'courses': courseFile, 'tdFiles': tdFiles, 'tpFiles': tpFiles, 'corrFiles': corrFiles})


def deleteCourse(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    idC = request.GET.get('idC')
    dataC = classSubject.objects.get(id=idC)
    dataC.delete()
    classe = classSubject.objects.filter(userId=user)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/allCourses.html', {'user': user, 'classe': classe, 'classeS': classeS})


def addingCourse(request):
    if request.method == 'POST':
        id = request.POST.get('idu')
        user = Users.objects.get(id=id)
        desc = request.POST.get('desc')
        dateCreation = datetime.datetime.now().strftime('%Y-%m-%d')
        fileC = request.FILES.get('fileC')
        classeName = request.POST.get('course')
        cours = classSubject.objects.get(titleClass=classeName)
        coursefile = course(
            desc=desc, creationDateCourse=dateCreation, courseFile=fileC, course=cours)
        coursefile.save()
        classe = classSubject.objects.filter(userId=user)
        classeS = classSubject.objects.filter(userId=user)
        return render(request, 'Teacher/allCourses.html', {'user': user, 'classe': classe, 'classeS': classeS})


def formUploadC(request):
    idc = request.GET.get('uId')
    user = Users.objects.get(id=idc)
    urCourses = classSubject.objects.filter(userId=user)
    classe = classSubject.objects.filter(userId=user)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/formUploadCourse.html', {'user': user, 'urCourses': urCourses, 'classe': classe, 'classeS': classeS})


def allCourses(request):
    id = request.GET.get('idUs')
    user = Users.objects.get(id=id)
    classe = classSubject.objects.filter(userId=user)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/allCourses.html', {'classe': classe, 'user': user, 'classeS': classeS})


def addCourse(request):
    if request.method == 'POST':
        id = request.POST.get('idus')
        titleClass = request.POST.get('titleC')
        levelClass = request.POST.get('levelC')
        codeClass = request.POST.get('codeC')
        dateOfCreation = datetime.datetime.now().strftime('%Y-%m-%d')
        user = Users.objects.get(id=id)
        c = classSubject(titleClass=titleClass, level=levelClass,
                         codeClasse=codeClass, creationDateClasse=dateOfCreation, userId=user)
        c.save()
        classe = classSubject.objects.filter(userId=user)
        classeS = classSubject.objects.filter(userId=user)
        return render(request, 'Teacher/allCourses.html', {'classe': classe, 'user': user, 'classeS': classeS})


def addCourseSubject(request):
    idu = request.GET.get('uId')
    user = Users.objects.get(id=idu)
    classeS = classSubject.objects.filter(userId=user)
    return render(request, 'Teacher/formAddCourse.html', {'user': user, 'classeS': classeS})


def updatingData(request):
    if request.method == 'POST':
        id = request.POST.get('idUser')
        nom = request.POST.get('LN')
        prenom = request.POST.get('FN')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        role = request.POST.get('role')
        u = Users.objects.get(id=id)
        oldPic = u.picture.name

        # print(oldPic.replace('profile_pics/',''))
        if bool(request.FILES.get('fileImgUpdate', False)) == True:
            picture = request.FILES.get('fileImgUpdate')
            user = Users(id=id, nom=nom, prenom=prenom, email=email,
                         password=password, picture=picture, role=role)
            user.save()
            classeS = classSubject.objects.filter(userId=user)
            return render(request, 'Teacher/teacherProfile.html', {'user': user, 'classeS': classeS})
        else:
            picture = oldPic
            user = Users(id=id, nom=nom, prenom=prenom, email=email,
                         password=password, picture=picture, role=role)
            user.save()
            classeS = classSubject.objects.filter(userId=user)
            return render(request, 'Teacher/teacherProfile.html', {'user': user, 'classeS': classeS})
    else:
        return render(request, 'teacherProfile.html')


def displayData(request):
    emailT = request.GET.get('userE')
    row = Users.objects.get(email=emailT)
    classeS = classSubject.objects.filter(userId=row)
    return render(request, 'Teacher/formUpdateData.html', {'user': row, 'classeS': classeS})


def profileT(request):
    emailT = request.GET.get('userE')
    dataTeacher = Users.objects.get(email=emailT)
    classeS = classSubject.objects.filter(userId=dataTeacher)
    return render(request, 'Teacher/teacherProfile.html', {'user': dataTeacher, 'classeS': classeS})
