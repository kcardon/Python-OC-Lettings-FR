
#. **Cloner le repository** :
      `cd /path/to/put/project/in
      git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#. **Créer l'environnement virtuel**

      - `cd /path/to/Python-OC-Lettings-FR`
      - `python -m venv venv`
      - `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
      - Activer l'environnement:
             `source venv/bin/activate` (macOS / Linux)
             `.\venv\Scripts\Activate.ps1` (Windows)
      - Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
      `which python`
      - Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
      - Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
      - Pour désactiver l'environnement, `deactivate`

#. **Exécuter le site** (macOS / Linux) :
      `cd /path/to/Python-OC-Lettings-FR
      source venv/bin/activate
      pip install --requirement requirements.txt
      python manage.py runserver`
   Visitez `http://localhost:8000` dans un navigateur.

#. **Linting** :
      `cd /path/to/Python-OC-Lettings-FR
      source venv/bin/activate
      flake8`

#. **Tests unitaires** :
   L'application intègre une couverture de tests supérieure à 80%.
   
      `cd /path/to/Python-OC-Lettings-FR
      source venv/bin/activate
      pytest`

#. **Base de données** :
      `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`

- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter


#. **Panel d'administration** :
    Visitez `http://localhost:8000/admin` et connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`.

**Note pour les utilisateurs Windows** :
Utilisez PowerShell et remplacez l'activation de l'environnement virtuel par : `.\venv\Scripts\Activate.ps1` 
Remplacez également `which <my-command>` par `(Get-Command <my-command>).Path`.

