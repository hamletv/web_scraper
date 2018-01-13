# import libraries

import urllib2
from bs4 import BeautifulSoup

import csv
from datetime import datetime

# get url
getpage = "http://www.bloomberg.com/quote/SPX:IND"

# get HTML of variable getpage/url
page = urllib2.urlopen(getpage)

# parse html w/bs and store in var
soup = BeautifulSoup(page, 'html.parser')


# take out the <div> of name and get its value
name_box = soup.find("h1", attrs = {"class": "name"})

name = name_box.text.strip()
print name

# get index price
price_box = soup.find("div", attrs = {"class":"price"})
price = price_box.text
print price

# open csv file with append, old data not erased
with open("index.csv", "a") as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([name, price, datetime.now()])

