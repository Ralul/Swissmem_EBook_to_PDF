import pdfkit


options = {
    'page-size': 'B6',
    'pageWidth':
}

pdfkit.from_file('HTML_def.html', 'Swissmem_B6.pdf', options=options)

