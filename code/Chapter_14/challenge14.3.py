from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

class PdfFileSplitter:
    def __init__(self, path):
        self.path = path       
        self.reader = PyPDF2.PdfReader(open(path, "rb"))
        self.num_pages = self.reader.numPages
        
    def split(self, breakpoint):
        if breakpoint <= 0 or breakpoint >= self.num_pages:
            print("Invalid")
            return None    