from bs4 import BeautifulSoup
import urllib, urllib2
from urlparse import urlparse
import re
from datetime import datetime
import os

link='http://boards.4chan.org/b/res/456353246'

def getSoup(link=''):
    print 'Accesing ', link
    page = urllib.urlopen(link)
    html = page.read()
    page.close()
    return BeautifulSoup(html)

if __name__ == '__main__':
    print 'Getting page HTML...'
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

    print 'Added %i filed' % i

