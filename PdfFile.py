import PyPDF2
import os

with open("test.pdf", mode='rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    writer=PyPDF2.PdfFileWriter()
    print(reader.getNumPages())
    page=reader.getPage(3)
    page.rotateClockwise(90)
    writer.addPage(page)
    if not os.path.isfile("tilt.pdf"):
        with open("tilt.pdf",'wb') as tilt_file:
                writer.write(tilt_file)
    else:
        print("file is preset already")







