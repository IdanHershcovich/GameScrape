from bs4 import BeautifulSoup
import requests as req
import GameInfo

class SteamScrape:
    def __init__(self, name, url = None, soup = None,):
        self.name = name
        self.url = url
        self.soup = soup



    def getSteamItemURL(item_name: str):
        base_url = 'https://store.steampowered.com/search/?term='
        formatted_name = item_name.replace(' ', '+')
        item_url = base_url+formatted_name
        print("return value from getSteamURL() func: " + item_url)
        self.url = item_url

    def getPageSoup():
        try:
            response = req.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
        except req.exceptions.HTTPError as err:
            raise SystemExit(err)
        self.soup = soup


    # def pageToText(page_obj):
    #     page_text = BeautifulSoup(page_obj.text, 'html.parser')
        
    #     return page_text

    def parsePrice():
        soup = self.soup
        
        regular_price_class = "col search_price responsive_secondrow"
        discounted_price_class = "col search_price discounted responsive_secondrow"
        

        if soup.find_all("div", class_= discounted_price_class):
            price = soup.find_all("div", class_= discounted_price_class)[0].text
        else:
            price = soup.find_all("div", class_= regular_price_class)[0].text
        print(price)




    def run():
        search_item_url = getSteamItemURL('battlefront 2')
        page_response = getPage(search_item_url)
        page_text = pageToText(page_response)
        price = parsePrice(page_text)




run()