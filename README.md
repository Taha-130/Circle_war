# Circle war

Ce projet est un jeu en Python où deux joueurs s'affrontent pour occuper la plus grande aire en plaçant des cercles dans une fenêtre graphique.

## Installation

### Prérequis

- Python 3.8 ou plus récent.
- Les bibliothèques nécessaires pour exécuter le projet.

### Étapes d'installation

1. Clonez ce dépôt ou téléchargez les fichiers.
2. Installez les bibliothèques nécessaires avec la commande suivante :

   ```bash
   pip install -r requirements.txt
   ```

### Créer un environnement virtuel (optionnel)

Pour éviter les conflits entre bibliothèques, il est recommandé d'utiliser un environnement virtuel :

#### Créer un environnement virtuel

```bash
python -m venv env
```

#### Activer l'environnement virtuel

- Sous Windows :

```bash
env\Scripts\activate
```

- Sous macOS/Linux :

```bash
source env/bin/activate
```

#### Installer les dépendances

```bash
pip install -r requirements.txt
```

## Exécution du projet

Pour lancer le jeu, exécutez le fichier principal :

```bash
python main.py
```

## Fonctionnalités

- Deux joueurs prennent des tours pour placer des cercles sur une zone.
- Calcul des aires d'intersection pour déterminer le gagnant.
- Interface graphique simple via la bibliothèque upemtk.

## Structure du Projet

- `circle_war.py` : Contient le code principal du jeu.
- `requirements.txt` : Liste des dépendances nécessaires.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des suggestions ou des pull requests.

## License

Ce projet est sous licence MIT.
