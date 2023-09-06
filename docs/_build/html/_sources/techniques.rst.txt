Spécifications techniques
----------

Technologies et langages de programmation employés
~~~~~~~~~~~~~~~~~~
* Python / Django (backend)
* SQLite (base de données)
* Html / CSS (front-end)
* Github (gestion de version)
* Sentry (monitoring)
* Docker (conteneurisation)   
* CircleCi (intégration & livraison continue)
* Heroku (hébergement)
* reStructuredText / sphinx / readthedocs (documentation)

Structure de la base de données et modèles de données
~~~~~~~~~~~~~~~~~~
* Application "lettings" : modèles "Address" et "Letting".
* Application "profiles" : modèle "Profile".

**Panel d'administration** :
Visitez `http://localhost:8000/admin` et connectez-vous avec le nom d'utilisateur et mot de passe admin fournis.

**Linting** :
``cd /path/to/Python-OC-Lettings-FR``
``source venv/bin/activate``
``flake8``

**Tests unitaires** :
L'application intègre une couverture de tests supérieure à 80%.
``cd /path/to/Python-OC-Lettings-FR``
``source venv/bin/activate``
``pytest``

**Note pour les utilisateurs Windows** :
Utilisez PowerShell et remplacez l'activation de l'environnement virtuel par : `.\venv\Scripts\Activate.ps1` 

