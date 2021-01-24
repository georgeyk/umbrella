from weasyprint import HTML

# https://github.com/Kozea/WeasyPrint/tree/gh-pages/samples/invoice
HTML("invoice/invoice.html").write_pdf("output/output.pdf")
