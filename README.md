# RichTextGmail
A Chrome extension that converts URLs to embedded images or to title text, like Quora's text editor. I'm doing this because it's fun, and I really want to improve system designs. _Work in progress_

# Back-End

- A server that contains a Python crawler. On receipt of a URL, the crawler fetches the associated page and parses it for important human-readable information (a title tag or similar). If the URL points to an image file, it simply downloads the image. 
- Current design of system employs ~use of a TCP socket~ use of a self-designed HTTP server with support for ony a GET request for handling communications from the front-end, as well as the requests and BeautifulSoup library for actual retrieval of page data.

Comments:
- (May 11th 2015) The use of a TCP socket by itself is very primitive, unsuitable for image handling when image sizes are potentially unknown, and there may be issues with Websocket protocols with the front-end. Why not define an HTTP server with only a single GET method defined instead? This allows much neater abstraction via a simple API interface, and Javascript can easily make HTTP GET requests without the fuss of invoking Websockets. 
- (May 11th 2015) The defined GET method could encapsulate the current behaviour of the Python crawler. In other words, when a client makes a GET request with some parameters, our API feeds the parameters to our crawler, and responds with the results of the crawler. Image files are first saved on the server, sent to the client, then deleted, freeing up disk space instantly.
- (May 12th 2015) Saving an image is unnecessary - so long as MIME type is known, `requests` can directly forward the data packet to the client. However, a current implementation requires a simple (but in practice messy-looking) URL scheme that thankfully humans will hopefully never have to worry about. The HTTP server has been implemented, and the server-side code looks much cleaner. However, no threading support has yet been included.

# Front-End

- A Javascript listener that either uses AJAX or can simply be invoked upon some user event (like [TeX for Gmail](https://chrome.google.com/webstore/detail/tex-for-gmail/gjnmclkoadjdljnfmbnnhaahilafoeji?hl=en)). Upon invokation, the Javascript uses a regular expression to obtain all links in the text editor and dynamically replaces them once the server returns with the required information.

# Current Progress:
- (May 11th 2015) Built a Python crawler server-side framework that can return page title text. Requires [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Requests](http://docs.python-requests.org/en/latest/), and uses native socket library for handling and receiving URLs. Uses Python 2.7.9. Currently working on image handling extension.
- ~Built a test file for crawler; will soon expand into proper testing framework. Current - and only - test passes. Instructions included in file.~ (May 12th 2015) This idea has been put on the backburner for now - manual tests suffice for the moment, and all tests are currently met.
- (May 12th 2015) Rewrote server-side framework to expand into proper HTTP server, so as to make a real API instead of employing klunky `socket` module. Current tests all pass; crawler can now return images and text, which was our desired behaviour. This has been tested in Chrome, but should also work in all IE and Firefox.
