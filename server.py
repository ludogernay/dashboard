import http.server
import os
import subprocess

PORT = 8888
server_address = ("", PORT)

# Generate graphs before starting the server
subprocess.run(["python", "graphs.py"])

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

print("Server active on port:", PORT)
httpd = http.server.HTTPServer(server_address, CustomHandler)
httpd.serve_forever()
