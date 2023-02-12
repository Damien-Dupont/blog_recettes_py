# Generated by Django 4.1.6 on 2023-02-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('photo', models.CharField(max_length=200)),
                ('auteur', models.CharField(max_length=200)),
                ('date_parution', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
            ],
        ),
    ]
