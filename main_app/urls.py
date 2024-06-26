from django.urls import path, include
from . import views

urlpatterns = [
    path("select2/", include("django_select2.urls")),
    path("", views.Home.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("notes/", views.note_index, name="note-index"),
    path("notes/<int:note_id>/", views.note_detail, name="note-detail"),
    path("notes/create/", views.NoteCreate.as_view(), name="note-create"),
    path("notes/<int:pk>/update/", views.NoteUpdate.as_view(), name="note-update"),
    path("notes/<int:pk>/delete/", views.NoteDelete.as_view(), name="note-delete"),
    path("accounts/signup/", views.signup, name="signup"),
    path("export/", views.export, name="export"),
]
