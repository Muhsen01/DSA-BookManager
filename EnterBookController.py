from SLL import *


class EnterBookController():
    def __init__(self):
        self.ll = SLL()

    def AtBeg(self, book):
        self.ll.AtBeginning(book)

    def RemBeg(self):
        self.ll.RemoveBeginning()

    def AtEnd(self, book):
        self.ll.AtEnd(book)

    def RemEnd(self):
        self.ll.RemoveAtEnd()

    def InOrder(self, book):
        self.ll.InsertInOrder(book)

    def FindBook(self, book):
        return self.ll.GetData(book)

    def Print(self):
        _str = self.ll.Print()
        return _str