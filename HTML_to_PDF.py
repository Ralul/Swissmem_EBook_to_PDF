import pdfkit, os.path



fh = open("temp/" + "HTML_defragmentation.html")

line = fh.read()
print (line)
options = {
    'margin-top': '0.0mm',
    'margin-right': '0.0mm',
    'margin-bottom': '0.0mm',
    'margin-left': '0.0mm',
    "page-Width" : "5000mm",
    "Page-Height" : "5000mm"
}


pdfkit.from_string(line, "Site.pdf", options = options)