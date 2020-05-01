import PyPDF2
import os

watermark_file = "watermark.pdf"


source_file_reader = PyPDF2.PdfFileReader("test.pdf")
watermark_file_reader = PyPDF2.PdfFileReader(watermark_file)
writer = PyPDF2.PdfFileWriter()


pdf_page = source_file_reader.getPage(0)
watermark_page = watermark_file_reader.getPage(0)

pdf_page.mergePage(watermark_page)

writer.addPage(pdf_page)

if not os.path.exists("new_watermark.pdf"):
    with open("new_watermark.pdf", mode='wb') as output:
        writer.write(output)
else:
    print("file is already present")



# for pdf_page in source_file_reader.:
