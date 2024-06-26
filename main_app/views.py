from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Note
from .form import NoteForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer



# Create your views here.
def about(request):
    return render(request, "about.html")


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("note-index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


@login_required
def note_index(request):
    notes = Note.objects.filter(user=request.user)
    return render(
        request,
        "notes/index.html",
        {
            "notes": notes,
        },
    )


@login_required
def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, "notes/detail.html", {"note": note})


@login_required
def export(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="notes.pdf"'
    pdf = SimpleDocTemplate(response, pagesize=letter)
    style = getSampleStyleSheet()
    journal = []
    notes = Note.objects.filter(user=request.user)
  
    for note in notes:
        notes = Note.objects.filter(user=request.user) 
        note_symptoms = note.assessment.all()
        symptoms_list = ", ".join([symptom.name for symptom in note_symptoms])
        journal.append(Paragraph(f"Title: {note.title}", style["Normal"]))
        journal.append(Spacer(1, 12))
        journal.append(Paragraph(f"Date: {note.date}", style["Normal"]))
        journal.append(Spacer(1, 12))
        journal.append(Paragraph(f"Symptoms Reported: {symptoms_list}", style["Normal"]))
        journal.append(Spacer(1, 12))
        journal.append(Paragraph(f"Notes: {note.notes}", style["Normal"]))
        journal.append(Spacer(1, 24))
    pdf.build(journal)
    return response


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = "/notes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = "/notes/"


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm


class Home(LoginView):
    template_name = "home.html"
