"""
URL configuration for StudentRecordManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from StudentRecord.views import *
# from StudentRecord.views import index,records
# from StudentRecord.views import records


urlpatterns = [
    path('abc/', admin.site.urls),
    path('', index, name='home'),
    path('record',records, name='records'),
    path('admin',admin_page, name='admin_page'),
    path('student-login',studentLogin, name='studentLogin'),
    path('faculty-login',facultylogin, name='facultylogin'),

    path('dashboard',dashboard, name='dashboard'),
    path('faculty_InnerPage',facultyInnerPage, name='facultyInnerPage'),
]
