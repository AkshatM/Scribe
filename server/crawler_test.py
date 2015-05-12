import socket

''' This tests crawler.py. 

Please run crawler.py first (either as daemon or in separate window), then run this file.'''

test_url = "https://www.youtube.com/watch?v=LJTaPaFGmM4"

sock = socket.socket()

host = "127.0.0.1"
port = 5000

sock.connect((host,port))

sock.send(test_url)
print "Sent!"
# should return 'Python Advanced Tutorial 6.6 - Simple File Server - YouTube' somewhere

print "Received!"
print sock.recv(4096)