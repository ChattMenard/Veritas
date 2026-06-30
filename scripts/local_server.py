#!/usr/bin/env python3
"""Self-hosted local HTTP server for the evidence archive.

Usage:
    python3 scripts/local_server.py [--port 8080] [--root .]

Serves the entire repository over HTTP. No cloud. No GitHub.
Access at: http://localhost:8080
"""

import argparse
import http.server
import socketserver
import sys
from pathlib import Path


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow cross-origin access so mirrors can fetch
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def log_message(self, format, *args):
        # Log to stdout with a clear prefix
        print(f"[SERVER] {self.address_string()} - {format % args}")


def serve(port: int, root: Path):
    import os
    os.chdir(root)

    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        print(f"\n=== LOCAL EVIDENCE SERVER ===")
        print(f"Serving:    {root.resolve()}")
        print(f"URL:        http://localhost:{port}")
        print(f"Network:    http://{get_local_ip()}:{port}")
        print(f"\nCtrl+C to stop\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n=== SERVER STOPPED ===")


def get_local_ip() -> str:
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serve the archive locally.")
    parser.add_argument("--port", type=int, default=8080, help="Port to serve on")
    parser.add_argument("--root", default=".", help="Root directory to serve")
    args = parser.parse_args()

    serve(args.port, Path(args.root))
