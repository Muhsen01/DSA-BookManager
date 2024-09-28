from tkinter import *
from tkinter import ttk
from BSTController import *
from Book import *


class BSTView(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("Enter a Book in Binary Search Tree Data Structure")
        self.geometry('600x600')
        frameLeft = Frame(self, width=40, padx=20, pady=20)
        frameLeft.pack(side=LEFT)
        frameRight = Frame(self, width=40, padx=20, pady=20)
        frameRight.pack(side=RIGHT)

        lblFind = ttk.Label(frameLeft, text="Current Book List")
        lblFind.pack(padx=10, pady=0)
        self.tboxData = Text(frameLeft, width=30, height=20)
        self.tboxData.pack()

        self.controller = BSTController()

        lblTitle = ttk.Label(frameRight, text="Title:")
        lblTitle.pack(padx=10, pady=0)
        self.entBookTitle = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookTitle.pack(padx=10, pady=10)

        lblISBN = ttk.Label(frameRight, text="ISBN:")
        lblISBN.pack(padx=10, pady=0)
        self.entBookISBN = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookISBN.pack(padx=10, pady=10)

        lblAuthor = ttk.Label(frameRight, text="Author:")
        lblAuthor.pack(padx=10, pady=0)
        self.entBookAuthor = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookAuthor.pack(padx=10, pady=10)

        lblYear = ttk.Label(frameRight, text="Year:")
        lblYear.pack(padx=10, pady=0)
        self.entBookYear = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entBookYear.pack(padx=10, pady=10)

        btnInsertSLL = ttk.Button(frameRight, text="Insert", command=self.insert)
        btnInsertSLL.pack(padx=20, pady=10)

        lblFind = ttk.Label(frameRight, text="Enter ISBN: ")
        lblFind.pack(padx=10, pady=0)
        self.entFindISBN = ttk.Entry(frameRight, font=('Helvetica', 12), width=20)
        self.entFindISBN.pack(padx=10, pady=10)
        btnFindBook = ttk.Button(frameRight, text="Find Book", command=self.Find)
        btnFindBook.pack(padx=20, pady=10)

        btnRemBeg = ttk.Button(frameRight, text="Import", command=self.ImportBooks)
        btnRemBeg.pack(padx=20, pady=10)

    def insert(self):
        self.controller.Insert(self.getBookData())
        self.UpdateDisplay()

    def Find(self):
        #foundBook = self.controller.FindBook(self.getBookData())
        self.tboxData.delete("1.0", END)
        #self.tboxData.insert(INSERT, str(foundBook))

    def ImportBooks(self):
        self.controller.ImportBooks()
        self.UpdateDisplay()

    # collect data from input controls into a Book object
    def getBookData(self):
        book = Book(self.entBookTitle.get(), self.entBookISBN.get(), self.entBookAuthor.get(), self.entBookYear.get())
        return book

    # display the contents in the display text box
    def UpdateDisplay(self):
        self.tboxData.delete("1.0", END)
        self.tboxData.insert(INSERT, self.controller.Print())

