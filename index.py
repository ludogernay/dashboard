import cgi
import data_processing as dp

# Récupérer les données du formulaire
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
        filtered_df = filtered_df[filtered_df['Release Year'] >= release_dateForm]
    elif date_typeForm == 'max':
        filtered_df = filtered_df[filtered_df['Release Year'] <= release_dateForm]
    elif date_typeForm == 'exact':
        filtered_df = filtered_df[filtered_df['Release Year'] == release_dateForm]

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
            transition: left 0.3s ease;
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
            left: -0.7%;
        }}
         .filter-group {{
            margin-bottom: 1rem;
            padding: 0.5rem;
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
            border: solid 2px;
            border-color: white;
            border-radius: 7px;
            gap: 0.5rem;
        }}
        .game {{
            background-color: #333;
            color: white;
            padding: 1rem;
            border-radius: 7px;
            border: solid 2px;
            border-color: white;
            width: 16%;
            text-align: center;
        }}
        .logo {{
            width: 100%;
            height: auto;
            border-radius: 7px;
        }}
    </style>
</head>
<body>
    <h1>Gaming Tracker</h1>
    <div class="filters">
        <h2>Filter Games</h2>
        <form action="index.py" method="post">
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
            <button type="submit">Apply Filters</button>
        </form>
    </div>
    <div class='container'>"""

for i in filtered_df['Image'].tolist():
    html += f"<div class='game'><img class='logo' src='{i}' alt='Game Image'></div>"
html += """
    </div>
</body>
</html>
"""

print(html)
