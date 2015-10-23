#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 

from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starte simple_httpd auf Port: ' + str(httpd.server_port))

httpd.serve_forever()
