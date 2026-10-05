from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class UserAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":

            response = {
                "status": "healthy"
            }

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )   

            return
        
        if self.path == "/users/1":

            response = {
                "id": 1,
                "name": "Hariharan K",
                "username": "khari",
                "email": "hari@example1.com",
                "version": "v1"
            }

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )

        else:

            self.send_response(404)
            self.end_headers()


    def do_POST(self):

        if self.path == "/users":

            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            request_data = json.loads(body)

            response = {
                "id": 2,
                "name": request_data["name"],
                "username": request_data["username"],
                "email": request_data["email"],
                "version": "v1"
            }

            self.send_response(201)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )

        else:

            self.send_response(404)
            self.end_headers()


    def do_PUT(self):

        if self.path == "/users/1":

            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            request_data = json.loads(body)

            response = {
                "id": 1,
                "name": request_data["name"],
                "username": request_data["username"],
                "email": request_data["email"],
                "version": "v1"
            }

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )

            return

        self.send_response(404)
        self.end_headers()

    
    def do_PATCH(self):

        if self.path == "/users/1":

            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            request_data = json.loads(body)

            response = {
                "id": 1,
                "email": request_data["email"],
                "version": "v1"
            }

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )

            return

        self.send_response(404)
        self.end_headers()


    def do_DELETE(self):

        if self.path == "/users/1":

            self.send_response(200)
            self.end_headers()

            return

        self.send_response(404)
        self.end_headers()

server = HTTPServer(
    ("0.0.0.0", 8000),
    UserAPIHandler
)

print("API v1 running on port 8000", flush=True)

server.serve_forever()