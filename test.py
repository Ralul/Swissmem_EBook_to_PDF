# save-webpage.py

import urllib.request, urllib.error, urllib.parse

url = 'https://programminghistorian.org/en/lessons/working-with-web-pages'

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('test.html', 'wb')
f.write(webContent)
f.close
