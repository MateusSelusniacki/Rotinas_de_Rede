from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == '/'):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            message = "Hello, World! Here is a GET response"
            self.wfile.write(bytes(message, "utf8"))

        if(self.path == '/example'):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            message = "GET message"
            self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])

        f = open("file.txt","w")
        f.write(str(self.rfile.read(content_length)))

    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
    
    def do_DELETE(self):
        pass
    
    def do_HEAD(self):
        pass

    def do_PATCH(self):
        pass

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()