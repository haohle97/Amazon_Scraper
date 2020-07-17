import requests 
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Sony-Noise-Cancelling-Headphones-WH1000XM3/dp/B07G4MNFS1/ref=sr_1_1_sspa?crid=3MHFEP0A0UV0I&dchild=1&keywords=sony+wh-1000xm3&qid=1594942257&sprefix=sony+%2Caps%2C217&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNjJSUkFOQVpYMVFCJmVuY3J5cHRlZElkPUEwOTUyOTkwMlExMDA5WldONkpaSSZlbmNyeXB0ZWRBZElkPUEwNDU1MzY3MlVCVFhBSVNNRTRYQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml') 

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    
    converted_price = float(price[1:]) #get all the characters after the currency symbol and cast it to float. The resulting value can also be used to calculate total price for a list of products

    if(converted_price < 200):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 200):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hao.le122396@gmail.com', 'zxuyjqmfbiimtzmd')

    subject = 'Price fell down!'
    body = 'Check the Amazon link https://www.amazon.com/Sony-Noise-Cancelling-Headphones-WH1000XM3/dp/B07G4MNFS1/ref=sr_1_1_sspa?crid=3MHFEP0A0UV0I&dchild=1&keywords=sony+wh-1000xm3&qid=1594942257&sprefix=sony+%2Caps%2C217&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNjJSUkFOQVpYMVFCJmVuY3J5cHRlZElkPUEwOTUyOTkwMlExMDA5WldONkpaSSZlbmNyeXB0ZWRBZElkPUEwNDU1MzY3MlVCVFhBSVNNRTRYQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'hao.le122396@gmail.com',
        'lynnleofficial@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


check_price()