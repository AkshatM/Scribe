from bs4 import BeautifulSoup
import requests
import re

def crawler(pattern):
    '''
    Handles the actual crawling. The parameter 'pattern' is a text pattern the Javascript listener sends along.

    This function does some input handling to extract a URL from the Javascript listener, and then to crawl that page.

    If the response headers of our HTTP GET request to the desired URL includes the word 'image', then we return the content of the response,
    and the response headers.

    If the response headers of our HTTP GET request DO NOT contain 'image', then we happily return the title of the page as a Unicode string,
    as well as the response headers for consistency.
    
    '''

    GRUBER_URLINTEXT_PAT = ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))' # taken from Kenneth Reitz' hypermark - identifies all URLs inside some text 

    url = re.search(GRUBER_URLINTEXT_PAT,pattern).group(0) # finds all URLS in pattern

    print("Crawling the url: " + url) # needs no explanation

    try: 

        response = requests.get(url) # get page source with HTTP GET request

        if 'image' not in response.headers['content-type']:
            soup = BeautifulSoup(requests.get(url).text) # object containing HTML page data
            return soup.title.string, response.headers['content-type'] #return title string, response headers
        else:
            image_type = response.headers['content-type'].split('/')[-1]
            return response.content, response.headers['content-type'] # return image, response headers

    except:

        return 'ERR'
