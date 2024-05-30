import cgi
import cgitb
import pandas as pd
import data_processing as dp
cgitb.enable()

# Lire les données depuis le fichier CSV
df = pd.read_csv('videogames.csv')

# Obtenir l'ID du jeu à partir de la chaîne de requête
form = cgi.FieldStorage()
game_id = form.getvalue('id')

# Trouver le jeu correspondant dans le DataFrame
game = df.loc[df['ID'] == int(game_id)]
platforms = dp.select_csv_column(df, "Platform").unique()

# Si le jeu n'existe pas, gérer l'erreur
if game.empty:
    print("Content-Type: text/html")
    print()
    print("<h1>Jeu non trouvé</h1>")
else:
    game = game.iloc[0]  # Extraire la première ligne comme série

    # Générer le formulaire HTML
    print("Content-Type: text/html")
    print()
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Update Game</title>
    </head>
    <body>
        <h1>Update Game</h1>
        <form action="update_game.py" method="post">
            <input type="hidden" name="id" value="{game_id}">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" value="{game['Title']}" required><br><br>
            <label for="image">Image URL:</label>
            <input type="text" id="image" name="image" value="{game['Image']}" required><br><br>
            <label for="platform">Platform:</label>
            <select id="platform" name="platform" required>
                <option value="{game['Platform']}" selected>{game['Platform']}</option>
    """
    for platform in platforms:
        if platform != game['Platform']:
            html += f'\n                <option value="{platform}">{platform}</option>'
    html += f"""
            </select><br><br>
            <label for="rating">Rating: (1-100)</label>
            <input type="text" id="rating" name="rating" value="{game['Rating']}" required><br><br>
            <label for="sales">Sales:</label>
            <input type="text" id="sales" name="sales" value="{game['Sales']}" required><br><br>
            <input type="submit" value="Update">
        </form>
    </body>
    </html>
    """
    print(html)

    # Traitement de la soumission du formulaire
    if form.getvalue('name'):
        name = form.getvalue('name')
        image = form.getvalue('image')
        platform = form.getvalue('platform')
        rating = form.getvalue('rating')
        sales = form.getvalue('sales')

        # Mettre à jour les détails du jeu dans le DataFrame
        df.loc[df['ID'] == int(game_id), ['Title', 'Image', 'Platform', 'Rating', 'Sales']] = [name, image, platform, rating, sales]

        # Écrire les modifications dans le fichier CSV
        df.to_csv('videogames.csv', index=False)

        # Rediriger vers la page principale ou une page de confirmation
        print("<script>window.location.href = 'index.py';</script>")
