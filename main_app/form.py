from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Note, Symptom

class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ['assessment', 'notes', 'title']
        widgets = {
            'assessment': Select2MultipleWidget(attrs={'id': 'mySelect2'}),
        }

from django import forms

