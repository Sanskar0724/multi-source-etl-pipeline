import requests 

def get_products():
    response = requests.get("https://fakestoreapi.com//products",timeout=10)
    data = response.json()
    return data
