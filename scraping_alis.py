#Importando a Biblioteca
import bs4
import urllib.request as urllib_request
import pandas as pd 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
from urllib.error import URLError, HTTPError
from urllib.request import urlretrieve

print("BeautifulSoup ->", bs4.__version__)
print("urllib ->", urllib_request.__version__)
print("pandas ->", pd.__version__)

#DECLARANDO CARDS
cards = []


#DEFININDO HTML E URL 
url = 'https://www.alisoficial.com.br/loja?filtro=&pg=1'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    html = response.read().decode('UTF-8')
       
except HTTPError as e:
    print(e.status, e.reason)
    
except URLError as e:
    print(e.reason)
     
def trata_html(html):
    return " ".join(input.split()).replace('> <', '><')

soup = BeautifulSoup(html, 'html.parser')

pages = int(str(soup.find('ul', {'class': "paginacao clear clearfix"}))[-11])


#anuncio = soup.find('div', {'class': 'produto-item swiper-slide'})
#print("A calça custa", anuncio.find('h4', {'class': 'produto-item-preco'}).get_text())


## Iterando por todas as páginas do site
for i in range(pages):
    ## Obtendo o HTML
    response = urlopen('https://www.alisoficial.com.br/loja?filtro=&pg=0' + str(i + 1))
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # Obtendo as TAGs de interesse
    anuncios = soup.find('div', {"class": "produtos clearfix"}).findAll('div', class_="produto-item swiper-slide")

    # Coletando as informações dos CARDS
    for anuncio in anuncios:
        card = {}

        # Valor
        card['nome'] = anuncio.find('h2', {'class': 'produto-item-nome'}).get_text()
        card['value'] = anuncio.find('h4', {'class': 'produto-item-preco'}).get_text()[0:8]
        # Informações
        #infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')
        #for info in infos:
        #    card[info.get('class')[0].split('-')[-1]] = info.get_text()

        # Acessórios
        #items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
        #items.pop()
        #acessorios = []
       #for item in items:
        #    acessorios.append(item.get_text().replace('► ', ''))
        #card['items'] = acessorios

        # Imagens
        #image = soup.find('div', {'class': 'produto-item swiper-slide'}).img
        #print(image.get('data-original'))
        #card['image'] = image.get('data-original') 

        # Adicionando resultado a lista cards
        cards.append(card)
         

print(len(cards))
#print(image)
# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
print(dataset)
dataset.to_csv('./testes/alis.csv', sep=';', index = False, encoding = 'utf-8-sig')
#print(dataset)

