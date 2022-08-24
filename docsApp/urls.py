from django.urls import path
from . import views

urlpatterns = [
    path("", views.retrieve_files, name="choose_file"),
    path("upload_file/", views.upload_file, name="upload_file"),
    path("delete_file/<int:pk>/", views.delete_file, name="delete_file"),
]
