from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Note, Symptom
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def note_index(request):    
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/index.html', {
        'notes': notes, 
    })

@login_required
def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/detail.html', {'note': note})


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['assessment', 'notes', 'title']
    success_url = '/notes/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/notes/'

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'assessment', 'notes' ]

class Home(LoginView):
    template_name = 'home.html'