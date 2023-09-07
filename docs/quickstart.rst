Guide de démarrage rapide
=========================

Voici les étapes minimales nécessaires pour démarrer l'application selon l'usage déterminé.

**Lancer l'application hébergée** :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    * L'application est hébergée sur le domaine suivant:

https://lettings-app-6566faf2057b.herokuapp.com/

**Lancer l'application localement depuis une image Docker**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      **Prérequis**
      
      - *Docker* : Assurez-vous que Docker est installé sur votre machine. 
  
      Si ce n'est pas le cas, consultez la documentation officielle de Docker pour votre système d'exploitation : 
      https://docs.docker.com/get-docker/
    
      **Ouvrez une invite de commande puis chargez et lancez l'image**
      - ``docker run --pull always -p 8000:8000 kcardon/ocr-lettings-app:latest``
      Visitez `http://localhost:8000` dans un navigateur.


