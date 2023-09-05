## Résumé


Site web d'Orange County Lettings, start-up dans le secteur de la location de biens immobiliers. 
L'application est destinée à la gestion des prospects et des biens immobiliers en location.

https://lettings-app-6566faf2057b.herokuapp.com/

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/kcardon/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Récapitulatif du processus de déploiement

Le processus de déploiement de l'application s'appuie sur une approche CI/CD, qui comprend les étapes suivantes :

1. **Compilation et Tests** : 
   * A chaque push sur le repository GitHub, l'image docker est créée, à partir de laquelle les tests sont exécutés et le code est compilé.
   * La suite du déploiement n'est planifié qu'en cas de réussite des étapes de test.

2. **Déploiement** :
   * Si la conteneurisation est réussie, l'image est mise à jour sur le DockerHub ainsi que sur Heroku.
   * Seules les modifications de la branche master déclenchent le déploiement. Les autres branches sont uniquement testées.

### Prérequis

Ces pré-requis complètent ceux indiqués dans le chapitre "Développement local".
Disposer d'un accès aux applicatifs suivants:

* **GitHub** (https://github.com/): assure la gestion de version du code source à travers des dépôts Git. Il offre des fonctionnalités de collaboration telles que le suivi des problèmes, la revue de code et la gestion de projets.
https://github.com/kcardon/Python-OC-Lettings-FR.git

* **Sentry** (https://sentry.io/): plateforme de surveillance des erreurs qui donne une visibilité en temps réel sur les crashs et problèmes de performance.
https://cardon.sentry.io/projects/python-django/?project=4505680878043136
  
* **CircleCI**: système d'intégration continue et de livraison continue (CI/CD) qui permet d'automatiser le processus de build, de test, et de déploiement des applications à chaque changement apporté à la branche master du code source.
https://app.circleci.com/pipelines/github/kcardon/Python-OC-Lettings-FR

* **Docker Desktop**: permet de construire, partager et exécuter des applications dans des conteneurs. Il s'intègre directement à DockerHub.

* **DockerHub** (https://hub.docker.com/): service de cloud qui permet de stocker et de partager l'image de conteneur Docker. 
https://hub.docker.com/repository/docker/kcardon/ocr-lettings-app/

* **Heroku** (https://www.heroku.com/): solution d'hébergement web.
Le site web en production peut être consulté à l'adresse suivante: https://lettings-app-6566faf2057b.herokuapp.com/
  


### Étapes de déploiement

1. Suivez les étapes du chapitre précédent liées au développement local. Assurez-vous d'avoir configuré l'application pour la production.

2. Pousser la branche master mise à jour (ou effectuer un merge d'une branche séparée vers la branche master) lancera la pipeline CI/CD de CircleCi.

3. Connectez-vous sur CircleCi afin de suivre le bon déroulement de la Pipeline (build, tests, conteneurisation, déploiement) et d'être en mesure de consulter les logs d'erreurs le cas échéant.

4. Connectez-vous sur DockerHub afin de vous assurer de la bonne mise à jour de l'image Docker lors du déploiement.

5. Connectez-vous sur Heroku afin de contrôler le déploiement effectif de l'image Docker sur l'hébergeur.
