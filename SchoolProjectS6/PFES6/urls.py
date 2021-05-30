from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('teacher', views.teacher_index, name="teacher"),
    path('student', views.student_index, name='student'),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name='logout'),

]
