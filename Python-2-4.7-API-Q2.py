import requests
import json

def get_all_products(base_url):
    response = requests.get(f"{base_url}/api/products")

    if response.status_code == 200:
        data = response.json()

        if 'data' in data:
            products = data['data']
    
            total_products = len(products)
            print(total_products)
            
base_url = "http://host1.open.uom.lk:8080"
get_all_products(base_url)