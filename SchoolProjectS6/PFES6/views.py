from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userApp
# Create your views here.

'''
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        ps = request.POST['psw']
        user = userApp(email=email, password=ps)
        if user is not None:
            auth.login(request, user)
            if user.role == 'teacher':
                return render(request, 'teachersSpace.html')
            elif user.role == 'student':
                return redirect(request, 'StudentsSpace.html')
        else:
            #messages.info(request,'invalide ..!!')
            return redirect('login')
    else:
        return render(request, 'index.html')
'''