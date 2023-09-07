Procédure de déploiement
------------------------------

Récapitulatif du processus de déploiement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Le processus de déploiement de l'application s'appuie sur une approche CI/CD, qui comprend les étapes suivantes :

1. **Compilation et Tests**
* A chaque push sur le repository GitHub, l'image docker est créée, à partir de laquelle les tests sont exécutés et le code est compilé.
* La suite du déploiement n'est planifié qu'en cas de réussite des étapes de test.

2. **Déploiement**
* Si la conteneurisation est réussie, l'image est mise à jour sur le DockerHub ainsi que sur Heroku.
* Seules les modifications de la branche master déclenchent le déploiement. Les autres branches sont uniquement testées.

Prérequis
^^^^^^^^^^
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

Commande unique pour extraire l'image docker du dockerhub et lancer l'application sur localhost:
``docker run --pull always -p 8000:8000 kcardon/ocr-lettings-app:latest``

* **Heroku** (https://www.heroku.com/): solution d'hébergement web.
  
Le site web en production peut être consulté à l'adresse suivante:

https://lettings-app-6566faf2057b.herokuapp.com/
  


Étapes de déploiement
^^^^^^^^^^

* Suivez les étapes du chapitre précédent liées au développement local. Assurez-vous d'avoir configuré l'application pour la production.
* Poussez la branche master mise à jour (ou effectuez un merge d'une branche séparée vers la branche master). Cela lancera automatiquement la pipeline CI/CD de CircleCi.
* Connectez-vous sur CircleCi afin de suivre le bon déroulement de la Pipeline (build, tests, conteneurisation, déploiement) et d'être en mesure de consulter les logs d'erreurs le cas échéant.
* Connectez-vous sur DockerHub afin de vous assurer de la bonne mise à jour de l'image Docker lors du déploiement.
* Connectez-vous sur Heroku afin de contrôler le déploiement effectif de l'image Docker sur l'hébergeur.
