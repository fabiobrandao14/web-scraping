#!/usr/bin/env python
# coding: utf-8

# In[15]:


import bs4
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select

def sep():
	print('\n\n','***********************************************************************************''\n\n')


url = 'https://www.bcb.gov.br'

options = Options() 
options.headless = True 
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(options=options) #
driver.get(url)

driver.implicitly_wait(10)

element = driver.find_element_by_xpath("//*[@id='home']")

html = element.get_attribute('outerHTML')

soup = BeautifulSoup(html, 'html.parser')

# Inflação 

table = soup.find(class_ = 'complemento mb-3 mb-md-2')

df = pd.read_html(str(table))
inflacao_realizada = soup.find('div', {'class': 'percentual light mr-2'}).get_text()


table_cambio = soup.find('div', class_ = 'componente cotacao')
cambio = pd.read_html(str(table_cambio))
cambio


div_selic = soup.findAll('div', class_ = 'percentual light mr-2')[1].get_text()
div_selic

sep()
print(df)
sep()
print("Inflação 12 meses -->", inflacao_realizada)
sep()
print(cambio)
sep()
print("tx Selic -->", div_selic)
sep()



	