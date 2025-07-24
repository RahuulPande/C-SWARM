#!/usr/bin/env python3
import http.server
import socketserver

PORT = 8000

class TestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Connection Test - Cognizant Talent Edge CRM</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
                .success { color: #0072C6; font-size: 24px; font-weight: bold; }
                .info { color: #333; margin: 20px 0; }
            </style>
        </head>
        <body>
            <h1 class="success">✅ Connection Successful!</h1>
            <p class="info">Your remote connection is working properly.</p>
            <p class="info">The Cognizant Talent Edge CRM Toolkit is running on port 8501.</p>
            <p class="info">Use the same connection method for port 8501 to access the full application.</p>
            <hr>
            <p><strong>Next Steps:</strong></p>
            <p>1. Close this tab</p>
            <p>2. Change the URL from :8000 to :8501</p>
            <p>3. Access the full Streamlit application</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), TestHandler) as httpd:
        print(f"🌐 Test server running on port {PORT}")
        print(f"📱 Access via: http://localhost:{PORT}")
        httpd.serve_forever()