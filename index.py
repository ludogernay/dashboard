import cgi
import data_processing as dp
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
    <title>DashBoard</title>
</head>
<body>
    <div>
        <h1>DashBoard</h1>
    </div>
</body>
</html>
"""
print(html)
print(dp.select_between_csv_line(dp.read_csv_files("videogames.csv"), "Sales",29000000, 300000000))