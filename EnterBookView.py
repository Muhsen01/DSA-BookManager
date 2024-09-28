from tkinter import *
from tkinter import ttk
from EnterBookController import *
from Book import *


class EnterBookView(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("Enter a Book in Linked List Data Structure")
        self.geometry('600x600')
        frameLeft = Frame(self, width=40, padx=20, pady=20)
        frameLeft.pack(side=LEFT)
        frameRight = Frame(self, width=40, padx=20, pady=20)
        frameRight.pack(side=RIGHT)

        lblFind = ttk.Label(frameLeft, text="Current Book List").pack(padx=10, pady=0)
        self.tboxData = Text(frameLeft, width=30, height=20)
        self.tboxData.pack()

        self.controller = EnterBookController()

        lblTitle = ttk.Label(frameRight, text="Title:").pack(padx=10, pady=0)
        self.entBookTitle = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookTitle.pack(padx=10, pady=10)

        lblISBN = ttk.Label(frameRight, text="ISBN:").pack(padx=10, pady=0)
        self.entBookISBN = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookISBN.pack(padx=10, pady=10)

        lblAuthor = ttk.Label(frameRight, text="Author:").pack(padx=10, pady=0)
        self.entBookAuthor = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookAuthor.pack(padx=10, pady=10)

        lblYear = ttk.Label(frameRight, text="Year:").pack(padx=10, pady=0)
        self.entBookYear = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookYear.pack(padx=10, pady=10)

        btnAtBeg = ttk.Button(frameRight, text="At Beg", command=self.AtBeg)
        btnAtBeg.pack(padx=20, pady=10)

        btnRemBeg = ttk.Button(frameRight, text="Rem Beg", command=self.RemBeg)
        btnRemBeg.pack(padx=20, pady=10)

        btnAtEnd = ttk.Button(frameRight, text="At End", command=self.AtEnd)
        btnAtEnd.pack(padx=20, pady=10)

        btnRemEnd = ttk.Button(frameRight, text="Rem End", command=self.RemEnd)
        btnRemEnd.pack(padx=20, pady=10)

        btnInOrder = ttk.Button(frameRight, text="In Order", command=self.InOrder)
        btnInOrder.pack(padx=20, pady=10)

        lblFind = ttk.Label(frameRight, text="Enter ISBN: ").pack(padx=10, pady=0)
        btnFindBook = ttk.Button(frameRight, text="Find Book", command=self.FindBook)
        btnFindBook.pack(padx=20, pady=10)


    def AtBeg(self):
        self.controller.AtBeg(self.getBookData())
        self.UpdateDisplay()

    def RemBeg(self):
        self.controller.RemBeg()
        self.UpdateDisplay()

    def RemEnd(self):
        self.controller.RemEnd()
        self.UpdateDisplay()

    def AtEnd(self):
        self.controller.AtEnd(self.getBookData())
        self.UpdateDisplay()

    def InOrder(self):
        self.controller.InOrder(self.getBookData())
        self.UpdateDisplay()

    def FindBook(self):
        foundBook = self.controller.FindBook(self.getBookData())
        self.tboxData.delete("1.0", END)
        self.tboxData.insert(INSERT, str(foundBook))

    # collect data from input controls into a Book object
    def getBookData(self):
        book = Book(self.entBookTitle.get(), self.entBookISBN.get(), self.entBookAuthor.get(), self.entBookYear.get())
        return book

    # display the contents in the display text box
    def UpdateDisplay(self):
        self.tboxData.delete("1.0", END)
        self.tboxData.insert(INSERT, self.controller.Print())

