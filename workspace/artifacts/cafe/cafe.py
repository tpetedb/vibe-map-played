import http.client
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


class Cafe(BaseHTTPRequestHandler):
    def do_GET(self):
        code = 200 if self.path == "/coffee" else 404
        self.send_response(code)
        self.end_headers()
        self.wfile.write(b"one coffee" if code == 200 else b"not on the menu")

    def log_message(self, fmt, *args):
        pass


httpd = HTTPServer(("127.0.0.1", 0), Cafe)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
port = httpd.server_address[1]
for path in ("/coffee", "/unicorn-milk"):
    con = http.client.HTTPConnection("127.0.0.1", port)
    con.request("GET", path)
    print(f"GET {path} -> {con.getresponse().status}")
    con.close()
httpd.shutdown()
