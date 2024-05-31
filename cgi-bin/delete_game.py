import cgi
import cgitb
import pandas as pd
cgitb.enable()

# Lire les données depuis le fichier CSV
df = pd.read_csv('videogames.csv')

# Obtenir l'ID du jeu à partir de la chaîne de requête
form = cgi.FieldStorage()
game_id = form.getvalue('id')

# Supprimer le jeu correspondant dans le DataFrame
df = df[df['ID'] != int(game_id)]

# Écrire les modifications dans le fichier CSV
df.to_csv('videogames.csv', index=False)

# Rediriger vers la page principale
print("Content-type: text/html")
print()
print("<script>window.location.href = '/';</script>")
