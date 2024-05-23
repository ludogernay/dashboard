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

print(html_end)
