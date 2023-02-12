# Generated by Django 4.1.6 on 2023-02-08 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_membre_ingredient_commentaire_recette_membre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ingredients', to='blog.recette'),
        ),
    ]
