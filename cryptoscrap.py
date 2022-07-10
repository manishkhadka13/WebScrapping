import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
crypto_name = []
crypto_marketcap = []
crypto_price = []
crypto_circulating = []
crypto_symbol = []
df=pd.DataFrame()
def scrape(date):
    url=(('https://coinmarketcap.com/historical/')+date)
    webpage=requests.get(url)
    soup=BeautifulSoup(webpage.text, 'html.parser')
    tr=soup.find_all('tr',attrs={'class':'cmc-table-row'})
    count=0
    for row in tr:
        if count==25:
            break;
        try:
            #print(count)
            count=count+1
            name_column=row.find('td',attrs={'class':'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'}) 
            cry_name=name_column.find('a',attrs={'class':'cmc-table__column-name--name cmc-link'}).text.strip() 
            crypto_mcap=row.find('td',attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()
            cry_price=row.find('td',attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
            crypto_supply_and_sym=row.find('td',attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
            crypto_supply=crypto_supply_and_sym.split(' ')[0]
            crypto_sym=crypto_supply_and_sym.split(' ')[1]
            #print(cry_name)
            crypto_name.append(cry_name)
            crypto_marketcap.append(crypto_mcap)
            crypto_price.append(cry_price)
            crypto_circulating.append(crypto_supply)
            crypto_symbol.append(crypto_sym)
        except:
            print(count,"From except")
            continue
scrape('20220429/')    
df['Name']=crypto_name
df['Market Capitalization']=crypto_marketcap
df['Price']=crypto_price
df['Circulating Supply']=crypto_circulating
df['Symbol']=crypto_symbol
print(df)