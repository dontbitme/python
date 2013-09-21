#-*- coding:UTF-8 -*-
from bs4 import BeautifulSoup as bs
import urllib2
url="http://w-master.cba.pl/"
page=urllib2.urlopen(url).read()

soup = bs(page)
# print soup.prettify()
l =  soup.findAll("div", attrs={'class': "post"})[-1]
l = str(l)
soup1 = bs(l)
p = soup1.findAll('p')
for e in p:
    print e.content
