from bs4 import BeautifulSoup
import requests
import base64

def crawler(url):
    '''
    Handles the actual crawling.

    If the response headers of our HTTP GET request to the desired URL includes the word 'image', then we return the content of the response,
    and the response headers.

    If the response headers of our HTTP GET request DO NOT contain 'image', then we happily return the title of the page as a Unicode string,
    as well as the response headers for consistency.
    
    '''
    try: 

        response = requests.get(url) # get page source with HTTP GET request

        if 'image' not in response.headers['content-type']:
            soup = BeautifulSoup(requests.get(url).text) # object containing HTML page data
            return soup.title.string.encode('utf-8'), response.headers['content-type'] #return title string, response headers
        else:
            image_type = response.headers['content-type'].split('/')[-1]
            return base64.b64encode(response.content), response.headers['content-type'] # return image in base 64, response headers

    except:

        return 'ERR'
