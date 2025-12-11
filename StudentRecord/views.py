from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from connect import connection

# Create your views here.

def index(request):
    return render(request,'index.html')

def records(request):
    return render(request,'records.html')

def admin_page(request):
    if request.method == 'POST':
        studentId = request.POST.get("username")
        password = request.POST.get("password")

        print(studentId)
        print(password)
        
        connect = connection()
        cursor = connect.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)

        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()

        user = authenticate(request, studentId = studentId, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           messages.error(request,"Invalid username or password")
    
    
    return render(request,'admin_page.html')

def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'studentLogin.html')

def facultylogin(request):
    return render(request,'facultylogin.html')

def dashboard(request):
    return render(request,'dashboard.html')

def facultyInnerPage(request):
    return render(request,'facultyInnerPage.html')
