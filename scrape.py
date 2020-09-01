from bs4 import BeautifulSoup
import requests as req



def getPage(url):
    try:
        response = req.get(url)
        response.raise_for_status()
    except req.exceptions.HTTPError as err:
        raise SystemExit(err)

    return response

def pageToText(page_obj):
    page_text = BeautifulSoup(page_obj.text, 'html.parser')

    return page_text

def parsePrice(soup):

    game_name = "Buy Monster Hunter: World"
    test = soup.find_all("h1", string=game_name)
    print(test)

    price_in_page = soup.select('.game_purchase_price')

    print(price_in_page)

p = getPage('https://store.steampowered.com/app/582010/Monster_Hunter_World/')

t = pageToText(p)

parsePrice(t)




