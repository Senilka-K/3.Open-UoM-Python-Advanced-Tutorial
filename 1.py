import requests
from bs4 import BeautifulSoup

url = 'https://glomark.lk/coconut/p/11624'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML element containing the price
    price_element = soup.find('span', {'class': 'price'})

    # Extract the price text
    price = price_element.text if price_element else 'Price not found'

    print(f'The price of the coconut is: {price}')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
    