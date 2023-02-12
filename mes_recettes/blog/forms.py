from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class InscriptionForm(forms.Form):
   nom = forms.CharField(label="Nom", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Votre nom', 'class':'inputChamp'}))
   pseudo = forms.CharField(label="Pseudo", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Votre pseudo', 'class':'inputChamp'}))
   email = forms.EmailField(label="Email", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Votre email', 'class':'inputChamp'}))
   mdp = forms.CharField(label="Mot de passe", max_length=200, widget=forms.PasswordInput(attrs={'class':'inputChamp'}))

class CommentaireForm(forms.Form):
   auteur = forms.CharField(label="Auteur", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Votre nom', 'class':'inputChamp'}))
   contenu = forms.CharField(label="Contenu", max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Votre commentaire', 'class':'inputChamp'}))
   note = forms.ChoiceField(label="Note", choices=[(i, i) for i in range(1, 6)])
#    note = forms.ChoiceField(label="Note", choices=[(i, i) for i in range(1, 6)], widget=forms.Select(attrs={'class':'inputChamp'}))