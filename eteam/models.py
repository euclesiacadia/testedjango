from django.db import models

# from django.shortcurts import render

# Create your models here.
class Equipa(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    objectos = models.Manager()

class Pessoa(models.Model):
    CARGOS = (('E', 'Estagiário'),('P', 'Programador'),('S', 'Secretário'))
    nome = models.CharField(max_length=255, null=False, blank=False)
    apelido = models.CharField(max_length=255, null=False, blank=False)
    cargo = models.CharField(max_length=1, choices=CARGOS)
    equipa = models.ManyToManyField(Equipa)
    objectos = models.Manager()
'''
class Membros(models.Models):
    membros = models.
'''

