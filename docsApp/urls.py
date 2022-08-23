from django.urls import path
from . import views

urlpatterns = [
    path("", views.choose_file, name="choose_file"),
    path("upload_file/", views.upload_file, name="upload_file")
]
