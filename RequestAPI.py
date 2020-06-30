from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

URL = "https://www.google.com/"
URL2="https://www.bbc.com/"


class RequestAPI(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36(KHTML, like Gecko) Chrome",
            "Accept": "text/html,application/xhtml+xml,application/xml;q = 0.9, image / webp, * / *;q = 0.8"}


    def call_api(self):
        req =  Request(self.url, headers= self.headers)
        page = urlopen(req)
        soup = BeautifulSoup(page,features="html.parser")
        return soup.text;



ra = RequestAPI(URL2)
print(ra.call_api())
