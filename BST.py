

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None    #first pointer
        self.right = None   #second pointer

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None    #the top part of the tree (starting point)
        self.count = 0
        self.search = 0

    def __str__(self):
        return self._printInorderSTR(self.root)

    def insert(self, data):
        self.count +=1
        node = BSTNode(data)
        if self.root == None:   #checking if the root is empty, if it is then this is the first node
            self.root = node
            return
        else:
            prevNode = self.root
            curNode = self.root
            while curNode != None:
                if data < curNode.data:
                    prevNode = curNode
                    curNode = curNode.left
                elif data > curNode.data:
                    prevNode = curNode
                    curNode = curNode.right
                else:
                    return None

            if data < prevNode.data:
                prevNode.left = node
            elif data > prevNode.data:
                prevNode.right = node
            else:
                return None

    def insertR(self, data):        #using recursion here, and here it calls this function
        self.count +=1
        self.root = self._insertR(self.root, data)

    def _insertR(self, root, data):
        if root is None:
            root = BSTNode(data)
        elif data < root.data:
            root.left = self._insertR(root.left, data)
        elif data > root.data:
            root.right = self._insertR(root.right, data)
        return root

    def printInorder(self):
        self._printInorder(self.root)

    def _printInorder(self, root):      #this function print the numbers in arthimatic order
         if root != None:
             self._printInorder(root.left)
             print(root.data, end="\n")
             self._printInorder(root.right)

    def _printInorderSTR(self, root):
        _str = ""
        if root != None:
             _str += self._printInorderSTR(root.left) + " "
             #print(root.data, end="\n")
             _str += str(root.data) + " "
             _str += self._printInorderSTR(root.right)
        return _str

    def get(self, data):
        return self._get(self.root, data)

    def _get(self, root, data):
        if root == None:
            return None
        elif data < root.data:
            self.search +=1
            return self._get(root.left, data)
        elif data > root.data:
            self.search += 1
            return self._get(root.right, data)
        else:
            return root.data

    def minValueNode(self, root):
        current = root  #current is the node
        while(current.left != None):
            current = current.left
        return current

    def delete(self, data):
        return self._delete(self.root, data)

    def _delete(self, root, data):
        if root == None:
            return root

        if data < root.data:
          root.left = self._delete(root.left, data)
        elif data > root.data:
          root.right = self._delete(root.right, data)

        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp

            temp = self.minValueNode(root.right)    #checking the minimum value on the right side of the tree
            root.data = temp.data   #take the data and copy it to the root
            root.right = self._delete(root.right, temp.data)
        return root
