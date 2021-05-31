from django.urls import path

from . import views
app_name = 'PFES6'
urlpatterns = [
    path('', views.index, name='index'),
    path('teacher', views.teacher_index, name="teacher"),
    path('student', views.student_index, name='student'),
    path('student/join_course', views.student_join_course,
         name='student_join_course'),
    path('student/to_do', views.student_to_do, name='student_to_do'),
    path('student/profile', views.student_profile, name='student_profile'),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name='logout'),

]
