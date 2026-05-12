from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=64)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_categorie

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    publier = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   # image = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.article}"
