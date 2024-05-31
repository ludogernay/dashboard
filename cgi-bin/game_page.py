#!/usr/bin/env python3

import cgi
import pandas as pd

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

# Read the CSV file
df = pd.read_csv("videogames.csv")

# Get the game ID from the URL
game_id = form.getvalue("id")
print(game_id)
# Find the game corresponding to the ID in the dataframe
if game_id and game_id.isdigit():
    game = df[df['ID'] == int(game_id)].iloc[0]
    # Build the HTML to display game details
    html = f"""<!DOCTYPE html>
    <html>
    <head>
        <title>{game['Title']}</title>
        <style>
            body {{
                background-color: black;
                color: white;
                font-family: Arial, sans-serif;
            }}
            img {{
                width: 300px;
                height: auto;
            }}
            .container {{
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                border: solid 2px white;
                border-radius: 7px;
                background-color: #333;
            }}
            .game-title {{
                font-size: 2em;
                text-align: center;
                padding-bottom: 20px;
            }}
            .game-details {{
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .game-details img {{
                max-width: 100%;
                height: auto;
                border-radius: 7px;
            }}
            .game-info {{
                margin-top: 20px;
            }}
            .link {{
                text-decoration: none;
                color: white;
            }}
            .back {{
                border: solid 2px white;
                width: fit-content;
                padding: 5px 10px;
                border-radius: 7px;    
            }}
        </style>
    </head>
    <body>
        <div class='container'>
            <div class='back'><a class='link' href='/'>Retour</a></div>
            <div class='game-title'>{game['Title']}</div>
            <div class='game-details'>
                <img src='{game['Image']}' alt='{game['Title']}'>
                <div class='game-info'>
                    <p><strong>Developer:</strong> {game['Developer']}</p>
                    <p><strong>Publisher:</strong> {game['Publisher']}</p>
                    <p><strong>Genre:</strong> {game['Genre']}</p>
                    <p><strong>Platform:</strong> {game['Platform']}</p>
                    <p><strong>Release Date:</strong> {game['Release Date']}</p>
                    <p><strong>Rating:</strong> {game['Rating']}</p>
                    <p><strong>Sales:</strong> {game['Sales']}</p>
                    <p><strong>ESRB Rating:</strong> {game['ESRB Rating']}</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    print(html)
else:
    print("<html><body><h1>Game not found</h1></body></html>")
