import urllib.request
import os
import pdfkit, os.path

import os.path

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os.path


#Input thrugh user
url = input("Bitte Geben sie hier die URL zur Seite ein:")


#HTML Download
fid=urllib.request.urlopen(url)
webpage=fid.read().decode('utf-8')

print(webpage)


#WebContent is Defragmentation
lines = webpage
lines = lines.replace("localhost", "localhost:7211")

#Special special letters Replace

lines = lines.replace("Ã¶", "ö")
lines = lines.replace("Ã¼", "ü")
lines = lines.replace("Ã¤", "ä")
lines = lines.replace("ÃŸ", "ß")
lines = lines.replace("Ã„", "Ä")

print(lines)


#WKHTMLtoPDF options / Configuratin
options = {
    'margin-top': '0.0mm',
    'margin-right': '0.0mm',
    'margin-bottom': '0.0mm',
    'margin-left': '0.0mm',
    "page-Width" : "5000mm",
    "Page-Height" : "5000mm"
}


#PDF creator

pdfkit.from_string(lines, "Site.pdf", options = options)

#PDF Cropper

pdf_file = PdfFileReader(open("Site.pdf", "rb"))


page = pdf_file.getPage(0)
print(page.cropBox.getLowerRight())
print(page.cropBox.getLowerLeft())
print(page.cropBox.getUpperRight())
print(page.cropBox.getUpperLeft())

writer = PdfFileWriter()

page.cropBox.setLowerLeft((445,612))
page.cropBox.setLowerRight((0,13500))
writer.addPage(page)

outstream = open("Finish.pdf", "wb")
writer.write(outstream)
outstream.close()
