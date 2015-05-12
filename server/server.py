import BaseHttpServer as bhttp
from urlparse import urlparse as parser
from crawler import crawler

'''Implements BaseHTTPServer that runs the crawler before responding to a GET request.

GET request from client is URL-encoded i.e. desired URL is passed as a field in the response.

For instance, if I wanted to link to www.google.com, I could do:

GET www.example.com:5000/?https://www.google.com

The class Handler allows me to define the GET response.'''

class Handler(bhttp.BaseHTTPRequestHandler):

    def do_GET(session): # or I could have done 'self' instead of 'session' and kept with convention - I think this is clearer.
        url_to_be_queried = parser(session.path).query
        session.send_response(200)
        session.end_headers()
        session.wfile.write(crawler(url_to_be_queried))

if __name__ == '__main__'
    server = bhttp.HTTPServer(('localhost', 5000), Handler)
    print 'Starting server, use a KeyboardInterrupt to stop'
    server.serve_forever()
        
        
    