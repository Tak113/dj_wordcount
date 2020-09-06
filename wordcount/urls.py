"""wordcount URL Configuration

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
# from django.contrib import admin #for authentication
from django.urls import path
from . import views


#page control
urlpatterns = [
    # path('admin/', admin.site.urls), #for authentication
    path('', views.home, name="home"), #'' means just mainpage
    path('countthewords/', views.count, name='count'), #the name 'count' is refered to action in form in html
    path('about/', views.about, name='about') #about page
]
