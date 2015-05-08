from bs4 import BeautifulSoup
import requests
import threading
import socket

def crawler(url, socket_to_return):
    '''
    Handles the actual crawling. The parameter url is the target URL; socket_to_return specifies which socket to return to.
    '''
    
    soup = BeautifulSoup(requests.get(url)) # object containing HTML page data

    # I'm using requests to handle a general purpose connection, and sockets to handle the actual default
    # connection I want with my Javascript listener. MAybe a more sensible configuration could be defined...
    
    socket_to_return.send(soup.title.contents)
    socket_to_return.close() # closes the socket - this automatically makes my program require multiple connections
    # to handle more than one link. Maybe I should make it accept an array of URLs instead? Maybe employ JSON to handle
    # Javascript data?

    # This function has no way of determining images yet... let's be patient.
    

if __name__== "__main__":

    host = "127.0.0.1"
    port = 5000 # maybe one day change this to port 443, as part of improved security?

    sock = socket.socket() # create a socket object
    sock.bind((host,port)) # bind that sucker!
    sock.listen(5) # listens for five queued connections; maybe consider changing number in future?

    print "Your server has begun!"

    

    

    
    

