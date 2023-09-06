Guide de démarrage rapide
=========================

Voici les étapes minimales nécessaires pour démarrer l'application selon l'usage déterminé.

**Lancer l'application hébergée** :
~~~~~~~~~~~~~~~~~~
    * L'application est hébergée sur le domaine suivant:
      https://lettings-app-6566faf2057b.herokuapp.com/

**Lancer l'application localement depuis une image Docker**
~~~~~~~~~~~~~~~~~~
      **Prérequis**
      
      - *Docker* : Assurez-vous que Docker est installé sur votre machine. 
      Si ce n'est pas le cas, consultez la documentation officielle de Docker pour votre système d'exploitation : 
      https://docs.docker.com/get-docker/
    
      **Charger et lancer l'image**
      - ``docker run --pull always -p 8000:8000 kcardon/oc-lettings:latest``
      Visitez `http://localhost:8000` dans un navigateur.


**Lancer l'application localement après avoir clôné le dépôt github**
~~~~~~~~~~~~~~~~~~
      **Prérequis**
      - Compte GitHub avec accès en lecture à ce repository
      - Git CLI
      - SQLite3 CLI
      - Interpréteur Python, version 3.6 ou supérieure

      Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

      **Etapes**

      - *Cloner le repository* :
            ``cd /path/to/put/project/in
            git clone https://github.com/kcardon/Python-OC-Lettings-FR.git``
      - *Créer l'environnement virtuel*:
            ``cd /path/to/Python-OC-Lettings-FR
            python -m venv venv
            apt-get install python3-venv``
      - *Activer l'environnement*:
             ``source venv/bin/activate`` (macOS / Linux)
             ``.\venv\Scripts\Activate.ps1`` (Windows)
      - *Exécuter le site*
            ``cd /path/to/Python-OC-Lettings-FR``
            ``pip install --requirement requirements.txt``
            ``python manage.py runserver``
            Visitez `http://localhost:8000` dans un navigateur.