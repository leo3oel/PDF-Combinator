from pdfCombinator import PdfCombinator
import os

if __name__ == "__main__":
    
    itemsInFolder = os.listdir(os.getcwd())
    filesInFolder = [item for item in itemsInFolder if os.path.isfile(item)]
    pdfFiles = sorted([os.path.join(os.getcwd(), file) for file in filesInFolder if file.endswith('.pdf')])

    if len(pdfFiles) > 1:
        PdfCombinator = PdfCombinator(pdfFiles[0], pdfFiles[1], os.path.join(os.getcwd(), "out.pdf"))
        PdfCombinator.outputPdf()
