from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def records(request):
    return render(request,'records.html')

def admin_page(request):
    return render(request,'admin_page.html')

def studentLogin(request):
    return render(request,'studentLogin.html')

def facultylogin(request):
    return render(request,'facultylogin.html')