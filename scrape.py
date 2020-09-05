from bs4 import BeautifulSoup
import requests as req




def getSteamItemURL(item_name: str):
    base_url = 'https://store.steampowered.com/search/?term='
    formatted_name = item_name.replace(' ', '+')
    item_url = base_url+formatted_name
    print("return value from getSteamURL() func: " + item_url)
    return item_url

def getPage(url):
    try:
        response = req.get(url)
        response.raise_for_status()
    except req.exceptions.HTTPError as err:
        raise SystemExit(err)
    print("return value from getPage() func: {} ".format(response))
    return response

def pageToText(page_obj):
    page_text = BeautifulSoup(page_obj.text, 'html.parser')
    
    # print("return value from pagetoText() func: {}".format(page_text))
    return page_text

def parsePrice(soup):

    regular_price_class = "col search_price responsive_secondrow"
    discounted_price_class = "col search_price discounted responsive_secondrow"
    

    price = soup.find_all("div", class_= discounted_price_class)
    if not price:
        price = soup.find_all("div", class_= regular_price_class)[0].text
    else: 
        price =  soup.find_all("div", class_= discounted_price_class)[0].text
    # test = soup.find_all("div", class_="col search_price responsive_secondrow")[0].text
    print(price)

    # price_in_page = soup.select('.game_purchase_price')

   
    # print(type(price_in_page))

# p = getPage(getSteamItem('Battlefront'))

# t = pageToText(p)

# parsePrice(t)




def run():
    search_item_url = getSteamItemURL('battlefront 2')
    page_response = getPage(search_item_url)
    page_text = pageToText(page_response)
    price = parsePrice(page_text)




run()