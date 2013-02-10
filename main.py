"""Lazy4Chan  

Usage:
  l4c.py LINK

"""
from bs4 import BeautifulSoup
import urllib, urllib2
from urlparse import urlparse
import re
import os
from docopt import docopt


def getSoup(link=''):
    print 'Accesing ', link
    page = urllib.urlopen(link)
    html = page.read()
    page.close()
    return BeautifulSoup(html)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    link =  arguments['LINK']
    try:
        soup = getSoup(link)
        folder =  urlparse(link).path.split('/')[-1]
        if not os.path.exists(folder):
        	os.makedirs(folder)
        i = 0
        for span in soup.find_all('span',{'class':'fileText'}):
        	imgLink = re.sub('//','http://',span.find('a')['href'])
        	name = urlparse(imgLink).path.split('/')[-1]
        	img = urllib2.urlopen(imgLink).read()

        	file = open(os.path.join(folder,name),'w+')
        	file.write(img)
        	file.close
        	i += 1
        	print name

        print 'Added %i files' % i
    except:
        print 'No valid link provided'

