import requests
import json

base_url = "http://host1.open.uom.lk:8080/api/products/"

response = requests.get(base_url)
response.json()

todo = {"id": 85, "brand": "Araliya"}
response = requests.put(base_url, json=todo)
response.json()

print(response.json())