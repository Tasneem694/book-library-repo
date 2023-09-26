"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from admn.views import *
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login',login,name='login'),
    path('logout', logout, name='logout'),
    path('signup',register, name='register'),
    path('profile', profile, name='profile'),

    path('users', users, name='users'),
    path('delete_user/<int:ID>', delete_user, name='delete_user'),
    path('update_user/<int:ID>', update_user, name='update_user'),
    path('add_user', add_user, name='add_user'),

    path('students', students, name='students'),
    path('student_details/<int:ID>', details, name='details'),
    path('delete_student/<int:ID>', delete_student, name='delete_student'),
    path('update_student/<int:ID>', update_student, name='update_student'),
    path('std_books', std_books, name='std_books'),
    path('student_borrowed_books', std_borrowd, name='std_borrowd'),
    path('update_borrow/<int:ID>', update_borrow, name='update_borrow'),

    path('view_books', view_books, name='view_books'),
    path('book_details/<int:ID>', book_details, name='book_details'),
    path('delete_book/<int:ID>', delete_book, name='delete_book'),
    path('update_book/<int:ID>', update_book, name='update_book'),
    path('add_book', add_book, name='add_book'),
    path('borrowed_books', borrowed_books, name='borrowed_books'),

]
