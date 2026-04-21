from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 80

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from Akash Francis - Project DevOps +  CI/CD ")

with HTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
