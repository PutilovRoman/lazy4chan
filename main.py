#!/usr/bin/env python
"""Lazy4Chan  

Usage:
  l4c.py LINK
  l4c.py LINK DIR



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
        
        if arguments['DIR']:
            folder = arguments['DIR']
        else:
            folder =  urlparse(link).path.split('/')[-1]

        if not os.path.exists(folder):
            os.makedirs(folder)

        old = 0
        new = 0
        for span in soup.find_all('span',{'class':'fileText'}):
	    imgLink = re.sub('//','http://',span.find('a')['href'])
	    name = urlparse(imgLink).path.split('/')[-1]

            try:
                with open(os.path.join(folder,name)) as f:
                    old +=1 
            except:
                img = urllib2.urlopen(imgLink).read()
                file = open(os.path.join(folder,name),'w+')
                file.write(img)
                file.close
                new += 1
                print name

        print 'Added %i files. Old files: %i. Total %i' % (new,old, new+old)

    except:
        print 'No valid link provided'

