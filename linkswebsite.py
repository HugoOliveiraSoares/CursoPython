from BeautifulSoup import BeautifulSoup
import urllib3
import re

def getlinks(url):
    html_page = urllib3.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a',
                attrs={'href':re.compile("^http://")}):
            links.append(link.get('href'))

    return links

links = getlinks("http://www.teachmeidea.com")
print(links)