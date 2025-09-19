from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''
<html>
<body>
   <p>Edition:Windows 11Pro</p>
   <p>Version:24H2</p>
   <p>Processor:Intel i7-12700H</p>
   <p>Installed RAM: 16 GB</p>
   <p>System type: 64-bit Operating System</p>
</body>
</html>
'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address = ('',8000)
httpd =HTTPServer(server_address,Myserver)
httpd.serve_forever()