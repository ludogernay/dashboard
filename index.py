import cgi
import pandas as pd
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


df = pd.read_csv("videogames.csv")


html = """<!DOCTYPE html>
<html>
<head>
    <title>Mon programme</title>
    <style>
        body {
            background-color: black;
            color: white;
        }
        h1 {
            text-align: center;
        }
        .container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            padding: 1rem;
            margin: 0 auto;
            color: white;
            height: auto;
            min-height: 60vh;
            width: 80%;
            gap: 0.5rem;
        }
        .game {
            display: flex;
            align-items: center;
            background-color: #333;
            color: white;
            padding: 1rem;
            border-radius: 7px;
            border: solid 2px;
            border-color: white;
            width: 16%;
            text-align: center;
        }
        .logo {
            width: 100%;
            height: auto;
            border-radius: 7px;
        }
    </style>
</head>
<body>
    <h1>Gaming Tracker</h1>
    <div class='container'>
"""

print(html)

for index, row in df.iterrows():
    game_id = row['ID']
    image_url = row['Image']
    print(f"<div class='game'><a href='game_page.py?id={game_id}'><img class='logo' src='{image_url}' alt='Game Image'></a></div>")

print("</div>")

html_end = """
</body>
</html>
"""
