import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from time import sleep
from datetime import datetime

def get_currency_prices():
    
    currency = ['usd', 'eur', 'pln']

    while True:
        
        result = []
        for curr in currency:

            url = f'https://minfin.com.ua/ua/currency/auction/exchanger/{curr}/buy/lvov/'
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')
            for price in soup.find_all('span', class_='Typography cardHeadlineL align'):
                index = price.text.find(',') + 3
                result.append(price.text[:index])

        msg = f'{currency[0].upper()}: {result[0]}/{result[1]}\n{currency[1].upper()}: {result[2]}/{result[3]}\n{currency[2].upper()}: {result[4]}/{result[5]}'

        print(datetime.now())
        print(msg)
        print('----------------------------------------------')

        toast = ToastNotifier()
        toast.show_toast(title='Currency prices:', msg=msg, duration=60)
        sleep(1800)


if __name__ == '__main__':
    get_currency_prices()

