#!/usr/bin/env python

import cgi
import pandas as pd
from data_processing import create_csv_line


print("Content-type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

# Récupérer les données du formulaire
id = form.getfirst('id', '')
title = form.getfirst('title', '')
developer = form.getfirst('developer', '')
publisher = form.getfirst('publisher', '')
genre = form.getfirst('genre', '')
platform = form.getfirst('platform', '')
release_date = form.getfirst('release-date', '')
rating = form.getfirst('rating', '')
sales = form.getfirst('sales', '')
esrb_rating = form.getfirst('esrb-rating', '')
image = form.getfirst('image', '')

# Créer un dictionnaire avec les valeurs du formulaire
new_game = {
    'ID': id,
    'Title': title,
    'Developer': developer,
    'Publisher': publisher,
    'Genre': genre,
    'Platform': platform,
    'Release Date': release_date,
    'Rating': rating,
    'Sales': sales,
    'ESRB Rating': esrb_rating,
    'Image': image
}

# Lire le fichier CSV existant
df = pd.read_csv("videogames.csv")

# Exemple d'utilisation de la fonction create_csv_line
df = create_csv_line(df, new_game)
# Enregistrer le fichier CSV mis à jour
df.to_csv("videogames.csv", index=False)

print("<p>Game added successfully!</p>")
print("<a href='index.py'>Return to main page</a>")
