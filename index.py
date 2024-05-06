import cgi
import data_processing as dp
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

df = dp.read_csv_files("videogames.csv")
filtered_df = dp.select_between_csv_line(df, "Sales", 20000000,40000000)

html = """<!DOCTYPE html>
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
        .game {
            background-color: #333;
            color: white;
            padding: 1rem;
            border-radius: 7px;
            border: solid 2px;
            border-color: white;
            width: 30%;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Gaming Tracker</h1>
</body>
</html>
"""
print(html)
print("<div class='container'>")
for i in filtered_df['Title'].tolist():
    print(f"<div class=\"game\">{i}</div>")
print("</div>")