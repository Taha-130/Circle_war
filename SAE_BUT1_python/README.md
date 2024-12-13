Projet Python : Jeu de Cercle

Ce projet est un jeu en Python permettant à deux joueurs de s'affronter pour contrôler des zones avec des cercles colorés. Les joueurs peuvent placer des cercles, réduire les cercles adverses, et le score final est calculé en fonction des zones occupées.

Prérequis

Pour exécuter ce projet, assurez-vous d'avoir installé les outils et dépendances suivantes :

Python 3.8 ou version ultérieure

Les bibliothèques Python listées dans le fichier requirements.txt

Installation

Clonez ce dépôt ou téléchargez les fichiers sources.

git clone <url-du-depot>
cd <nom-du-repertoire>

Créez un environnement virtuel (optionnel mais recommandé) :

python -m venv env
source env/bin/activate # Sur Windows : .\env\Scripts\activate

Installez les dépendances nécessaires :

pip install -r requirements.txt

Exécution du Projet

Pour lancer le jeu, exécutez le fichier principal :

python <nom-du-fichier-principal>.py

Fonctionnement

Chaque joueur joue à tour de rôle.

Les cercles sont placés ou réduits en cliquant sur l'écran.

Le jeu se termine après 11 tours, et le joueur ayant occupé le plus d'espace gagne.

Fichiers Importants

<nom-du-fichier-principal>.py : Contient le code source principal du jeu.

requirements.txt : Liste des dépendances du projet.

Génération du Fichier requirements.txt

Si vous modifiez ou ajoutez des bibliothèques au projet, vous pouvez regénérer le fichier requirements.txt avec la commande suivante :

pipreqs . --force

Cela mettra à jour le fichier requirements.txt avec les dépendances actuelles du projet.

Contributeurs

Auteur : [Taha Thierry SEFOUDINE]

Licence

Ce projet est sous licence [Indiquez la licence ici, par exemple MIT, GPL, etc.].
