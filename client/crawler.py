from bs4 import BeautifulSoup
import requests
import threading
import socket

def crawler(url):
    '''
    Handles the actual crawling.
    '''

    soup = BeautifulSoup(requests.get(url)) # object containing HTML page data
    return soup.title.contents

if __name__== "__main__":

    host = "127.0.0.1"
    port = 5000 # maybe one day change this to port 443, in security plans?

    sock = socket.socket()
    sock.bind((host,port))
    sock.listen(5) # listens for five queued connections; maybe consider changing number in future?
    

