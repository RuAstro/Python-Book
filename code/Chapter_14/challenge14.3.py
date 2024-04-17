from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
import PyPDF2

class PdfFileSplitter:
    def __init__(self, path):
        self.path = path       
        self.reader = PdfReader(open(path, "rb"))
        self.num_pages = self.reader.numPages
        
    def split(self, breakpoint):
        if breakpoint <= 0 or breakpoint >= self.num_pages:
            print("Invalid")
            return None   
    
        #for write to split PDFs
        self.pdf1 = PdfWriter()
        self.pdf2 = PdfWriter()
        
        #loop through each page of pdf
        #if current num page is less than breakpoint, page added to self.pdf1
        #other then that we add it to self.pdf2
        for page_num in range(self.num_pages):
            if page_num < breakpoint:
                self.pdf1.addPage(self.reader.getPage(page_num))
                
            else:
                self.pdf2.addPage(self.reader.getPage(page_num))
    
    
    #takes 2 parameters for split between PDFs
    #self.pfd1 and 2 is to separate files using write method            
    def write(self, filename_1, filename_2, filename):
        filename_1 = filename + "_1.pdf"
        filename_2 = filename + "_2.pdf"
        
        with open(filename_1, "wb") as output_file_1:
            self.pdf1.write(output_file_1)
            
        with open(filename_2, "wb") as output_file_2:
            self.pdf2.write(output_file_2)
            