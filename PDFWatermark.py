import PyPDF2

source_pdf_file_reader = PyPDF2.PdfFileReader(open("test.pdf", mode='rb'))
watermark_pdf_file_reader = PyPDF2.PdfFileReader(open("watermark.pdf", mode='rb'))
writer = PyPDF2.PdfFileWriter()


for i in range(source_pdf_file_reader.getNumPages()):
    pdf_page= source_pdf_file_reader.getPage(i)
    pdf_page.mergePage(watermark_pdf_file_reader.getPage(0))
    writer.addPage(pdf_page)


with open("PDFWatermark.pdf", mode='wb') as watermark_file:
    writer.write(watermark_file)
    
