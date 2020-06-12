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


url = "https://br.tradingview.com/symbols/BMFBOVESPA-"+str(tag)



chrome_options = Options() 
chrome_options.headless = True 
driver = webdriver.Chrome(options=chrome_options) #
driver.get(url)
time.sleep(3)
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser') 


financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[0]
valoracao = []
i = 0
for k in range(0, 10):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    valoracao.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[1]
historico_precos = []
i = 0
for k in range(0, 4):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    historico_precos.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[2]
bp = []
i = 0
for k in range(0, 6):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    bp.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[3]
dividendos = []
i = 0
for k in range(0, 3):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    dividendos.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[4]
operacionais = []
i = 0
for k in range(0, 4):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    operacionais.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[5]
margens = []
i = 0
for k in range(0, 4):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    margens.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[6]
renda = []
i = 0
for k in range(0, 10):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    renda.append(card)
    i = i + 1



dataset1 = pd.DataFrame(valoracao)
dataset2 = pd.DataFrame(historico_precos)
dataset3 = pd.DataFrame(bp)
dataset4 = pd.DataFrame(dividendos)
dataset5 = pd.DataFrame(operacionais)
dataset6 = pd.DataFrame(margens)
dataset7 = pd.DataFrame(renda)

print(dataset1)
print(dataset2)
print(dataset3)
print(dataset4)
print(dataset5)
print(dataset6)
print(dataset7)

driver.quit()