# import requests
# from bs4 import BeautifulSoup

# def get_price(url, source):
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         if source == 'laughs':
#             price_element = soup.find('div', class_='price-box').find('span', class_='price')
#         elif source == 'glomark':
#             price_element = soup.find('div', class_='price').find('span', id='product-promotion-price')
#         else:
#             print("Invalid source provided")
#             return None

#         price = price_element.text.strip() if price_element else "Price not found"
#         return price
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")
#         return None
    
# def compare_prices(product_laughs, product_glomark):
#     laughs_price = get_price(product_laughs, 'laughs')
#     glomark_price = get_price(product_glomark, 'glomark')

#     print(f'Laughs  "COCONUT - Item#mr-2058" Rs.: {laughs_price}')
#     print(f'Glomark "Coconut" Rs.: {glomark_price}')

# laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
# glomark_coconut = 'https://glomark.lk/coconut/p/11624'

# compare_prices(laughs_coconut, glomark_coconut)


# import requests
# from bs4 import BeautifulSoup
# import re

# def get_price(url, source):
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         if source == 'laughs':
#             price_element = soup.find('div', class_='price-box').find('span', class_='price')
#         elif source == 'glomark':
#             price_element = soup.find('div', class_='price').find('span', id='product-promotion-price')
#         else:
#             print("Invalid source provided")
#             return None

#         price_text = price_element.text.strip() if price_element else "Price not found"

#         # Extracting the numeric part using regular expression
#         match = re.search(r'\d+\.\d+', price_text)
#         if match:
#             price_as_float = float(match.group())
#             return price_as_float
#         else:
#             return None
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")
#         return None
    
# def compare_prices(product_laughs, product_glomark):
#     laughs_price = get_price(product_laughs, 'laughs')
#     glomark_price = get_price(product_glomark, 'glomark')

#     if laughs_price is not None:
#         print(f'Laughs "COCONUT - Item#mr-2058" Price: Rs. {laughs_price:.2f}')
#     else:
#         print('Laughs price not found')

#     if glomark_price is not None:
#         print(f'Glomark "Coconut" Price: Rs. {glomark_price:.2f}')
#     else:
#         print('Glomark price not found')


# laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
# glomark_coconut = 'https://glomark.lk/coconut/p/11624'

# compare_prices(laughs_coconut, glomark_coconut)

import requests
from bs4 import BeautifulSoup
import re

def get_price(url, source):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        if source == 'laughs':
            price_element = soup.find('div', class_='price-box').find('span', class_='price')
        elif source == 'glomark':
            price_element = soup.find('div', class_='price').find('span', id='product-promotion-price')
        else:
            print("Invalid source provided")
            return None

        price_text = price_element.text.strip() if price_element else "Price not found"

        # Extracting the numeric part using regular expression
        match = re.search(r'\d+\.\d+', price_text)
        if match:
            price_as_float = float(match.group())
            return price_as_float
        else:
            return None
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
def compare_prices(product_laughs, product_glomark):
    laughs_price = (get_price(product_laughs, 'laughs'))
    glomark_price = (get_price(product_glomark, 'glomark'))

    if laughs_price is not None:
        print(f'Laughs "COCONUT - Item#mr-2058" Price: Rs. {laughs_price:.2f}')
    else:
        print('Laughs price not found')

    if glomark_price is not None:
        print(f'Glomark "Coconut" Price: Rs. {glomark_price:.2f}')
    else:
        print('Glomark price not found')

    if laughs_price > glomark_price:
        print(f'Glomark is cheaper: Rs. {laughs_price - glomark_price:.2f}')
    elif laughs_price < glomark_price:
        print(f'Laughs is cheaper: Rs. {glomark_price - laughs_price:.2f}')
    else:
        print('Price is the same')

laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'

compare_prices(laughs_coconut, glomark_coconut)


# laughs_tissues = 'https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html'
# glomark_tissues = 'https://glomark.lk/flora-facial-tissues-160s/p/10470'

# compare_prices(laughs_tissues,glomark_tissues)


# laughs_bread = 'https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html'
# glomark_bread = 'https://glomark.lk/sandwich-bread-450g/p/13606'

# compare_prices(laughs_bread,glomark_bread)