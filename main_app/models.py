from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Symptom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('symptom-detail', kwargs={'pk': self.id})
    
# class Feeling(models.Model):
#     emotion = models.CharField()
    

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    assessment = models.ManyToManyField(Symptom)
    notes = models.TextField(max_length=500)

    def __str__(self):
        # return self.date.strftime("%b %d")
        return self.title
    
    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'note_id': self.id})
    
    def save (self, *args, **kwargs):
        if not self.updated:
            self.updated= timezone.now()
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["-date"]
    
