# RichTextGmail
A Chrome extension that converts URLs to embedded images or to title text, like Quora's text editor. _Work in progress_

# Back-End

- A server that contains a Python crawler. On receipt of a URL, the crawler fetches the associated page and parses it for important human-readable information (a title tag or similar). If the URL points to an image file, it simply downloads the image. 

# Front-End

- A Javascript listener that either uses AJAX or can simply be invoked upon some user event (like [TeX for Gmail](https://chrome.google.com/webstore/detail/tex-for-gmail/gjnmclkoadjdljnfmbnnhaahilafoeji?hl=en)). Upon invokation, the Javascript uses a regular expression to obtain all links in the text editor and dynamically replaces them once the server returns with the required information.

# Current Progress:
- Built the Python crawler server-side framework. Requires [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Requests](http://docs.python-requests.org/en/latest/), and uses native socket library for handling and receiving URLs. Uses Python 2.7.9.
- Built a test file for crawler; will soon expand into proper testing framework. Current - and only - test passes. Instructions included in file. 

Currently, the crawler passes our test! 
