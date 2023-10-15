#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:45:18 2023

@author: ziyan
"""
#import libraries 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import urllib.request
from pprint import pprint

#define url
url = "https://en.wikipedia.org/wiki/Comma-separated_values"

#send get request 
page = requests.get(url)

print(page.text)

#parse the HTML content
soup =  BeautifulSoup(page.content, "html.parser")
print(soup.prettify())

#find table and scrape
table = soup.find("table",{"class":"wikitable"})
data = pd.read_html(str(table))[0]

#save as csv 
data.to_csv("output.csv", index=False)
 