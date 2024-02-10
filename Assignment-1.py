# import requests
# from bs4 import BeautifulSoup

# def get_price(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Example: If the price is inside an element with class 'price'
#     price_element = soup.find(class_='price')

#     # Extract the text content of the element (assuming it's just the price)
#     # You may need to perform additional parsing or handle different HTML structures
#     price = (price_element.text.strip().replace('$', ''))

#     return price

# # Example usage
# laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
# glomark_coconut = 'https://glomark.lk/coconut/p/11624'

# laughs_price = get_price(laughs_coconut)
# glomark_price = get_price(glomark_coconut)

# print(f"Laughs Coconut price: {laughs_price}")
# print(f"Glomark Coconut price: {glomark_price}")

# import requests
# from bs4 import BeautifulSoup

# def extract_price_laughs(url):
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         price_element_laughs = soup.find('span', class_='price')

#         price_laughs = price_element_laughs.text if price_element_laughs else "Price not found"

#         return price_laughs
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")
#         return None
    
# def extract_price_glomark(url):
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         price_element_glomark = soup.find('span', id="product-promotion-price")

#         price_glomark = price_element_glomark.text if price_element_glomark else "Price not found"

#         return price_glomark
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")
#         return None

# laughs_coconut_price = extract_price_laughs('https://scrape-sm1.github.io/site1/COCONUT%20market1super.html')
# glomark_coconut_price = extract_price_glomark('https://glomark.lk/coconut/p/11624')

# print(f"Laughs Coconut Price: {laughs_coconut_price}")
# print(f"Glomark Coconut Price: {glomark_coconut_price}")

import requests
from bs4 import BeautifulSoup

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

        price = price_element.text.strip() if price_element else "Price not found"
        return price
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def compare_prices(product_laughs, product_glomark):
    laughs_price = get_price(product_laughs, 'laughs')
    glomark_price = get_price(product_glomark, 'glomark')

    print(f'Laughs  "COCONUT - Item#mr-2058" Rs.: {laughs_price}')
    print(f'Glomark "Coconut" Rs.: {glomark_price}')

    if laughs_price and glomark_price:
        if laughs_price > glomark_price:
            print(f'Glomark is cheaper: {laughs_price - glomark_price}')
        elif laughs_price < glomark_price:
            print(f'Laughs is cheaper: {glomark_price - laughs_price}')
        else:
            print('Price is the same')

# Example usage
laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'

compare_prices(laughs_coconut, glomark_coconut)

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

#         price = price_element.text.strip() if price_element else None
#         return price
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")
#         return None

# def compare_prices(product_laughs, product_glomark):
#     laughs_price = get_price(product_laughs, 'laughs')
#     glomark_price = get_price(product_glomark, 'glomark')

#     if laughs_price is not None:
#         print(f'Laughs   COCONUT - Item#mr-2058 Rs.:  {laughs_price}')
#     else:
#         print('Laughs price not found')

#     if glomark_price is not None:
#         print(f'Glomark  Coconut Rs.:  {glomark_price}')
#     else:
#         print('Glomark price not found')

#     if laughs_price is not None and glomark_price is not None:
#         laughs_price = float(laughs_price)
#         glomark_price = float(glomark_price)

#         if laughs_price < glomark_price:
#             print(f'Laughs is cheaper Rs.: {glomark_price - laughs_price}')
#         elif laughs_price > glomark_price:
#             print(f'Glomark is cheaper Rs.: {laughs_price - glomark_price}')
#         else:
#             print('Price is the same')

# # Example usage
# laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
# glomark_coconut = 'https://glomark.lk/coconut/p/11624'

# compare_prices(laughs_coconut, glomark_coconut)


