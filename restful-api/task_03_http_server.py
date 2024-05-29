#!/usr/bin/python3
"""Add all arguments to a Python list and save to a file."""

import http.server
import socketserver
import json

PORT = 8000


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests.

        This method is called when a GET request is received by the server.
        It checks the requested path and sends the appropriate response.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/posts':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            posts = [
                {"id": 1, "title": "Post 1", "body": "This is the first post."},
                {"id": 2, "title": "Post 2", "body": "This is the second post."},
                {"id": 3, "title": "Post 3", "body": "This is the third post."}
            ]
            self.wfile.write(json.dumps(posts).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
