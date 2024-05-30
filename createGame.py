import cgi
import data_processing as dp
import pandas as pd

form = cgi.FieldStorage()

# Récupérer les critères de filtrage
genreForm = form.getfirst('genre', '')
platformForm = form.getfirst('platform', '')
release_dateForm = form.getfirst('release-date', '')
date_typeForm = form.getfirst('date-type', '')

print("Content-type: text/html; charset=utf-8\n")

df = dp.read_csv_files("videogames.csv")
genres = dp.select_csv_column(df, "Genre").unique()
platforms = dp.select_csv_column(df, "Platform").unique()

html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Mon programme</title>
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
    <h1>Add New Game</h1>
    <div class="form-container">
        <form action="AddingGame.py" method="post">
            <div class="form-group">
                <label for="title">Title:</label>
                <input type="text" id="title" name="title" required>
            </div>
            <div class="form-group">
                <label for="developer">Developer:</label>
                <input type="text" id="developer" name="developer" required>
            </div>
            <div class="form-group">
                <label for="publisher">Publisher:</label>
                <input type="text" id="publisher" name="publisher" required>
            </div>
            <div class="form-group">
                <label for="genre">Genre:</label>
                <select id="genre" name="genre" required>
                    <option value="">Select Genre</option>"""
for genre in genres:
    html += f'\n<option value="{genre}">{genre}</option>'
html += """
                </select>
            </div>
            <div class="form-group">
                <label for="platform">Platform:</label>
                <select id="platform" name="platform" required>
                    <option value="">Select Platform</option>"""
for platform in platforms:
    html += f'\n<option value="{platform}">{platform}</option>'
html += f"""
                </select>
            </div>
            <div class="form-group">
                <label for="release-date">Release Date:</label>
                <input type="date" id="release-date" name="release-date" required>
            </div>
            <div class="form-group">
                <label for="rating">Rating:</label>
                <input type="text" id="rating" name="rating" required>
            </div>
            <div class="form-group">
                <label for="sales">Sales:</label>
                <input type="text" id="sales" name="sales" required>
            </div>
            <div class="form-group">
                <label for="esrb-rating">ESRB Rating:</label>
                <input type="text" id="esrb-rating" name="esrb-rating" required>
            </div>
            <div class="form-group">
                <label for="image">Image URL:</label>
                <input type="text" id="image" name="image" required>
            </div>
            <button type="submit" class="button">Add Game</button>
        </form>
    </div>
</body>
</html>
"""

print(html)
