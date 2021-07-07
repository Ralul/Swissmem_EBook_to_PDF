from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os.path

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

outstream = open("Cropped.pdf", "wb")
writer.write(outstream)
outstream.close()