# import requests
# r = requests.get("https://uom.lk/")
# print(r.status_code)
# print(r.url)
# print(r.text)

# import requests
# r = requests.get("https://httpbin.org/get")
# print(r.status_code)
# print(r.url)
# print(r.text)

# import requests
# r = requests.get("https://httpbin.org/obvious-incorrect")
# print(r.status_code)
# print(r.url)
# print(r.text)

import requests
r = requests.get("https://www.google.com/search?q=python")
print(r.status_code)
print(r.url)
print(r.text)
