#!/usr/bin/env python3
"""
Simple HTTP server for testing the Bill Splitter website locally.
Run this script to start a local server on http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import sys
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = MyHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 Server running at http://localhost:{PORT}/")
            print(f"📁 Serving directory: {os.getcwd()}")
            print("\nPress Ctrl+C to stop the server\n")
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}')
            except:
                pass
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use.")
            print(f"   Try a different port: python3 server.py {PORT + 1}")
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8000.")
    main()

