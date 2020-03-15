import bs4 as bs
import urllib.request

site = " "

sauce = urllib.request.urlopen(site)
soup  = bs.BeautifulSoup(sauce, "lxml")