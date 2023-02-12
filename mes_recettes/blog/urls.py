from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('recette/<int:idRecette>', views.recette, name="recette"),
    path('categorie/<int:idCategorie>', views.categorie, name='categorie'),
    path('inscription', views.inscription, name='inscription'),
]