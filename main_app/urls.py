from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="about"),
    path("notes/", views.note_index, name="note-index"), 
]
