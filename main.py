import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):
    def load_json(self):
        with open('list.txt', 'r') as file:
            return file.read()

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("[]", "utf-8"))

    def do_GET(self):
        json_data = self.load_json()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(json_data), "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http:/%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
