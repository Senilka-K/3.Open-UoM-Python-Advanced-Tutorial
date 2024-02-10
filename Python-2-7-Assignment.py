import requests
from bs4 import BeautifulSoup

def get_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Write code to extract the price from the HTML content
    # Replace the following line with the actual code based on the structure of the webpage
    # price = 0.0

    # return price

def compare_prices(product_laughs, product_glomark):
    laughs_price = get_price(product_laughs)
    glomark_price = get_price(product_glomark)

    # if laughs_price < glomark_price:
    #     print(f"{product_laughs} is cheaper at {laughs_price} compared to {product_glomark} at {glomark_price}")
    # elif laughs_price > glomark_price:
    #     print(f"{product_glomark} is cheaper at {glomark_price} compared to {product_laughs} at {laughs_price}")
    # else:
    #     print(f"The prices of {product_laughs} and {product_glomark} are the same at {laughs_price}")

    print('Laughs  ',"COCONUT - Item#mr-2058",'Rs.: ' , laughs_price)
    print('Glomark ',"Coconut",'Rs.: ' , glomark_price)
    
    if(laughs_price>glomark_price):
        print('Glomark is cheaper:',laughs_price - glomark_price)
    elif(laughs_price<glomark_price):
        print('Laughs is cheaper:',glomark_price - laughs_price)    
    else:
        print('Price is the same')

# Example usage
laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'

compare_prices(laughs_coconut, glomark_coconut)
