from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Giornalisti(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    #contenuto = models.TextField()
    #bozza = models.BooleanField()
    #autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post",default=1)
    #data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome+" "+self.cognome


class Articoli(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    autore = models.ForeignKey(Giornalisti, on_delete=models.CASCADE, related_name="articoli")
    #data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo

   


