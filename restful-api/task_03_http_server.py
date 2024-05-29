#!/usr/bin/python3

"""Create a simple HTTP server that listens on port 8000 and returns a JSON response."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging

logging.basicConfig(level=logging.INFO)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"GET request received for {self.path}")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": "Hello, World!"}
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        logging.info(f"POST request received for {self.path}")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f"POST data: {post_data.decode()}")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": "Received POST request"}
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        return
    