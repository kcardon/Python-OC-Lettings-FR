# Image de base Python
FROM python:3

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu du répertoire courant (votre application Django) dans le conteneur
COPY . /app

# Installation des dépendances Python
RUN pip install --upgrade pip && pip install -r Python-OC-Lettings-FR/requirements.txt
CMD ["python", "Python-OC-Lettings-FR/manage.py", "runserver", "0.0.0.0:8000"]