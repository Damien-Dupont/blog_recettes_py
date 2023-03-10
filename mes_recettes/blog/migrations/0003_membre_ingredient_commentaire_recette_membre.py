# Generated by Django 4.1.6 on 2023-02-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categorie_recette_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mot_de_passe', models.CharField(max_length=200)),
                ('date_inscription', models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('quantite', models.FloatField()),
                ('unit', models.CharField(max_length=10)),
                ('recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='blog.recette')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField(max_length=2000)),
                ('date_publication', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('auteur', models.TextField(max_length=200)),
                ('note', models.IntegerField()),
                ('recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='blog.recette')),
            ],
        ),
        migrations.AddField(
            model_name='recette',
            name='membre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='recettes', to='blog.membre'),
        ),
    ]
