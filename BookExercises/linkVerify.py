#! python3
# link verification

import requests, sys, webbrowser, bs4
#res = requests.get('http://google.com/search?q=' + 'Sherman Firefly')
res = requests.get('https://en.wikipedia.org/wiki/Sherman_Firefly')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.find_all("a")
