import bs4
import time
import pandas as pd
from bs4 import BeautifulSoup
import selenium 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.bcb.gov.br/en/publications/copomminutes/cronologicos'

chrome_options = Options() 
chrome_options.headless = True 

driver = webdriver.Chrome() #options=chrome_optionsß
driver.get(url)

time.sleep(3)

element = driver.find_element_by_xpath("/html/body")

html = element.get_attribute('outerHTML')

soup = BeautifulSoup(html, 'html.parser')

k = 1

for n in range(1,191):
	time.sleep(3)
	xpath = "/html/body/app-root/app-root/main/dynamic-comp/div/div/bcb-publicacao/div/div/bcb-ultimaspublicacoes/div/div["+str(k)+"]/div[2]/h4/a"
	ata = driver.find_element_by_xpath(xpath)
	driver.execute_script('arguments[0].scrollIntoView(true);', ata)
	ata.click()
	time.sleep(3)
	dl = driver.find_element_by_xpath('//*[@id="publicacao"]/div[1]/div/div/div[2]/div[1]/div[2]/download/div/div/a').click()
	time.sleep(3)
	back = driver.find_element_by_xpath('//*[@id="publicacao"]/div[2]/div/a')
	driver.execute_script('arguments[0].scrollIntoView(true);', back)
	time.sleep(3)
	back.click()
	k += 1
	n = n + 1

driver.quit()