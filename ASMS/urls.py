from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="indexpage"),
    
    # students
    path('student/', views.student, name="studentpage"),
    path('all_student/', views.all_student, name="all_studentpage"),
    path('add_student/',views.add_student,name="add_student_page"),
    path('student_personal/', views.student_personal, name="student_personal_page"),
    
    # schools
    path('school/', views.school, name="schoolpage"),
    path('all_school/', views.all_school, name="all_schoolpage"),
    path('add_school/', views.add_school, name="add_school_page"),
    path('school_personal/', views.school_personal, name="school_personal_page"),
    
    
    # teachers
    path('teacher/', views.teacher, name="teacherpage"),
    path('all_teacher/', views.all_teacher, name="all_teacherpage"),
    path('add_teacher/', views.add_teacher, name="add_teacher_page"),
    path('teacher_personal/', views.teacher_personal, name="teacher_personal_page"),
    
    # login and register
    path('login/',views.login,name="loginpage"),
    path('register/',views.register,name="registerpage"),
    
    # contact
    path('contact/',views.contact,name="contactpage"),
    
    # 404
    path('404/',views.pagenotfound,name="404page"),
]
