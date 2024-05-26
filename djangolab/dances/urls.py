from django.contrib import admin
from django.urls import path

from . import views

app_name = 'dances'

urlpatterns = [
    path("", views.dancer_list),
    path("dances/", views.dance_home),
    path("detail/<int:id>/", views.dancer_detail, name='detail'),
    path("<int:id>/", views.dancer_detail, name='detail'),
    path("create/", views.dancer_create, name='create'),
    path("<int:id>/update/", views.dancer_update, name='update'),
    path("delete/", views.dancer_delete),
    path("createdance/", views.dance_create),
]