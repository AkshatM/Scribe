from bs4 import BeautifulSoup
import requests
import re

def crawler(pattern):
    '''
    Handles the actual crawling. The parameter url is the target URL. Does some input handling.
    '''
    GRUBER_URLINTEXT_PAT = ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))' # taken from Kenneth Reitz' hypermark - identifies all URLs inside some text 

    url = re.search(GRUBER_URLINTEXT_PAT,pattern).group(0)

    print "Crawling the url: " + url

    try:

        response = requests.get(url)

        if 'image' not in response.headers['content-type']:
            soup = BeautifulSoup(requests.get(url).text) # object containing HTML page data
            return soup.title.string, response.headers['content-type']
        else:
            image_type = response.headers['content-type'].split('/')[-1]
            return response.content, response.headers['content-type']
        
    # I'm using requests to handle a general purpose connection, and sockets to handle the actual default
    # connection I want with my Javascript listener. MAybe a more sensible configuration could be defined...

    except:

        return 'ERR'