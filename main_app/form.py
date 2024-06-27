from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Note, User


class NoteForm(forms.ModelForm):
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


# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username", "password"]
#         widgets = {
#             "username": forms.TextInput(
#                 attrs={
#                     'style': "width:100%;"
#                 }
#             ),
#             "password": forms.TextInput(
#                 attrs={
#                     'style': "width:100%;"
#                 }
#             ),
#         }
