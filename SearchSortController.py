import csv
from Book import *
import random
from SearchSortFunctions import *

class SearchSortController():
    def __init__(self):
        self.list = []

    def Print(self):
        _str = ""
        if isinstance(self.list[0], Book):
            for item in self.list:
                _str += str(item)
        elif isinstance(self.list[0], int):
            for item in self.list:
                _str += str(item) + "\n"
        return _str

    def ImportBooks(self):
        self.list.clear()
        with open ("C:\\mydata\\books4.csv", 'r', encoding="utf8") as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                title = line[0]
                isbn = int(line[1])
                author = line[2]
                year = int(line[3])
                book = Book(title, isbn, author, year)
                self.list.append(book)
        return

    def RandomArray(self):
        self.list.clear()
        for i in range(10):
            self.list.append(random.randint(100, 999))
        return

    def bubbleSort(self, direction):
        bubbleSort(self.list, direction)
        return

    def selectionSort(self, direction):
        selectionSort(self.list, direction)
        return

    def insertionSort(self, direction):
        selectionSort(self.list, direction)
        return

    def quickSort(self, direction):
        selectionSort(self.list, direction)
        return