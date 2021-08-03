#! /usr/bin/env python3
#-*- coding: utf-8 -*-
import bs4
import requests
import sys
import os


n = int(sys.argv[1])

url = "https://world.openfoodfacts.org/product/{}".format(n)
page = requests.get(url)


soup = bs4.BeautifulSoup(page.text, "html.parser")


#Recupere les noms des produits et les écrit dans le fichier product_data.csv
fichier = open("product_data.csv", "w")

for titre in soup.find_all('title'):
	 fichier.write(titre.text+'\n')
fichier.close()

#scraping de l'url de l'image
links =[]
links = soup.find_all("meta",property="og:image")

#Ecrit url des images dans le fichier product_url.csv
fichier = open("product_url.csv", "w")

for link in links :
	fichier.write(link.get("content"))
	fichier.write('\n')
fichier.close()


os.system("python3 addProduct.py")
