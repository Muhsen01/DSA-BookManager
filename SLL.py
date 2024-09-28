
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        _str = str(self.data)  # convert the data to string
        return _str

class SLL:
    def __init__(self):
        self.head = None

    def __str__(self):
        _str = ''
        current = self.head
        while current:
            _str += str(current)
            current = current.next
        return _str

    def AtBeginning(self, data):
        newNode = Node(data)        #allocate new node
        newNode.next = self.head    #point new node next to original head
        self.head = newNode         #change head to point to new node

    def AtEnd(self, data):
        newNode = Node(data)        #create new node

        if self.head is None:
            self.head = newNode
            return

        curNode = self.head
        while curNode.next is not None:  #walk to end of list
            curNode = curNode.next

        curNode.next = newNode      #attach new node to end of list

    def Print(self):
        _str = ""
        if self.head is None:
            return ("List is Empty")
            #print("List is Empty")
            return

        curNode = self.head
        while curNode is not None:
            _str += str(curNode.data)
            #print(curNode.data)
            curNode = curNode.next

        return _str

    def InsertInOrder(self, data):
        newNode = Node(data)

        if self.head is None:       #only node in list
            self.head = newNode
            return

        curNode = self.head
        if(newNode.data < curNode.data): #less than original head
            newNode.next = self.head
            self.head = newNode
            return

        prevNode = curNode
        while (curNode.data < newNode.data): #looking for right place
            if curNode.next is None:
                curNode.next = newNode
                return
            prevNode = curNode
            curNode = curNode.next

        newNode.next = curNode
        prevNode.next = newNode

    def RemoveBeginning(self):
        if self.head == None:
            return None
        else:
            self.head = self.head.next

    def RemoveAtEnd(self):
        if self.head == None:
            return None
        else:
            curNode = self.head
            prevNode = self.head
            while curNode.next != None:
                prevNode = curNode
                curNode = curNode.next
            prevNode.next = None

    def GetData(self, data):
        if self.head == None:
            return None
        else:
            curNode = self.head
            while curNode.next != None and curNode.data != data:
                   curNode = curNode.next

            if curNode.data == data:
                return curNode.data
            else:
                return None

