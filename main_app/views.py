from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Note, Symptom
# from .forms import NoteForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def note_index(request):    
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/index.html', {
        'notes': notes, 
    })

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/detail.html', {'note': note})



class NoteCreate(CreateView):
    model = Note
    fields = ['assessment', 'notes']
    success_url = '/notes/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteDelete(DeleteView):
    model = Note
    success_url = '/notes/'

class NoteUpdate(UpdateView):
    model = Note
    fields = ['assessment', 'notes']