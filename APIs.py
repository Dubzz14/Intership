import requests

receipt = requests.get("https://dummyjson.com/products")

print(receipt.json())