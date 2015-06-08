# RichTextGmail
A Chrome extension that converts raw text URLs in Gmail to embedded images or to friendly hyperlinks with page title text, like Quora's text editor. I'm doing this because it's fun, and I really want to improve system designs. Currently, the back-end only works on Python 2.7 - however, use of the 2to3 module should mitigate this.  _Work in progress_

# Back-End

- A server that contains a Python crawler. On receipt of a URL, the crawler fetches the associated page and parses it for important human-readable information (a title tag or similar). If the URL points to an image file, it simply downloads the image. 
- Current design of system employs use of a self-designed HTTP server with support for only a GET request for handling communications. An HTTPS wrapper provided by Mashaope's convenient API functionality allows us to access this point from an HTTPS endpoint.

# Front-End

A Chrome extension that encodes an event handler on pressing the F2 key in the document window (rather than a compose window). An XMLHttpRequest is carried out synchronously, and the result replaces the URLs. 

# Current Status

**This Chrome extension is able to reproduce all the desired functionality.** Pressing the F2 key in the document window once converts all raw URLs to human-readable links and actual images. All that's left is to iron out a few kinks that would subtract from user experience (see Issues).

The back-end server is complete, with an HTTPS middleman ensuring security. Current example of API endpoint definition can be seen in `server.py`. One can view examples within a favourite browser - the server has been successfully daemonised, and runs continuously on port 8080 of my domain.

The front-end component is nearing completion. It is able to recognise URLs within text using regular expressions, and implements a simple XMLHttpRequest to communicate with the server. Currently this XMLHttpPRequest works synchronously (i.e. the document will wait until the request is handled), something I plan to fix soon (this does mimic Quora's behaviour, but that is no excuse for embracing deprecated functionality). It replaces the text in a compose window with nice hyperlinks and images.

# Current Issues

* The F2 can only be pressed in the document window - it will not work if focus is on the composition or reply window. One should ideally focus on the compose or reply window that the user is on, and allow the application to affect that window.

* Use of this extension does not preserve page formatting. This is because of us assigning the result of an `innerText` replacement to `innerHTML`. However, iterating through `innerHTML` causes more problems since our regular expression is not configured to be smart. Using regex on HTML is bad in any case, which is why we stick to plain text instead.

* Pressing F2 with existing hyperlinks or images in text changes existing hyperlinks. This is a fault in `listener.js` - particularly, we are essentially resetting the `innerHTML` to find all URLs and replace them with anchor tags, _even those that are already in anchor tags_. 

Efforts are being made to resolve all of this.
