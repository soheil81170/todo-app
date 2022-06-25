"""set URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
from.import views
from crud.views import login 




app_name ="crud"
urlpatterns = [
	path('signup', views.signup ,name = "signup"),
	path('signup/submit', views.submit ,name = "submit"),      
    path('', views.login.as_view() ,),
    path('home',views.useri.as_view(),name = "home"),
    path('home/createtodo',views.createtodo,name = "create"),
    path('logout',views.logout,name="logout"),
    path('home/deletetodo/<int:pk>/',views.deletetodo.as_view(),name = "deletetodo"),
    path('home/updatetodo/<int:pk>/',views.updatetodo.as_view(),name = "updatetodo"),
]	








