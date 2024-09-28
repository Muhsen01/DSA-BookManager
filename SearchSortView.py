from tkinter import *
from tkinter import ttk
from SearchSortController import *

class SearchSortView(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("Demonstrate Search and Sort Algorithms")
        self.geometry('900x700')
        frameLeft = Frame(self, width=40, padx=20, pady=20)
        frameLeft.pack(side=LEFT)
        frameRight = Frame(self, width=40, padx=20, pady=20)
        frameRight.pack(side=RIGHT)

        lblAuthor = ttk.Label(frameLeft, text="Current Book List:").pack(padx=10, pady=0)
        vsb=Scrollbar(frameLeft, orient='vertical')
        vsb.pack(side=RIGHT, fill='y')
        self.tboxData = Text(frameLeft, width=60, height=20, yscrollcommand=vsb.set)
        vsb.config(command=self.tboxData.yview)
        self.tboxData.pack()

        #define controller
        self.controller = SearchSortController()

        btnRemBeg = ttk.Button(frameRight, text="Random Array", command=self.RandomArray)
        btnRemBeg.pack(padx=20, pady=10)

        btnRemBeg = ttk.Button(frameRight, text="Import Books", command=self.ImportBooks)
        btnRemBeg.pack(padx=20, pady=10)

        btnBubbleSort = ttk.Button(frameRight, text="Bubble Sort", command=self.BubbleSortBooks)
        btnBubbleSort.pack(padx=20, pady=10)

        btnSelectionSort = ttk.Button(frameRight, text="Selection Sort", command=self.SelectionSortBooks)
        btnSelectionSort.pack(padx=20, pady=10)

        btnInsertionSort = ttk.Button(frameRight, text="Insertion Sort", command=self.InsertionSortBooks)
        btnInsertionSort.pack(padx=20, pady=10)

        btnQuickSort = ttk.Button(frameRight, text="Quick Sort", command=self.QuickSortBooks)
        btnQuickSort.pack(padx=20, pady=10)

        self.chkbxDescVar = BooleanVar()
        chkbxDescSort = Checkbutton(frameRight, text="Descending Sort", variable=self.chkbxDescVar)
        chkbxDescSort.pack(padx=20, pady=20)

    # def Find(self):
    #     foundBook = self.controller.Find(self.getBookData())
    #     self.tboxData.delete("1.0", END)
    #     self.tboxData.insert(INSERT, str(foundBook))

    #display the contents in the display text box
    def UpdateDisplay(self):
        self.tboxData.delete("1.0", END)
        self.tboxData.insert(INSERT, self.controller.Print())

    def ImportBooks(self):
        self.controller.ImportBooks()
        self.UpdateDisplay()

    def RandomArray(self):
        self.controller.RandomArray()
        self.UpdateDisplay()

    def BubbleSortBooks(self):
        self.controller.bubbleSort(not self.chkbxDescVar.get())
        self.UpdateDisplay()

    def SelectionSortBooks(self):
        self.controller.selectionSort(not self.chkbxDescVar.get())
        self.UpdateDisplay()

    def InsertionSortBooks(self):
        self.controller.insertionSort(not self.chkbxDescVar.get())
        self.UpdateDisplay()

    def QuickSortBooks(self):
        self.controller.quickSort(not self.chkbxDescVar.get())
        self.UpdateDisplay()