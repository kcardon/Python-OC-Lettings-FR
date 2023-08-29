# Image de base Python
FROM python:3

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Handling secret key
ARG SECRET_KEY
ENV SECRET_KEY=$DJANGO_SECRET_KEY
RUN echo "SECRET_KEY is: $SECRET_KEY"

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu du répertoire courant (votre application Django) dans le conteneur
COPY . /app

# Installation des dépendances Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exécuter collectstatic
RUN python manage.py collectstatic --noinput

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT