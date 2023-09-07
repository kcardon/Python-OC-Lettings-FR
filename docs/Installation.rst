Installation
==============

**Lancer l'application localement après avoir clôné le dépôt github**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      **Prérequis**
      - Compte GitHub avec accès en lecture à ce repository
      - Git CLI
      - SQLite3 CLI
      - Interpréteur Python, version 3.6 ou supérieure

      Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

      **Etapes**

      - *Cloner le repository* :
            ``cd /path/to/put/project/in``
            ``git clone https://github.com/kcardon/Python-OC-Lettings-FR.git``
      - *Créer l'environnement virtuel*:
            ``cd /path/to/Python-OC-Lettings-FR``
            ``python -m venv venv``
            ``apt-get install python3-venv``
      - *Activer l'environnement*:
             ``source venv/bin/activate`` (macOS / Linux)
             ``.\venv\Scripts\Activate.ps1`` (Windows)
      - *Exécuter le site*
            ``cd /path/to/Python-OC-Lettings-FR``
            ``pip install --requirement requirements.txt``
            ``python manage.py runserver``
            Visitez `http://localhost:8000` dans un navigateur.