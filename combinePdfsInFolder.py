from pdfCombinator import PdfCombinator
import os

if __name__ == "__main__":
    
    itemsInFolder = os.listdir()
    filesInFolder = [item for item in itemsInFolder if os.path.isfile(item)]
    pdfFiles = sorted([file for file in filesInFolder if file.endswith('.pdf')])

    if len(pdfFiles) > 1:
        PdfCombinator = PdfCombinator(pdfFiles[0], pdfFiles[1], "out.pdf")
        PdfCombinator.outputPdf()
