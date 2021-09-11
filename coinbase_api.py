import requests
import json
import time

from requests.api import get


#gets the current value of BTC in inr
while True :
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-INR/spot") #to change to other coin ../other coin-- currency/..
    data = response.json()
    currency = data["data"]["base"]
    price = data["data"]["amount"]
    print(f"Currency : {currency}  Price: ₹ {price}"),
    assets()
    Rates()
    time.sleep(5)

 
 
