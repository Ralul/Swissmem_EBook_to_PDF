import urllib.request, urllib.error, urllib.parse

url = 'http://localhost:7211/database/resource/pk/2114'

response = urllib.request.urlopen(url)
webContent = response.read()

f = open('HTML_Download.HTML', 'wb')
f.write(webContent)
f.close

