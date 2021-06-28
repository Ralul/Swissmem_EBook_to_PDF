import pdfkit, os.path



fh = open("temp/" + "HTML_defragmentation.html")

line = fh.read()

options = {
    'margin-top': '0.0mm',
    'margin-right': '0.0mm',
    'margin-bottom': '0.0mm',
    'margin-left': '0.0mm',
    "page-Height": "147.5mm",
    "page-Width": "100mm",
    'encoding': "UTF-8",
}


pdfkit.from_string(line, "Site_1.pdf", options = options)