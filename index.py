import cgi
import data_processing as dp
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


df = dp.read_csv_files("videogames.csv")


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
        .filters {
            width: 20%;
            padding: 1rem;
            margin : 1%;
            background-color: #222;
            border-radius: 7px;
            border: solid 2px white;
        }
         .filter-group {
            margin-bottom: 1rem;
            padding: 0.5rem;
        }
        .filter-group label {
            display: block;
            margin-bottom: 0.5rem;
        }
        .filter-group input, .filter-group select {
            width: 100%;
            padding: 0.5rem;
            border-radius: 5px;
            border: solid 1px #ddd;
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
            border: solid 2px;
            border-color: white;
            border-radius: 7px;
            gap: 0.5rem;
        }
        .game {
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
    <div class="filters">
            <h2>Filter Games</h2>
            <div class="filter-group">
                <label for="genre">Genre:</label>
                <select id="genre">
                    <option value="all">All</option>
                    <option value="Action">Action</option>
                    <option value="Action-adventure">Action-adventure</option>
                    <option value="RPG">RPG</option>
                    <option value="shooter">Shooter</option>
                    <option value="roguelike">Roguelike</option>
                    <option value="Sandbox">Sandbox</option>
                    <option value="Social simulation">Social simulation</option>
                    <option value="Survival">Survival</option>
                    <option value="Sports">Sports</option>
                    <option value="Metroidvania">Metroidvania</option>
                    <option value="Platformer">Platformer</option>
                </select>
            </div>
            <div class="filter-group">
                <label for="platform">Platform:</label>
                <select id="platform">
                    <option value="all">All</option>
                    <option value="Consoles">Consoles</option>
                    <option value="PC">PC</option>
                    <option value="XBOX">Xbox</option>
                    <option value="playstation">PlayStation</option>
                    <option value="Nintendo Switch">Switch</option>
                    <option value="Mobile">Mobile</option>
                </select>
            </div>
            <div class="filter-group">
                <label for="release-date">Release Year :</label>
                <input type="date" id="year" name="release-date">
            </div>
            <div class="filter-group">
                <label for="date-type">Date:</label>
                <select id="date-type" name="date-type">
                    <option value="min">Minimum</option>
                    <option value="max">Maximum</option>
                    <option value="exact">Exacte</option>
                </select>
            </div>
            <button onclick="applyFilters">Apply Filters</button>
        </div>
    <div class='container'>
"""

print(html)

for i in df['Image'].tolist():
    print(f"<div class='game'><img class='logo' src='{i}' alt='Game Image'></div>")
print("</div>")

html_end = """
</body>
</html>
"""
