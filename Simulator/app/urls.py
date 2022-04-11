"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pages import views
from tweets.views import *

urlpatterns = [
    path('', views.home_view, name ="home"),
    path('home', views.home_view, name ="home"),
    path('about', views.about_view, name ="about"),
    path('participate', participate, name ="posts"),
    path('add_interaction', add_interaction, name ="add_interaction"),
    path('remove_interaction', remove_interaction, name ="remove_interaction"),
    path('add_post_by_user', add_post_by_user, name ="add_post_by_user"),
    path('add_reply', add_reply, name ="add_reply"),
    path('contact', views.contact_view, name ="contact"),
    path('update_session', update_session, name ="update_session"),
    path('submit', submit, name ="submit"),


    path('admin/', admin.site.urls)
]
