import http.server
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class BadmintonHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Route root requests directly to badminton.html
        if self.path in ('/', ''):
            self.path = '/badminton.html'
        return super().do_GET()

if __name__ == '__main__':
    # Allow port override from command line if needed
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            pass

    # Ensure address reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("0.0.0.0", PORT), BadmintonHTTPHandler) as httpd:
        print(f"Serving Suryodaya Park Badminton Championship at: http://localhost:{PORT}")
        print(f"Direct link: http://localhost:{PORT}/badminton.html")
        sys.stdout.flush()
        httpd.serve_forever()
