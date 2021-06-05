import requests
from bs4 import BeautifulSoup
import lxml
import re

class search_item:
    def bul():
        user_input = input("search ?")
        link = "https://www.gittigidiyor.com/arama/?k="+user_input
        page_input = input("enter page number ? ")
        link = link+"&sf="+page_input
        site = requests.get(link)
        soup = BeautifulSoup(site.content, "lxml")
        data = soup.find_all("p", {"class" : "fiyat price-txt robotobold price"})
        price_list = []
        for x in data:
            a = str(x)
            b = re.split(" ", a)
            c = list(b)
            price_list.append(c[24])
                
        data1 = soup.find_all("h3", {"class" : "product-title"})
        name_list = []
        for x in data1:
            a = x.find("span").text
            name_list.append(a)
        output = list(zip(price_list, name_list))
        for x,y in output:
            print(f"{x} : {y}")
        
