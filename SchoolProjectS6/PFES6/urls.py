from django.urls import path

from . import views
app_name = 'PFES6'
urlpatterns = [
    path('', views.index, name='index'),
    path('teacher', views.teacher_index, name="teacher"),
    path('student', views.student_index, name='student'),
    path('student/course', views.student_course, name='student_course'),
    path('student/join_course', views.student_join_course,
         name='student_join_course'),
    path('student/to_do', views.student_to_do, name='student_to_do'),
    path('student/profile', views.student_profile, name='student_profile'),
    path('student/edit_picture', views.student_picture, name='student_picture'),
    path('student/put_todo', views.student_put_todo, name='student_put_todo'),
    path('student/edit_profile', views.student_edit_profile,
         name='student_edit_profile'),
    path('student/delete_course', views.destroy,
         name='destroy'),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name='logout'),

]
