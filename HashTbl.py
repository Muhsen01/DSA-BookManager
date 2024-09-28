import math
from SLL import *


class NodeHT():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        _str = str(self.value)      #convert the value to string
        return _str

    def __eq__(self, other):
        if isinstance(other, str):  #isinstance to check for the data type, ex. in this line we looking for string
            if self.key == other:   #if other is string
                return True
            else:
                return False
        else:
            return False
        #if self.key == other.key:

class HashTbl():
    def __init__(self, size=200):
        self.size = size
        self.table = [SLL()] * size
        self.table = [SLL() for i in range(size)]

    def __str__(self):
        _str = ''
        for value in self.table:
            if str(value) != "None":
                _str += str(value)
        return _str

    def getHash(self, key):
        h = 0
        for char in key:        #for each charachter in the key
            h += ord(char)
        return h % self.size   #to force h to be in range

    def getHash2(self, key):
        h = 0
        for char in key:        #for each charachter in the key
            h += ord(char)
        return (h * h + int(math.sqrt(h))) % self.size

    def insertDblHash(self, key, value):
        hk = self.getHash(key)
        node = Node(key, value)

        if self.table[hk] == None:
            self.table[hk] = node
        else:
            hk = self.getHash2(key)         #to calculate the second gethash2
            if self.table[hk] is None:
                self.table[hk] = node
            else:
                return None

    def getDblHash(self, key):
        h = self.getHash(key)
        if self.table[h] != None:       #is first location empty
            if self.table[h].key == key:        #is node in table KEY node
                return self.table[h]
            else:                               #not in the key
                h = self.getHash2(key)
                if self.table[h] != None:              #is second hash location empty
                    if self.table[h].key == key:       #is node in tablr the KEY node
                        return self.table[h]
                    else:
                        return None     #not the KEY node (second hash location)
        else:
            return None     #first hash location is empty

    def insertOffset(self, key, value):
        hk = self.getHash(key)
        node = Node(key, value)
        if self.table[hk] == None:
            self.table[hk] = node
            return True
        else:
            for i in range(1, 3):       #for loop
                if self.table[hk+i] == None:
                    self.table[hk+i] = node
                    return True

                if self.table [hk-i] == None:
                    self.table[hk-1] = node
                    return True
            return False

    def getOffset(self, key):
        hk = self.getHash(key)
        if self.table[hk] != None:
            if self.table[hk].key == key:
                return self.table[hk].data
        else:
            for i in range(1, 3):
                if self.table[hk+i] != None:
                    if self.table[hk+i].key == key:
                        return self.table[hk+i].data

                if self.table[hk-i] != None:
                    if self.table[hk-i].key == key:
                        return self.table[hk-i].data
        return False

    def insertSLL(self, key, value):
        hk = self.getHash(key)
        node = NodeHT(key, value)
        self.table[hk].AtEnd(node)
        return True

    def getSLL(self, key):
        hk = self.getHash(key)
        node = self.table[hk].GetData(key)
        return node.value
