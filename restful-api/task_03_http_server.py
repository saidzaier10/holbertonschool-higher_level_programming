#!/usr/bin/python3

import http.server
import json


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def root(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def data(self):
        data = {"name": "John", "age": 30, "city": "New York"}
        json_data = json.dumps(data).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json_data)

    def status(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def info(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"version": "1.0", "description": "A simple API built with http.server"}).encode())

    def do_GET(self):
        path_function_map = {
            "/": self.root,
            "/data": self.data,
            "/status": self.status,
            "/info": self.info,
        }

        func = path_function_map.get(self.path, self.send_error)
        if func == self.send_error:
            func(404, "Endpoint not found")
        else:
            func()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)  # Gets the data itself
        print(post_data)  # Prints the data to the console

        self.send_response(200)  # Sends a 200 OK response
        self.end_headers()
        self.wfile.write(b"POST request received")  #


def run(server_class=http.server.HTTPServer,
        handler_class=MyRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
