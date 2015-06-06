# RichTextGmail
A Chrome extension that converts URLs to embedded images or to title text, like Quora's text editor. I'm doing this because it's fun, and I really want to improve system designs. Currently, the back-end only works on Python 2.7 - however, use of the 2to3 module should mitigate this.  _Work in progress_

# Back-End

- A server that contains a Python crawler. On receipt of a URL, the crawler fetches the associated page and parses it for important human-readable information (a title tag or similar). If the URL points to an image file, it simply downloads the image. 
- Current design of system employs use of a self-designed HTTP server with support for only a GET request for handling communications. 

# Front-End

A Chrome extension that encodes a event handler on pressing the F2 key in the document window (rather than a compose window). An XMLHttpRequest is carried out, and the result replaces the URLs.

# Current Status

The back-end server is complete, with some possible room for improving API endpoint definitions. Current example of API endpoint definition can be seen in `server.py`. One can view examples within a favourite browser - the server has been successfully daemonised, and runs continuously on port 8080 of my domain.

The front-end component is nearing completion. It is able to recognise URLs within text using regular expressions, and implements a simple XMLHttpRequest to communicate with the server.

# Current Issues

* Google's content security policy does not permit access to HTTP sites from an HTTPS-encrypted website like Gmail. There are two ways to overcome this: a) obtain an SSL certificate and convert the endpoint to an HTTPS endpoint, which is expensive and honestly overkill, or b) use Mashape to wrap around the endpoint with an HTTPS extension free of charge, provided we alter the API endpoint definition to keep with the conventions MashApe uses.

* Images sent by the server tend to keep their own encodings, which may be a problem for Javascript. However, this has not been demonstrated yet but worth planning for.

* The F2 can only be pressed in the document window - it will not work if focus is on the composition or reply window.

Efforts are being made to resolve all of this.
