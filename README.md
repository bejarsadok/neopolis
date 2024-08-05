# README

## Introduction

Ce projet est une application Django pour la gestion de tâches et de projets. Ce fichier `README.md` fournit des instructions sur la configuration de l'environnement de développement et sur l'exécution de l'application.

## Prérequis

Avant de commencer, assurez-vous que vous avez installé les outils suivants :

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Configuration de l'environnement de développement

1. **Créer un environnement virtuel**

   ```bash
   python -m venv venv

   ```

1. **Activez l'environnement virtuel**
   ```bash
   .\venv\Scripts\activate
   ```
1. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```


## Configuration de base de données

Tous d'abbord, on dois configurer la connexion avec la base de données dans le fichier settings.py

```bash
 "default": {
     "ENGINE": "django.db.backends.postgresql",
     "NAME": "neopolis",
     "USER": "postgres",
     "PASSWORD": "postgres",
     "HOST": "localhost",
     "PORT": "5432",
    }
```

Après la création des models dans le fichier models.py on dois executé cette command pour crée le fichier de migration

1. **création des migrations**

```bash
python manage.py makemigrations
```

1. **Appliquer les migrations**

```bash
python manage.py migrate
```

1. **Lancé le serveur de developpement**

```bash
python manage.py runserver
```
