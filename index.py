import cgi
import data_processing as dp
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <div>
        <h1>Mon programme</h1>
    </div>
</body>
</html>
"""
print(html)