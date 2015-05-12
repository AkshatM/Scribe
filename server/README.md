# Notes

- `server.py` creates a server with only one GET method defined. It employs `crawler.py` for actual crawling. All responses are simply responses from `crawler.py`.
- Our crawler successfully handles images as well as text.
- Our server can be run as a background process. Ideally, it should handle every request in its own thread - this feature is not yet implemented. 
