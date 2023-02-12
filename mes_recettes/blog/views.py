from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from blog.models import Recette, Categorie, Ingredient, Membre, Commentaire
from blog.forms import InscriptionForm

# Create your views here.
def index(request):

    # recupère la liste des recettes
    recettes = Recette.objects.all()

    # récupère les catégories
    categories = Categorie.objects.all()


    return render(request, 'blog/index.html', {
        'recettes': recettes,
        'categories': categories,
    })

def recette(request, idRecette):

    # récupère la recette suivant son id
    recette = Recette.objects.get(pk=idRecette)

    # récupère les catégories
    categories = Categorie.objects.all()

    # récupère les ingrédients de la recette
    ingredients = recette.ingredient_set.all()

    # récupère les commentaires de la recette
    commentaires = recette.commentaire_set.all()

    return render(request, 'blog/recette.html', {
        'commentaires': commentaires,
        'recette': recette,
        'categories': categories,
        'ingredients': ingredients,
    })

def categorie(request, idCategorie):

    # récupère la catégorie suivant son id
    categorie = Categorie.objects.get(pk=idCategorie)

    # récupère les catégories
    categories = Categorie.objects.all()

    # récupère les recettes de la catégorie
    recettes = categorie.recette_set.all()

    return render(request, 'blog/categorie.html', {
        'categorie': categorie,
        'categories': categories,
        'recettes': recettes,
    })

def inscription(request):

    if request.method == 'POST':
        form = InscriptionForm(request.POST)

        if form.is_valid():
            nom = form.cleaned_data['nom']
            pseudo = form.cleaned_data['pseudo']
            email = form.cleaned_data['email']
            mdp = form.cleaned_data['mdp']

            # créer le membre et l'enregistrer en base de données
            membre = Membre(nom = nom, pseudo = pseudo, email = email, mdp = mdp)
            membre.save()

            # ajoute dans la session l'id du membre
            request.session['membre_id'] = membre.id

            # redirige vers la page d'accueil
            return redirect('index')

    else:
        form = InscriptionForm()

    return render(request, 'blog/inscription.html', {
        'form': form,
    })