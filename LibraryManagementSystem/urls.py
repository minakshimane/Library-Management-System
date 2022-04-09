"""LibraryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from LMS import views
urlpatterns = [
    path('admin/', admin.site.urls),
path('',views.index,name="main"),
    path('adminsignup/',views.adminsignup,name="adminsignup"),
    path('saveadmin/',views.saveadmin,name='saveadmin'),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('onadminlogin/',views.onadminlogin,name="onadminlogin"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('addbook/',views.addbook,name="addbook"),
    path('savebook/',views.savebook,name="savebook"),
    path('bookdetail/',views.bookdetail,name="bookdetail"),
    path('Book_update/',views.Book_update,name="Book_update"),
    path('update_book/',views.update_book,name="update_book"),
    path('Book_delete/', views.Book_delete, name="Book_delete"),
    path('logout/', views.logout, name="logout"),
    path('Book_del/',views.Book_del,name="Book_del"),
    path('view_all/',views.view_all,name="view_all"),
]
