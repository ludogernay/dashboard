import cgi
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
print(form.getvalue("name"))
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