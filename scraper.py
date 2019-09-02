from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse
import requests

class Scraper:
    def GetImageUrl(self, url):
        page = self._GetPage(url)
        aftercomic = page.find("div", {"id": "aftercomic"})        
        image = aftercomic.find("img")
        return image['src']

    def DownloadImage(self, url):
        img_data = requests.get(url).content
        image_name =  url.split('/')[-1]
        image_url = "./output/" + image_name
        with open(image_url, 'wb') as handler:
            handler.write(img_data)
    
    def GetNextComicUrl(self, url):
        page = self._GetPage(url)
        nextButton = page.find("a", {"class": "cc-next"})
        if nextButton is None:
            return ""
        return nextButton["href"]

    def _GetPage(self, url):
        return BeautifulSoup(urlopen(url), "html.parser")