#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

def application(ennv, res):
    res('200 OK', [('Content-Type', 'text/html')])
    for k in ennv:
        print('%s = %s' % (k,ennv[k]))
    return [b'<h1>Hello, world</h1>']

httpd = make_server('', 8000, application)

print("Server is Start on port 8000")

httpd.serve_forever()
