import bs4
import time
import pandas as pd
from bs4 import BeautifulSoup
import selenium 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



entrada = (input("Digite a Ação: "))
tag = entrada.upper()





url = "https://br.tradingview.com/symbols/BMFBOVESPA-"+str(tag)+"/technicals/"

chrome_options = Options() 
chrome_options.headless = True 
driver = webdriver.Chrome() #options=chrome_options
driver.get(url)
time.sleep(3)


# 1 dia
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser') 
table_dia = soup.find(class_ = 'table-1YbYSTk8')
table2_dia = soup.findAll(class_ = 'table-1YbYSTk8')[1]
osciladores_dia = pd.read_html(str(table_dia))
medias_moveis_dia = pd.read_html(str(table2_dia))
sinal_dia = soup.find('div', class_ = 'speedometerWrapper-1SNrYKXY summary-72Hk5lHE').find('span', class_ = 'speedometerSignal-pyzN--tL buyColor-4BaoBngr').get_text()
placar_dia = soup.findAll('div', class_ = 'countersWrapper-1TsBXTyc')[1].get_text()

# 1 semana
semana = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[1]/div/div/div[1]/div/div/div[7]').click()
time.sleep(3)
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser') 
table_semana = soup.find(class_ = 'table-1YbYSTk8')
table2_semana = soup.findAll(class_ = 'table-1YbYSTk8')[1]
osciladores_semana = pd.read_html(str(table_semana))
medias_moveis_semana = pd.read_html(str(table2_semana))
sinal_semana = soup.find('div', class_ = 'speedometerWrapper-1SNrYKXY summary-72Hk5lHE').find('span', class_ = 'speedometerSignal-pyzN--tL buyColor-4BaoBngr').get_text()
placar_semana = soup.findAll('div', class_ = 'countersWrapper-1TsBXTyc')[1].get_text()

# 1 mes
mes = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[1]/div/div/div[1]/div/div/div[8]').click()
time.sleep(3)
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser')
table_mes = soup.find(class_ = 'table-1YbYSTk8')
table2_mes = soup.findAll(class_ = 'table-1YbYSTk8')[1]
osciladores_mes = pd.read_html(str(table_mes))
medias_moveis_mes = pd.read_html(str(table2_mes))
sinal_mes = soup.find('div', class_ = 'speedometerWrapper-1SNrYKXY summary-72Hk5lHE').find('span', class_ = 'speedometerSignal-pyzN--tL buyColor-4BaoBngr').get_text()
placar_mes = soup.findAll('div', class_ = 'countersWrapper-1TsBXTyc')[1].get_text()


print(placar_mes)
print(placar_dia)

driver.quit()







