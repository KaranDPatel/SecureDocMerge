import os
from PyPDF2 import PdfFileMerger

path='D:\\PythonScripts\\MergePdf\\pdf\\'
x = [a for a in os.listdir(path) if a.endswith(".pdf")]

print(x)
merger = PdfFileMerger()

for pdf in x:
    merger.append(open(path+pdf, 'rb'))

with open("MergePdfFiles.pdf", "wb") as fout:
    merger.write(fout)