import os
import requests
import fake_useragent
import urllib3
from bs4 import BeautifulSoup as bs4
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = os.getenv('URL')
URL_VIP = os.getenv('URL_VIP')

class Parser:
    user = fake_useragent.UserAgent().random
    def pars(self):
        self.r = requests.get(URL, verify=False)
        self.soup = bs4(self.r.text, 'lxml')
        self.info = self.soup.findAll('div', {'class':'table-flex__cell table-flex__cell--without-padding padding-left-default'})
        self.kurs = f'{self.info[0].text}: \n USD: {self.info[1].text} \n EUR: {self.info[2].text} \n'

    def __str__(self) -> str:
        return self.kurs

class VIP_Parser:
    user = fake_useragent.UserAgent().random
    def vip_pars(self):
        self.body = requests.get(URL_VIP, verify=False)
        self.soup = bs4(self.body.text, 'lxml')
        self.info = self.soup.find('div', {'class': 'currency-table__large-text'}).text
        self.info = f'GBP: {self.info}'
    
    def __str__(self) -> str:
        return self.info

P = Parser()
P.pars()
info = P.__str__()

V = VIP_Parser()
V.vip_pars()
vip_info = info + V.__str__()

          

        
