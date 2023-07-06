from pypdf import PdfReader, PdfWriter
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as msgbox

class PdfCombinator():

    def __init__(self, firstPdfFilename, secondPdfFilename):
        self.__firstFilename = firstPdfFilename
        self.__secondPdfFilename = secondPdfFilename

    

class MainWin(tk.Tk):

    __firstPdfFilename = ""
    __secondPdfFilename = ""
    __outputPdfFilename = ""

    def __init__(self):

        tk.Tk.__init__(self)
        self.minsize(400,300)
        self.__main_frame = tk.Frame(self)
        self.user_info_label = tk.Label(self)
        self.wm_title("PDF Combinator")

        self.__printWidgets()
        self.mainloop()

    def __printWidgets(self):
        self.__main_frame.columnconfigure(0, weight=1)
        self.__main_frame.columnconfigure(1, weight=1)
        openFirstPdfButton = tk.Button(self.__main_frame, text="Erstes PDF", command=lambda: self.__getPdfName(self.__firstPdfFilename))
        openFirstPdfButton.grid(column=0, row=1)
        openSecondPdfButton = tk.Button(self.__main_frame, text="Erstes PDF", command=lambda: self.__getPdfName(self.__secondPdfFilename))
        openSecondPdfButton.grid(column=1, row=1)
        openOutputPdfButton = tk.Button(self.__main_frame, text="Erstes PDF", command=lambda: self.__getPdfName(self.__outputPdfFilename))
        openOutputPdfButton.grid(column=0, row=2)


    def __getPdfName(self, variable):
        variable = filedialog.askopenfilename()

    def __saveFile(self):
        self.__outputPdfFile = filedialog.asksaveasfile(mode="w", initialfile=".pdf")
        if self.__outputPdfFile:
            self.__outputPdfFilename = self.__outputPdfFile.name
            if not self.__outputPdfFilename.endswith(".pdf"):
                msgbox.showerror("Ungültiger Dateiname", "Bitte Dateiname überprüfen")
                return 0
            self.__outputPdfFile.write(self.__makePdf())
            self.__outputPdfFile.close()

    def __makePdf(self):
        pass

if __name__ == "__main__":
    
    MainWin()
