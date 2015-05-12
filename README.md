# RichTextGmail
A Chrome extension that converts URLs to embedded images or to title text, like Quora's text editor. I'm doing this because it's fun, and I really want to improve system designs. _Work in progress_

# Back-End

- A server that contains a Python crawler. On receipt of a URL, the crawler fetches the associated page and parses it for important human-readable information (a title tag or similar). If the URL points to an image file, it simply downloads the image. 
- Current design of system employs use of a TCP socket for handling communications from the front-end, as well as the requests and BeautifulSoup library for actual retrieval of page data.

Comments:
- (May 11th 2015) The use of a TCP socket by itself is very primitive, unsuitable for image handling when image sizes are potentially unknown, and there may be issues with Websocket protocols with the front-end. Why not define an HTTP server with only a single GET method defined instead? This allows much neater abstraction via a simple API interface, and Javascript can easily make HTTP GET requests without the fuss of invoking Websockets. 
- (May 11th 2015) The defined GET method could encapsulate the current behaviour of the Python crawler. In other words, when a client makes a GET request with some parameters, our API feeds the parameters to our crawler, and responds with the results of the crawler. Image files are first saved on the server, sent to the client, then deleted, freeing up disk space instantly.

# Front-End

- A Javascript listener that either uses AJAX or can simply be invoked upon some user event (like [TeX for Gmail](https://chrome.google.com/webstore/detail/tex-for-gmail/gjnmclkoadjdljnfmbnnhaahilafoeji?hl=en)). Upon invokation, the Javascript uses a regular expression to obtain all links in the text editor and dynamically replaces them once the server returns with the required information.

# Current Progress:
- (May 11th 2015) Built a Python crawler server-side framework that can return page title text. Requires [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Requests](http://docs.python-requests.org/en/latest/), and uses native socket library for handling and receiving URLs. Uses Python 2.7.9. Currently working on image handling extension.
- Built a test file for crawler; will soon expand into proper testing framework. Current - and only - test passes. Instructions included in file. 

Currently, the crawler passes our test! 
