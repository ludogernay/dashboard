import http.server
import os
import subprocess
import urllib.parse

PORT = 8888
server_address = ("", PORT)

# Generate graphs before starting the server
subprocess.run(["python", "graphs.py"])

class CustomHandler(http.server.CGIHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        parsed_path = urllib.parse.urlparse(self.path)
        self.path = parsed_path.path

        if self.path == '/':
            self.path = '/cgi-bin/index.py'
        elif self.path == '/graphs':
            self.path = '/static/index.html'
        elif self.path == '/create':
            self.path = '/cgi-bin/createGame.py'
        elif self.path == '/update':
            self.path = '/cgi-bin/update_game.py'
        elif self.path == '/game':
            self.path = '/cgi-bin/game_page.py'
        elif self.path == '/add':
            self.path = '/cgi-bin/addingGame.py'
        elif self.path == '/delete':
            self.path = '/cgi-bin/delete_game.py'
        elif self.path.startswith('/static/'):
            self.path = self.path
        else:
            self.path = '/static' + self.path

        # Append query parameters to the path
        self.path += '?' + parsed_path.query

        if self.path.endswith('.py'):
            self.cgi_info = '', self.path[1:]  # Set cgi_info for CGI scripts
            return http.server.CGIHTTPRequestHandler.run_cgi(self)
        else:
            return http.server.CGIHTTPRequestHandler.do_GET(self)

    def is_cgi(self):
        base_path = os.path.dirname(self.path)
        if base_path in self.cgi_directories:
            script_name = os.path.basename(self.path)
            self.cgi_info = base_path, script_name
            return True
        return False

# Setting the CGI directories
CustomHandler.cgi_directories = ["/cgi-bin"]

print("Server active on port:", PORT)
httpd = http.server.HTTPServer(server_address, CustomHandler)
httpd.serve_forever()
