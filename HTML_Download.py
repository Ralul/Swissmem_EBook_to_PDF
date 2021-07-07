import urllib.request, urllib.parse, os.path

url = 'http://localhost:7211/database/resource/pk/2601'


response = urllib.request.urlopen(url)
webContent = response.read()

print(webContent)
print(type(webContent))

save_path = 'Temp'
name_of_file = "HTML_Download.HTML"

completeName = os.path.join(save_path, name_of_file)

file1 = open(completeName, "wb")

file1.write(webContent)
file1.close()
