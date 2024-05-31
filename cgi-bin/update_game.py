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
        <style>
        body {{
            background-color: black;
            color: white;
        }}
        h1 {{
            text-align: center;
        }}
        .form-container {{
            display: flex;
            justify-content: center;
            padding: 1rem;
            margin: 0 auto;
            width: 50%;
            background-color: #222;
            border-radius: 7px;
            border: solid 2px white;
        }}
        .form-group {{
            margin-bottom: 1rem;
            padding: 1rem;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 0.5rem;
        }}
        .form-group input, .form-group select {{
            width: 100%;
            padding: 0.5rem;
            border-radius: 5px;
            border: solid 1px #ddd;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #fff;
            background-color: #4CAF50;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
        }}
        .button:hover {{background-color: #3e8e41}}
        .button:active {{
            background-color: #3e8e41;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }}
    </style>
    </head>
    <body>
        <h1>Update Game</h1>
        <div class="form-container">
        <form action="/update" method="post">
        <div class="form-group">
            <input type="hidden" name="id" value="{game_id}">
        </div>
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" value="{game['Title']}" required><br><br>
        </div>
        <div class="form-group">
            <label for="image">Image URL:</label>
            <input type="text" id="image" name="image" value="{game['Image']}" required><br><br>
        </div>
        <div class="form-group">
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
            <input type="submit" class="button" value="Update">
        </form>
    </div>
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
        print("<script>window.location.href = '/';</script>")
