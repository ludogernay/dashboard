import cgi
import data_processing as dp

# Récupérer les données du formulaire
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

# Appliquer les filtres
filtered_df = df

if genreForm:
    filtered_df = filtered_df[filtered_df['Genre'] == genreForm]
if platformForm:
    filtered_df = filtered_df[filtered_df['Platform'] == platformForm]
if release_dateForm:
    # Selon le type de date sélectionné, appliquer le filtre approprié
    if date_typeForm == 'min':
        filtered_df = filtered_df[filtered_df['Release Date'] >= release_dateForm]
    elif date_typeForm == 'max':
        filtered_df = filtered_df[filtered_df['Release Date'] <= release_dateForm]
    elif date_typeForm == 'exact':
        filtered_df = filtered_df[filtered_df['Release Date'] == release_dateForm]

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
        .filters {{
            position: fixed;
            z-index: 1;
            transition: left 0.3s ease;
            top: 0;
            left: -15%;
            width: 20%;
            padding: 1rem;
            margin : 1%;
            background-color: #222;
            border-radius: 7px;
            border: solid 2px white;
        }}
        
        .filters h2 {{
            text-align: right;
        }}
        .filters:hover {{
            left: -0.6%;
        }}
         .filter-group {{
            margin-bottom: 1rem;
            padding: 2rem;
        }}
        .filter-group label {{
            display: block;
            margin-bottom: 0.5rem;
        }}
        .filter-group input, .filter-group select {{
            width: 100%;
            padding: 0.5rem;
            border-radius: 5px;
            border: solid 1px #ddd;
        }}
        .container {{
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
        }}
        .game {{
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #333;
            color: white;
            padding: 1rem;
            border-radius: 7px;
            border: solid 2px;
            border-color: white;
            width: 16%;
            min-width: 250px;
            height: auto;
            text-align: center;
        }}
        .logo {{
            width: 100%;
            height: 400px;
            border-radius: 7px;
            border: solid 1px white;
        }}
        .button_logo {{
            display: flex;
            align-items: center;
            justify-content: space-around;
            width: 100%;
        }}
        .update_button {{
            filter: invert(1) brightness(2) sepia(20) saturate(50) hue-rotate(-50deg);
            width: 48px;
            height: 48px;
            cursor: pointer;
        }}
        .delete_button {{
            filter: invert(24%) sepia(95%) saturate(7484%) hue-rotate(340deg) brightness(101%) contrast(102%);
            width: 30px;
            height: 30px;
            cursor: pointer;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            margin: 1rem;
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
    <h1>Gaming Tracker</h1>
    <div class="filters">
        <h2>Filter Games</h2>
        <form action="/" method="post">
            <div class="filter-group">
                <label for="genre">Genre:</label>
                <select id="genre" name="genre">
                    <option value="">All</option>"""
for genre in genres:
    html += f'\n<option value="{genre}" {"selected" if genre == genreForm else ""}>{genre}</option>'
html += """
                </select>
            </div>
            <div class="filter-group">
                <label for="platform">Platform:</label>
                <select id="platform" name="platform">
                    <option value="">All</option>"""
for platform in platforms:
    html += f'\n<option value="{platform}" {"selected" if platform == platformForm else ""}>{platform}</option>'
html += f"""
                </select>
            </div>
            <div class="filter-group">
                <label for="release-date">Release Year :</label>
                <input type="date" id="year" name="release-date" value="{release_dateForm}">
            </div>
            <div class="filter-group">
                <label for="date-type">Date:</label>
                <select id="date-type" name="date-type">
                    <option value="">All</option>
                    <option value="min" {"selected" if date_typeForm == 'min' else ""}>Minimum</option>
                    <option value="max" {"selected" if date_typeForm == 'max' else ""}>Maximum</option>
                    <option value="exact" {"selected" if date_typeForm == 'exact' else ""}>Exacte</option>
                </select>
            </div>
            <button type="submit" class="button">Apply Filters </button>
        </form>
         <a href="/create" class="button"> (+) Add Game </a>
         <a href="/graphs" class="button"> Graphs </a>
    </div>
    <div class='container'>"""
for i,row in filtered_df.iterrows():
    game_id = row['ID']
    image_url = row['Image']
    html += f"""
        <div class='game'>
            <div class='button_logo'>
                <a href='update?id={game_id}'><img class='update_button' src='/static/logos/update.png' alt='update'></a>
                <a href='delete?id={game_id}'><img class='delete_button' src='/static/logos/delete.png' alt='delete'></a>
            </div>
            <a href='game?id={game_id}'><img class='logo' src='{image_url}' alt='Game Image'></a>
        </div>
        """


html_end = """
    </div>
</body>
</html>
"""

print(html)
