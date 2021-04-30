import requests
from bs4 import BeautifulSoup
import time
import datetime

#ipAdress = '192.168.1.1'

def EthToDevice(ipAdress):
    url = 'http://' + ipAdress
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.79'}
    responsmy = requests.get(url, headers=headers)
    soup = BeautifulSoup(responsmy.content, 'html.parser')
    print("=" * 50)
    print("=" * 50)
    print("IpAdress Device: " + ipAdress)
    print("=" * 50)
    for i in range(8):
        qoutes = soup.find_all('div', {'id':'A', 'class':str(i)})

        for qoute in qoutes:
            today = datetime.datetime.today()

            print(today.strftime("[%Y-%m-%d  %H:%M:%S] AnalogPin ") + str(i), qoute.text)
    print("=" * 50)

    for i in range(2, 12):
        qoutes = soup.find_all('div', {'id':'D', 'class':str(i)})

        for qoute in qoutes:
            today = datetime.datetime.today()
            print(today.strftime("[%Y-%m-%d  %H:%M:%S] DigitalPin ") + str(i), qoute.text)



