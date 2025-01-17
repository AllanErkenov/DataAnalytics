from django.shortcuts import render
import requests
import json
from bs4 import BeautifulSoup
from django.http import HttpResponse
url=requests.get("https://api.coinbase.com/v2/exchange-rates?currency=USDT")
data=url.json()
Final=data["data"]["rates"]["RUB"]
url1=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd&include_last_updated_at=true")
data1=url1.json()
Final1=data1['tron']['usd']
url4=requests.get("https://ru-meteo.ru/moscow/hour")
soup1 = BeautifulSoup(url4.text, "html.parser")
temp=soup1.findAll('div', class_='current-temp')
temp1=str(temp)
temp2=BeautifulSoup(temp1,"html.parser")
temp3=temp2.findAll(string=True)
temp4=str(temp3[1])




def index(request):
    return HttpResponse(f"""
           <p>Курс USDT к рублю: {Final}</p>
           <p>Курс TRON к USDT: {Final1}</p>
           <p>Температура в Москве: {temp4}</p>
           <script> setTimeout(function(){{
   window.location.reload();
}}, 60000);
           </script>
       """)