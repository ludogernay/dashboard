# Serveur de Visualisation des Ventes de Jeux Vidéo

## Présentation

Ce projet met en place un serveur local pour gérer les requêtes HTTP et générer des visualisations pour les données de ventes de jeux vidéo. Le serveur est construit en utilisant le module `http.server` de Python et utilise CGI pour gérer diverses opérations telles que l'affichage de graphiques, l'ajout, la mise à jour et la suppression de données de jeux.

## Fonctionnalités

- **Serveur de Contenu Statique** : Sert des fichiers HTML et images statiques pour les visualisations.
- **Scripts CGI** : Gère divers scripts CGI pour les opérations sur les données.
- **Génération de Graphiques** : Génère des graphiques à partir des données de ventes de jeux vidéo avant de démarrer le serveur.

## Routes 
    / : Redirige vers la page principale gérée par index.py.
    /graphs : Sert la page HTML statique avec les graphiques (index.html).
    /create : Gère la création de nouvelles données de jeu (createGame.py).
    /update : Gère la mise à jour des données de jeu existantes (update_game.py).
    /game : Affiche les détails individuels du jeu (game_page.py).
    /add : Gère l'ajout de nouvelles données de jeu (addingGame.py).
    /delete : Gère la suppression de données de jeu (delete_game.py).
    /static/ : Sert les fichiers statiques (CSS, JS, images).

## Fichiers et Répertoires

    server.py : Script principal du serveur.
    graphs.py : Script pour générer et sauvegarder les graphiques à partir des données de ventes de jeux vidéo.
    cgi-bin/ : Répertoire contenant les scripts CGI pour gérer diverses opérations.
    static/ : Répertoire pour les fichiers statiques incluant les graphiques générés et les fichiers HTML.