from pypdf import PdfReader, PdfWriter
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as msgbox
import webbrowser

class PdfCombinator():

    __firstPDF = None
    __secondPDF = None

    def __init__(self, firstPdfFilename, secondPdfFilename, outFilename):
        self.__firstFilename = firstPdfFilename
        self.__secondPdfFilename = secondPdfFilename
        self.__outFilename = outFilename
        self.__readPdfs()
    
    def __readPdfs(self):
        self.__firstPDF = PdfReader(self.__firstFilename) 
        self.__secondPDF = PdfReader(self.__secondPdfFilename)

    def outputPdf(self):
        outputPdf = PdfWriter()
        outputPdf = self.__addPages(outputPdf)
        outputPdf = self.__addExtraPagesOfSecondPdf(outputPdf)
        outputPdf.write(self.__outFilename)

    def __addPages(self, outputPdf):
        for index in range(len(self.__firstPDF.pages)):
            outputPdf.add_page(self.__firstPDF.pages[index])
            outputPdf.add_page(self.__secondPDF.pages[index])
        return outputPdf
    
    def __addExtraPagesOfSecondPdf(self, outputPdf):
        if len(self.__firstPDF.pages) < len(self.__secondPDF.pages):
            for index in range(len(self.__firstPDF.pages), len(self.__secondPDF.pages)):
                outputPdf.add_page(self.__secondPDF.pages[index])
        return outputPdf


class MainWin(tk.Tk):

    __firstPdfFilename = ""
    __secondPdfFilename = ""
    __outputPdfFilename = ""

    def __init__(self):

        tk.Tk.__init__(self)
        self.__main_frame = tk.Frame(self)
        self.user_info_label = tk.Label(self)
        self.wm_title("PDF Combinator")

        self.__printWidgets()
        self.mainloop()

    def __printWidgets(self):
        self.__main_frame.columnconfigure(0, weight=1)
        self.__main_frame.columnconfigure(1, weight=1)
        openFirstPdfButton = tk.Button(self, text="Erstes PDF", command=self.__getFirstName)
        openFirstPdfButton.grid(column=0, row=1, pady=5, padx=5)
        openSecondPdfButton = tk.Button(self, text="Zweites PDF", command=self.__getSecondName)
        openSecondPdfButton.grid(column=1, row=1, pady=5, padx=5)
        openOutputPdfButton = tk.Button(self, text="Output Pfad", command=self.__saveFile)
        openOutputPdfButton.grid(column=0, row=2, columnspan=2, pady=5, padx=5)

    def __getFirstName(self):
        self.__firstPdfFilename = filedialog.askopenfilename()

    def __getSecondName(self):
        self.__secondPdfFilename = filedialog.askopenfilename()

    def __saveFile(self):
        self.__outputPdfFile = filedialog.asksaveasfile(mode="w", initialfile=".pdf")
        if not self.__firstPdfFilename or not self.__secondPdfFilename:
            msgbox.showerror("Keine PDfs ausgewählt", "Bitte beide PDFs auswählen")
        if self.__outputPdfFile:
            self.__outputPdfFilename = self.__outputPdfFile.name
            if not self.__outputPdfFilename.endswith(".pdf"):
                msgbox.showerror("Ungültiger Dateiname", "Bitte Dateiname überprüfen")
                return 0
            self.__makePdf()

    def __makePdf(self):
        pdfCombinator = PdfCombinator(self.__firstPdfFilename, self.__secondPdfFilename, self.__outputPdfFilename)
        pdfCombinator.outputPdf()
        webbrowser.open_new("file://" + self.__outputPdfFilename)

if __name__ == "__main__":
    
    MainWin()
