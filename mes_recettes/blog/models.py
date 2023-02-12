from django.db import models

# Create your models here.
class Recette(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True)
    photo = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    date_parution = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie = models.ForeignKey("Categorie", on_delete=models.PROTECT, null=True, blank=True)
    membre = models.ForeignKey("Membre", on_delete=models.PROTECT, related_name="recettes", null=True, blank=True)

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Ingredient(models.Model):
    nom = models.CharField(max_length=200)
    quantite = models.FloatField()
    unit = models.CharField(max_length=10)
    recette = models.ForeignKey("Recette", on_delete=models.PROTECT)

    def __str__(self):
        return self.nom

class Membre(models.Model):
    pseudo = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    # prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mdp = models.CharField(max_length=200)
    date_inscription = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'inscription")

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    contenu = models.TextField(max_length=2000)
    date_publication = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")
    recette = models.ForeignKey("Recette", on_delete=models.CASCADE, related_name="commentaires")
    auteur = models.TextField(max_length=200)
    note = models.IntegerField()
    recette = models.ForeignKey("Recette", on_delete=models.PROTECT)

    def __str__(self):
        return self.contenu