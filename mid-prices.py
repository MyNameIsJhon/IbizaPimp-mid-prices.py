import requests
from bs4 import BeautifulSoup #beautifulsoup me permet de parser les element du html afin de pouvoir les récupéré plus tard

server_code = 200

q = 2

url = "https://ibizapimp.com/shop" 
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

prices = soup.find_all("bdi")

moy = 0
i = 0

while page.status_code == 200 :
    prices = soup.find_all("bdi")
    
    for str_price in prices :
        price = float(str_price.text.replace("€", ""))
        moy += price
        i += 1

    url = "https://ibizapimp.com/shop" + "/page/" + str(q)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    q += 1
    print("Révision des pris de la page " + str(q - 1))

print("La moyenne des prix de toute la boutique en ligne Ibiza Pimp est : " + str(int(moy/i)) + "€")