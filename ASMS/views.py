from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

# start student views
def student(request):
    return render(request, 'pages/student.html')

def add_student(request):
    return render(request, 'forms/add_student.html')

def all_student(request):
    return render(request, 'pages/all_students.html')

def student_personal(request):
    return render(request, 'personal/student_personal.html')
# end


# teacher
def teacher(request):
    return render(request, 'pages/teacher.html')

def all_teacher(request):
    return render(request, 'pages/all_teachers.html')

def add_teacher(request):
    return render(request, 'forms/add_teacher.html')

def teacher_personal(request):
    return render(request, 'personal/teacher_personal.html')
# end teacher


# school
def school(request):
    return render(request, 'pages/school.html')

def all_school(request):
    return render(request, 'pages/all_schools.html')

def add_school(request):
    return render(request, 'forms/add_school.html')

def school_personal(request):
    return render(request, 'personal/school_personal.html')
# end school

# start login and register
def login(request):
    return render(request,'authenticate/login.html')


def register(request):
    return render(request,'authenticate/register.html')

# contact
def contact(request):
    return render(request,'pages/contact.html')

# 404
def pagenotfound (request):
    return render(request,'pages/404.html')
    





