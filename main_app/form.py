from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Note, Symptom


class NoteForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))

    # assessment = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 100%;'}))

    # notes = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%;',}))

    class Meta:
        model = Note
        fields = [ "title", "assessment", "notes"]
        widgets = {
            "assessment": Select2MultipleWidget(
                attrs={
                    "id": "mySelect2",
                    "data-close-on-select": "false", 
                    'style': 'width: 100%;' 
                }
            
            ),
            "notes": forms.Textarea(
                attrs={
                    'style': "width:100%;"
                }
            ),
            "title": forms.TextInput(
                attrs={
                    'style': "width:100%;"
                }
            ),
        }


from django import forms
