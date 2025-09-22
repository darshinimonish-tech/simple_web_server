# EX01 Developing a Simple Webserver

# Date: 19/09/2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:from http.server import HTTPServer,BaseHTTPRequestHandler
content =
```
from http.server import HTTPServer,BaseHTTPRequestHandler
content ="""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TCP/IP Protocol Suite</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    table {
      border-collapse: collapse;
      width: 70%;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    th, td {
      border: 1px solid #555;
      padding: 12px;
      text-align: center;
    }
    th {
      background-color: #333;
      color: #fff;
    }
    tr:nth-child(even) {
      background-color: #eaeaea;
    }
    tr:nth-child(odd) {
      background-color: #ffffff;
    }
    caption {
      font-size: 22px;
      margin-bottom: 15px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <table>
    <caption>TCP/IP Protocol Suite</caption>
    <tr>
      <th>Layer</th>
      <th>Protocols</th>
    </tr>
    <tr>
      <td>Application Layer</td>
      <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP, Telnet</td>
    </tr>
    <tr>
      <td>Transport Layer</td>
      <td>TCP, UDP</td>
    </tr>
    <tr>
      <td>Internet Layer</td>git
      <td>IP (IPv4/IPv6), ICMP, ARP</td>
    </tr>
    <tr>
      <td>Network Interface Layer</td>
"""
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
```
# OUTPUT:
![alt text](<Screenshot 2025-09-19 201210.png>)
![alt text](<Screenshot 2025-09-19 201317.png>)


# RESULT:
The program for implementing simple webserver is executed successfully.
