









import webbrowser
import time
import requests

key = " INSERT KEY HERE " 

#response = requests.get("https://api.bestbuy.com/v1/products((search=Coffee)&sku=6015921)?apiKey=INSERTKEYHERE&sort=onlineAvailability.asc&show=onlineAvailability,addToCartUrl,name,url&format=json")
response = requests.get("https://api.bestbuy.com/v1/products((search=NVIDIA)&sku=6439402)?apiKey=INSERTKEYHERE&sort=onlineAvailability.asc&show=onlineAvailability,addToCartUrl,name&format=json")
print(response.json())
file = response.json()['products'][0]['onlineAvailability']
#link = repsonse.json()['products'][0]['addToCartURL']
#avail = file['onlineAvailability']
print(file)
while file is False:
    time.sleep(3)
    response = requests.get("https://api.bestbuy.com/v1/products((search=NVIDIA)&sku=6439402)?apiKey=INSERTKEYHERE&sort=onlineAvailability.asc&show=onlineAvailability,addToCartUrl,name&format=json")
    file = response.json()['products'][0]['onlineAvailability']
    print("Still nothing...")
    print(file)
   
if file is True: 
        print("Available, Adding to cart")
        #browser.get("https://api.bestbuy.com/click/-/6439402/cart")
        webbrowser.open("https://api.bestbuy.com/click/-/6439402/pdp")
        webbrowser.open("https://api.bestbuy.com/click/-/6439402/cart")
        time.sleep(500)

#browser.get("https://www.bestbuy.com/site/keurig-k-select-single-serve-k-cup-pod-coffee-maker-matte-black/6015921.p?skuId=6015921")
#browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")

