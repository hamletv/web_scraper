# import libraries

import urllib2
from bs4 import BeautifulSoup

# get url
getpage = "http://www.bloomberg.com/quote/SPX:IND"

# query website
page = urllib2.urlopen(getpage)

# parse html w/bs and store in var
soup = BeautifulSoup(page, 'html.parser')

