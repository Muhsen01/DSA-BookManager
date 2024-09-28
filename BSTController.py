from BST import *
from Book import *
import csv


class BSTController():

    def __init__(self):
        self.BS = BST()

    def Insert(self, book):
        self.BS.insertR(book)

    def Find(self, book):
        return self.BS.get(book)

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

    def Print(self):
        return str(self.BS)
