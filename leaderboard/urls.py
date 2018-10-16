from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    # leaderboard/
    path('', views.index, name='index'),

    # leaderboard/addmatch

    path('delete', views.delete, name='delete'),

]
