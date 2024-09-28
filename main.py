from tkinter import *
from EnterBookView import *
# from LinkedListView import *
# from StackView import *
# from QueueView import *
from HashTblView import *
# import llPayload as pl
# import Person as pe
from SearchSortView import *
from BSTView import *

# Create an instance of tkinter frame or widget
win = Tk()
win.geometry("400x400")
win.title("Data Structures and Algorithms")


heading = ttk.Label(win, text="Data Structure and Algorithm Analysis", font=("Arial", 16))
heading.grid(row=3, column = 2, padx=10, pady=10)


# btnStack = ttk.Button(win, text="Stacks", command=lambda:StackWindow()).grid(row=6, column=2, padx=10, pady=10)
# btnQueue = ttk.Button(win, text="Queues", command=lambda:QueueWindow()).grid(row=7, column=2, padx=10, pady=10)
btnEnterBook = ttk.Button(win, text="Books In Linked List", command=lambda:EnterBookView()).grid(row=9, column=2, padx=10, pady=10)
btnHashTbl = ttk.Button(win, text="Books In Hash Tables", command=lambda:HashTblView()).grid(row=10, column=2, padx=10, pady=10)
btnBST = ttk.Button(win, text="Books In Binary Search", command=lambda:BSTView()).grid(row=11, column=2, padx=10, pady=10)
btnSearchSort = ttk.Button(win, text="Search/Sort", command=lambda:SearchSortView()).grid(row=12, column=2, padx=10, pady=10)
#btnGraph = ttk.Button(win, text="Graph Data", command=lambda:GraphView()).grid(row=13, column=2, padx=10, pady=10)


win.mainloop()
