import BaseHTTPServer as bhttp
from urlparse import urlparse as parser
from crawler import crawler
from SocketServer import ThreadingMixIn

port = 8080 # default port to use

'''Implements BaseHTTPServer that runs the crawler before responding to a GET request.

GET request from client is URL-encoded i.e. desired URL is passed as a field in the response.

For instance, if I wanted to link to www.google.com, I could do:

GET www.example.com:<port>/?https://www.google.com

The class Handler allows me to define the GET response.'''

class Handler(bhttp.BaseHTTPRequestHandler):        

    def do_GET(self):
        requests_response = crawler(parser(self.path).query)
        if requests_response != 'ERR':
            self.send_response(200)
            self.send_header("Content-type", requests_response[-1])
            self.end_headers()
            self.wfile.write(requests_response[0])
        else:
            self.send_error(400)

    def log_message(self, format, *args):
        # uncomment following to enable logging into file. I want to save limited memory, so nothing should be logged.
        #open('message.log', "a").write("%s - - [%s] %s\n" % (self.address_string(),self.log_date_time_string(),format%args))
        return

class ThreadedHTTPServer(ThreadingMixIn, bhttp.HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('www.akshatm.com', port), Handler) #alter localhost to actual IP
    print('Starting server...')
    #try:
    server.serve_forever()
    #except KeyboardInterrupt:
    #    server.server_close()
    #    print("Server ended")
        
        
    
