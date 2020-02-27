"""import PyPDF2
#convert pdf to text file..
def pdftotxt(pdfname):
    pdfob=PyPDF2.PdfFileReader(pdfname)
    with open('G:/Pycharm/pycharm_programs/CTYHP/test.txt','w') as f:
        for i in range(pdfob.getNumPages()):
            data=pdfob.getPage(i).extractText()
            #print(data)
            f.write(data)

fname=input("Enter the pdf file name:")
pdftotxt(fname)
G:/TEXT/5th SEM/iot unit 2/UNIT II-5TH SEM/Communications Module/GSM Module/Programming Arduino with GSM Module.pdf
"""
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    with open('G:/Pycharm/Pycharm Projects/CTYHP/t2.txt','w') as f:
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
            data =  retstr.getvalue()

        #print(data)
        f.write(data)
    print("done")

if __name__ == '__main__':
    pdfparser('C:/Users/Shobha/Desktop/table.pdf')
