#Nachrichten
import requests
import json
from flask import Blueprint, render_template
from bs4 import BeautifulSoup
import csv
import urllib

Bahn = Blueprint("Bahn", __name__, template_folder="templates")

headers = {'User-Agent': 'Mozilla/4.0'}

url= "https://www.kvb.koeln/qr/155/"

response = requests.get(url, headers=headers)

html = BeautifulSoup(response.text, 'html.parser')

ziel_html = html.find_all('td', class_='qr_td',text=True)

test = ziel_html[1].get_text()
test_file = open("Bahn\Bahn.txt", "w")
test_file.write(test)
test_file.write("\n")
test_file.close()

for x in range(2, 10):
    test = ziel_html[x].get_text()
    test_file = open("Bahn\Bahn.txt", "a")
    test_file.write(test)
    test_file.write("\n")
    test_file.close()

Bahn_text = open('Bahn\Bahn.txt')
alle = Bahn_text.readlines()
Linie1 = alle[0]
Richtung1 = alle[1]
Zeit1 = alle[2]
Linie2 = alle[3]
Richtung2 = alle[4]
Zeit2 = alle[5]
Linie3 = alle[6]
Richtung3 = alle[7]
Zeit3 = alle[8]
