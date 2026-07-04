#!/usr/bin/env python3
"""Hamburg Slot Monitor — simple local server."""
import http.server
import socketserver
import os
import sys

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.js': 'application/javascript'})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Hamburg Slot Monitor запущен: http://localhost:{PORT}")
    print("Нажмите Ctrl+C для остановки")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nОстановлен.")
        sys.exit(0)
