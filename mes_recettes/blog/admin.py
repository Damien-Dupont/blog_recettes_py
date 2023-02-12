from django.contrib import admin
from blog.models import Recette, Categorie, Ingredient, Membre, Commentaire
# Register your models here.
admin.site.register(Recette)
admin.site.register(Categorie)
admin.site.register(Ingredient)
admin.site.register(Membre)
admin.site.register(Commentaire)
