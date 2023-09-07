Spécifications techniques
------------------------------

Technologies et langages de programmation employés
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Python 3.9.12 / Django 3.0 (backend)
* SQLite 3.41.1 (base de données)
* HTML5 / CSS (front-end)
* git 2.37.3 (gestionnaire de version)
* Docker 24.0.2 (conteneurisation)
* Sphinx 6.2.1 / reStructuredText (documentation)

Interfaces de programmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Github (cloud gestionnaire de version)
* Sentry (monitoring)
* Docker (conteneurisation)   
* CircleCi (intégration & livraison continue)
* Heroku (hébergement)
* Readthedocs (documentation)

Structure de la base de données et modèles de données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

