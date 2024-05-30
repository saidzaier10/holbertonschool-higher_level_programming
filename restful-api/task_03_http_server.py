#!/usr/bin/python3

import http.server
import json


class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Handle GET requests
        if self.path == '/':
            # Respond to root path with a simple text message
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # Respond to /data path with JSON data
            data = {'name': 'John', 'age': 30, 'city': 'New York'}
            json_data = json.dumps(data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data)
        elif self.path == '/status':
            # Respond to /status path with a simple message
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            # Handle undefined endpoints with a 404 error
            self.send_error(404, 'Endpoint not found')


def run(server_class=http.server.HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
