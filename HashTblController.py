from HashTbl import *


class HashTblController():

    def __init__(self):
        self.hashTable = HashTbl(10)

    def Insert(self, book):
        self.hashTable.insertSLL(book.title, book)

    def Find(self, book):
        return self.hashTable.getSLL(book)

    def Print(self):
        return str(self.hashTable)
