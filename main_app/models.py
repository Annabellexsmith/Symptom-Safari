from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Symptom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('symptom-detail', kwargs={'pk': self.id})

class Note(models.Model):
    user = models.ForeignKey(User,          on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    assessment = models.ManyToManyField(Symptom)
    notes = models.TextField(max_length=500)
    
    def __str__(self):
        return self.date.strftime("%b %d")
    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'note_id': self.id})
    
